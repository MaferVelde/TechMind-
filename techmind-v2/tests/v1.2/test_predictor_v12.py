"""Smoke/regression tests del predictor TechMind v1.2."""

from __future__ import annotations

from pathlib import Path
import gc

import numpy as np
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

EXPECTED_SHA256 = (
    "1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61"
)

VALID_CLASSES = {
    "backend",
    "cloud",
    "datascience",
    "frontend",
}

VALID_DECISIONS = {
    "accepted",
    "review",
    "rejected_ood",
    "rejected_invalid",
}


@pytest.fixture(scope="module")
def predictor():
    model = TechMindPredictor(MODEL_PATH)

    yield model

    del model
    gc.collect()


def test_model_info(predictor: TechMindPredictor) -> None:
    info = predictor.model_info()

    assert info["version"] == "1.2.0-multilingual"
    assert info["status"] == "validated_experimental_candidate"
    assert info["classifier"] == "LinearSVC"
    assert float(info["classifier_C"]) == 0.3
    assert int(info["embedding_dimension"]) == 384

    assert set(info["classes"]) == VALID_CLASSES

    assert info["domain_control"]["threshold"] == 0.4266
    assert info["domain_control"]["n_neighbors"] == 5

    assert (
        info["confidence_control"]["threshold"]
        == 0.8132
    )

    assert info["artifact_sha256"] == EXPECTED_SHA256
    assert info["scores_are_probabilities"] is False


def test_predictor_backend_regression(
    predictor: TechMindPredictor,
) -> None:
    result = predictor.predict(
        (
            "Crear un endpoint REST que valide la solicitud "
            "y guarde el usuario en la base de datos."
        ),
        top_k=4,
    )

    assert result["model_version"] == "1.2.0-multilingual"
    assert result["model_status"] == "validated_experimental_candidate"
    assert result["n_inputs"] == 1

    item = result["predictions"][0]

    required_fields = {
        "index",
        "text",
        "valid_input",
        "decision",
        "prediction",
        "second_category",
        "decision_margin",
        "domain_similarity_5nn",
        "tfidf_active_features",
        "reason",
        "score_top1",
        "score_top2",
        "top_k",
    }

    assert required_fields.issubset(item.keys())

    assert item["valid_input"] is True
    assert item["prediction"] == "backend"
    assert item["decision"] == "accepted"

    assert item["second_category"] in VALID_CLASSES
    assert item["decision"] in VALID_DECISIONS

    assert np.isfinite(item["score_top1"])
    assert np.isfinite(item["score_top2"])
    assert np.isfinite(item["decision_margin"])
    assert np.isfinite(item["domain_similarity_5nn"])

    assert item["decision_margin"] >= predictor.margin_threshold
    assert (
        item["domain_similarity_5nn"]
        >= predictor.domain_threshold
    )

    assert item["tfidf_active_features"] > 0

    assert len(item["top_k"]) == 4
    assert {
        entry["category"]
        for entry in item["top_k"]
    } == VALID_CLASSES


def test_predictor_explanation(
    predictor: TechMindPredictor,
) -> None:
    result = predictor.predict(
        (
            "Train a classifier with cross validation and "
            "evaluate precision recall and F1."
        ),
        include_explanation=True,
        explanation_top_n=8,
        top_k=4,
    )

    item = result["predictions"][0]

    assert "explanation" in item

    explanation = item["explanation"]

    assert explanation["available"] is True
    assert explanation["scope"] == "tfidf_differential_only"
    assert isinstance(explanation["terms"], list)
    assert len(explanation["terms"]) <= 8
