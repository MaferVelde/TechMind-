"""Pruebas de los controles operativos de TechMind v1.2."""

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


def test_thresholds_are_frozen(predictor: TechMindPredictor) -> None:
    assert predictor.domain_n_neighbors == 5
    assert predictor.domain_threshold == 0.4266
    assert predictor.margin_threshold == 0.8132


def test_four_operational_states(predictor: TechMindPredictor) -> None:
    result = predictor.predict(
        [
            "Crear un endpoint REST que valide la solicitud y guarde el usuario en la base de datos.",
            "Store application backups in object storage with lifecycle policies.",
            "Preparar una tortilla de patatas con huevos, cebolla y aceite de oliva.",
            "",
        ]
    )

    predictions = result["predictions"]

    assert predictions[0]["decision"] == "accepted"
    assert predictions[0]["reason"] is None

    assert predictions[1]["decision"] == "review"
    assert predictions[1]["reason"] == "low_decision_margin"
    assert predictions[1]["domain_similarity_5nn"] >= predictor.domain_threshold
    assert predictions[1]["decision_margin"] < predictor.margin_threshold

    assert predictions[2]["decision"] == "rejected_ood"
    assert predictions[2]["reason"] == "low_semantic_domain_support"
    assert predictions[2]["domain_similarity_5nn"] < predictor.domain_threshold

    assert predictions[3]["decision"] == "rejected_invalid"
    assert predictions[3]["reason"] == "invalid_input"
    assert predictions[3]["prediction"] is None
    assert predictions[3]["decision_margin"] is None
    assert predictions[3]["domain_similarity_5nn"] is None


def test_summary_matches_decisions(predictor: TechMindPredictor) -> None:
    result = predictor.predict(
        [
            "Crear un endpoint REST que valide la solicitud y guarde el usuario en la base de datos.",
            "Store application backups in object storage with lifecycle policies.",
            "Preparar una tortilla de patatas con huevos, cebolla y aceite de oliva.",
            "",
        ]
    )

    assert result["summary"] == {
        "accepted": 1,
        "review": 1,
        "rejected_ood": 1,
        "rejected_invalid": 1,
    }
