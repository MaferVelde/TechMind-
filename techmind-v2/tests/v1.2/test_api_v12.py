"""Pruebas FastAPI de TechMind v1.2."""

from __future__ import annotations

from pathlib import Path
import os
import gc

import pytest
from fastapi.testclient import TestClient


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

# Debe establecerse antes de importar main.py,
# porque MODEL_PATH se resuelve durante el import.
os.environ["TECHMIND_V12_MODEL_PATH"] = str(MODEL_PATH)

from techmind_api_v12.main import app  # noqa: E402


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client

    gc.collect()


def test_health(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["model_loaded"] is True
    assert data["api_version"] == "1.2.0"
    assert data["model_version"] == "1.2.0-multilingual"


def test_model_info(client: TestClient) -> None:
    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()

    assert data["api_version"] == "1.2.0"
    assert data["version"] == "1.2.0-multilingual"
    assert data["status"] == "validated_experimental_candidate"
    assert data["classifier"] == "LinearSVC"
    assert float(data["classifier_C"]) == 0.3
    assert int(data["embedding_dimension"]) == 384
    assert data["artifact_sha256"] == EXPECTED_SHA256
    assert data["scores_are_probabilities"] is False


def test_predict(client: TestClient) -> None:
    response = client.post(
        "/predict",
        json={
            "texts": [
                (
                    "Train a classification model and evaluate "
                    "precision recall and F1."
                ),
                (
                    "Preparar una pizza con tomate y queso."
                ),
            ],
            "include_explanation": False,
            "top_k": 4,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["model_version"] == "1.2.0-multilingual"
    assert data["n_inputs"] == 2
    assert len(data["predictions"]) == 2

    technical = data["predictions"][0]
    ood = data["predictions"][1]

    assert technical["prediction"] == "datascience"
    assert technical["decision"] in {
        "accepted",
        "review",
    }

    assert ood["decision"] == "rejected_ood"


def test_openapi_contract(client: TestClient) -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200

    paths = set(
        response.json()["paths"].keys()
    )

    assert {
        "/",
        "/health",
        "/model-info",
        "/predict",
    }.issubset(paths)
