"""Pruebas de regresión multilingual de TechMind v1.2."""

from __future__ import annotations

import gc
from pathlib import Path

import pytest

from techmind_v12 import TechMindPredictor


ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    ROOT
    / "models"
    / "experimental"
    / "v1.2.0-multilingual"
    / "techmind_hybrid_v1_2_0_multilingual.joblib"
)


@pytest.fixture(scope="module")
def predictor():
    model = TechMindPredictor(MODEL_PATH)
    yield model
    del model
    gc.collect()


def test_multilingual_regression(predictor: TechMindPredictor) -> None:
    texts = [
        "Crear un endpoint REST que valide la solicitud y guarde el usuario en la base de datos.",
        "Store application backups in object storage with lifecycle policies.",
        "Обучить модель классификации и оценить precision, recall и F1.",
        "Crear un responsive component con CSS Grid y keyboard accessibility.",
    ]

    expected_categories = [
        "backend",
        "cloud",
        "datascience",
        "frontend",
    ]

    result = predictor.predict(texts, top_k=4)

    assert result["n_inputs"] == 4
    assert len(result["predictions"]) == 4

    for item, expected in zip(result["predictions"], expected_categories):
        assert item["valid_input"] is True
        assert item["prediction"] == expected
        assert item["decision"] in {"accepted", "review"}
        assert item["domain_similarity_5nn"] >= predictor.domain_threshold


def test_known_multilingual_operational_behavior(
    predictor: TechMindPredictor,
) -> None:
    result = predictor.predict(
        [
            "Crear un endpoint REST que valide la solicitud y guarde el usuario en la base de datos.",
            "Store application backups in object storage with lifecycle policies.",
            "Обучить модель классификации и оценить precision, recall и F1.",
            "Crear un responsive component con CSS Grid y keyboard accessibility.",
        ]
    )

    decisions = [item["decision"] for item in result["predictions"]]

    assert decisions[0] == "accepted"
    assert decisions[1] == "review"
    assert decisions[2] == "accepted"
    assert decisions[3] == "accepted"
