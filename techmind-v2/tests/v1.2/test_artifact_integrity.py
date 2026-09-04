"""Pruebas de integridad del artefacto TechMind v1.2.0-multilingual."""

from __future__ import annotations

import hashlib
from pathlib import Path

import joblib
import numpy as np
from sklearn.svm import LinearSVC


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

EXPECTED_CLASSES = [
    "backend",
    "cloud",
    "datascience",
    "frontend",
]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)

    return digest.hexdigest()


def test_artifact_exists() -> None:
    assert MODEL_PATH.exists(), f"No se encontró el artefacto v1.2: {MODEL_PATH}"
    assert MODEL_PATH.is_file()


def test_artifact_sha256() -> None:
    assert _sha256(MODEL_PATH) == EXPECTED_SHA256


def test_artifact_metadata_and_architecture() -> None:
    artifact = joblib.load(MODEL_PATH)

    required_keys = {
        "version",
        "status",
        "features",
        "classifier",
        "classifier_C",
        "embedding_model",
        "embedding_dimension",
        "normalize_embeddings",
        "classes",
        "domain_reference_embeddings",
        "domain_control",
        "confidence_control",
        "architecture",
    }

    assert required_keys.issubset(artifact.keys())
    assert artifact["version"] == "1.2.0-multilingual"
    assert artifact["status"] == "validated_experimental_candidate"

    classifier = artifact["classifier"]
    assert isinstance(classifier, LinearSVC)
    assert float(artifact["classifier_C"]) == 0.3

    assert (
        artifact["embedding_model"]
        == "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    assert int(artifact["embedding_dimension"]) == 384
    assert bool(artifact["normalize_embeddings"]) is True
    assert list(artifact["classes"]) == EXPECTED_CLASSES

    assert classifier.n_features_in_ == 60384
    assert classifier.coef_.shape == (4, 60384)
    assert np.isfinite(classifier.coef_).all()
    assert np.isfinite(classifier.intercept_).all()


def test_domain_reference_embeddings() -> None:
    artifact = joblib.load(MODEL_PATH)

    references = np.asarray(
        artifact["domain_reference_embeddings"],
        dtype=np.float32,
    )

    assert references.shape == (3666, 384)
    assert np.isfinite(references).all()

    norms = np.linalg.norm(references, axis=1)
    assert np.allclose(norms, 1.0, atol=1e-4)


def test_operational_thresholds_in_artifact() -> None:
    artifact = joblib.load(MODEL_PATH)

    domain = artifact["domain_control"]
    confidence = artifact["confidence_control"]

    assert domain["metric"] == "mean_cosine_similarity_5nn"
    assert int(domain["n_neighbors"]) == 5
    assert float(domain["threshold"]) == 0.4266

    assert confidence["metric"] == "top1_minus_top2_decision_margin"
    assert float(confidence["threshold"]) == 0.8132
