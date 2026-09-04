# Deployment — v1.2.0-multilingual

## Objetivo

Desplegar el microservicio de Ciencia de Datos de forma reproducible y aislada mediante Docker.

## Componentes

```text
techmind_v12/
techmind_api_v12/
models/experimental/v1.2.0-multilingual/
deploy/v1.2.0-multilingual/
```

## Artefacto

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

El Dockerfile valida este hash durante el build.

## Imagen Docker

Tag recomendado:

```text
techmind:v1.2.0-multilingual
```

Base:

```text
python:3.11-slim-bookworm
```

Runtime:

```text
Python 3.11
FastAPI
Uvicorn
Scikit-Learn
Sentence Transformers
Transformers
PyTorch CPU
Joblib
NumPy
SciPy
```

## PyTorch

Versión CPU-only:

```text
torch==2.13.0+cpu
```

Índice:

```text
https://download.pytorch.org/whl/cpu
```

Esto evita dependencias CUDA/NVIDIA innecesarias.

## MiniLM

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

En runtime:

```text
local_files_only=True
```

Variables offline:

```text
HF_HUB_OFFLINE=1
TRANSFORMERS_OFFLINE=1
HF_HUB_DISABLE_TELEMETRY=1
TOKENIZERS_PARALLELISM=false
```

## API

Paquete:

```text
techmind_api_v12/
```

Versión API:

```text
1.2.0
```

Modelo:

```text
1.2.0-multilingual
```

Endpoints:

```text
GET  /
GET  /health
GET  /model-info
POST /predict
GET  /docs
GET  /redoc
GET  /openapi.json
```

## Healthcheck

```http
GET /health
```

Respuesta esperada:

```json
{
  "status": "ok",
  "model_loaded": true,
  "api_version": "1.2.0",
  "model_version": "1.2.0-multilingual"
}
```

## Model Info

```http
GET /model-info
```

Debe reportar:

```text
model_version = 1.2.0-multilingual
status = validated_experimental_candidate
classifier = LinearSVC
classifier_C = 0.3
embedding_dimension = 384
scores_are_probabilities = false
artifact_sha256 =
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

## Build

```bash
docker build   --progress=plain   -f deploy/v1.2.0-multilingual/docker/Dockerfile   -t techmind:v1.2.0-multilingual   .
```

Durante el build deben verificarse:

```text
TORCH_CPU_OK
SHA256 OK
MINILM_BUILD_OK
```

## Docker Compose

```bash
docker compose   -f deploy/v1.2.0-multilingual/docker/compose.yaml   up -d
```

## Estado esperado

```bash
docker inspect techmind-v12   --format '{{.State.Status}} / {{.State.Health.Status}}'
```

```text
running / healthy
```

## Smoke Test

```bash
python deploy/v1.2.0-multilingual/docker/smoke_test_docker.py
```

Valida:

```text
/health
/model-info
SHA256
/predict
English
Español
Русский
OOD
```

Resultado certificado:

```text
DOCKER SMOKE TEST PASSED
```

## Predictor

Paquete:

```text
techmind_v12/
```

Firma pública:

```python
predict(
    texts,
    include_explanation=False,
    explanation_top_n=8,
    top_k=None
)
```

## Decisiones

```text
accepted
review
rejected_ood
rejected_invalid
```

Backend debe usar `decision` como autoridad.

## Scores

`score_top1` y `score_top2` no son probabilidades.

## Rollback

```text
v1.1.0 = baseline estable / fallback
v1.2.0-multilingual = validated_experimental_candidate
```

## Logging recomendado

```text
timestamp
model_version
decision
prediction
second_category
decision_margin
domain_similarity_5nn
reason
latency_ms
```
