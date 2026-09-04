# Changelog

Todos los cambios relevantes de **TechMind** se documentan en este archivo.

El proyecto utiliza versionado semántico para distinguir la evolución del modelo, del package y de la interfaz API.

---

## [1.2.0-multilingual]

### Status

```text
validated_experimental_candidate
```

`v1.1.0` se conserva como **stable baseline / fallback**.

### Added

- Arquitectura multilingual híbrida:
  - **TF-IDF Word**
  - **TF-IDF Character**
  - **MiniLM Multilingual**
  - **LinearSVC**
- Modelo de embeddings:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

- Embeddings semánticos de `384` dimensiones.
- Normalización L2 de embeddings.
- Soporte multilingual evaluado para:
  - Español (`es`)
  - Inglés (`en`)
  - Ruso (`ru`)
  - Español/Inglés (`es_en`)
- Nuevo package de inferencia:

```text
techmind_v12/
```

- Nueva API para v1.2:

```text
techmind_api_v12/
```

- Nuevos estados operacionales:
  - `accepted`
  - `review`
  - `rejected_ood`
  - `rejected_invalid`
- Control de confianza mediante **Decision Margin**.
- Control de soporte semántico mediante **5-Nearest Neighbors con similitud coseno**.
- Benchmark multilingual de desarrollo:

```text
data/evaluation/multilingual_benchmark.csv
```

- Benchmark multilingual final independiente:

```text
data/evaluation/multilingual_final_benchmark_v1.csv
```

- Challenge OOD controlado:

```text
data/evaluation/ood_challenge_v1.csv
```

- Documentación específica de versión:

```text
docs/versions/v1.2.0-multilingual/
```

- Paquete de deployment:

```text
deploy/v1.2.0-multilingual/
```

- Docker CPU-only para v1.2.
- Verificación SHA-256 del artefacto durante build.
- Carga offline de MiniLM en runtime.
- Smoke test Docker para:
  - `/health`
  - `/model-info`
  - `/predict`
  - Inglés
  - Español
  - Ruso
  - OOD
- Documentación de:
  - arquitectura;
  - model card;
  - evaluación;
  - validación multilingual;
  - controles operativos;
  - deployment.
- Nuevo Notebook 06 para evaluación multilingual de v1.1.
- Etapa 07 para desarrollo, validación, empaquetado y deployment de v1.2.

### Changed

- La arquitectura evoluciona de:

```text
TF-IDF Word
+
TF-IDF Character
      ↓
SGDClassifier
```

a:

```text
TF-IDF Word
+
TF-IDF Character
+
MiniLM Multilingual 384
      ↓
LinearSVC
C = 0.3
```

- El clasificador final cambia de `SGDClassifier` a:

```text
LinearSVC
C = 0.3
```

- El espacio final de entrada del clasificador pasa a:

```text
60,384 características
```

compuesto por:

```text
60,000 TF-IDF
+
384 MiniLM
```

- La validación operacional deja de depender únicamente de cobertura TF-IDF y margen v1.1.

Ahora se aplica:

```text
Input validation
      ↓
Semantic Domain Support
      ↓
Decision Margin
      ↓
accepted / review /
rejected_ood / rejected_invalid
```

- La API v1.2 expone `decision` como autoridad operacional.
- Los scores de `LinearSVC` se documentan explícitamente como **scores de decisión y no probabilidades**.
- Backend debe interpretar:

```text
decision
```

y no recalcular thresholds de dominio o margen.

### Experimental evaluation

Antes de construir el modelo híbrido se evaluó MiniLM como representación independiente.

Resultados aproximados:

| Modelo MiniLM-only | F1 Macro CV |
|---|---:|
| Logistic Regression | 0.7604 |
| LinearSVC | 0.7729 |
| SGDClassifier | 0.7724 |

Conclusión:

> MiniLM aportó representación semántica multilingual, pero por sí solo perdió discriminación sobre vocabulario técnico especializado.

Esto motivó la arquitectura híbrida.

### Hyperparameter selection

Búsqueda controlada de `C` para `LinearSVC`:

| C | F1 Macro CV |
|---:|---:|
| 0.1 | 0.8461 |
| **0.3** | **0.8574** |
| 1.0 | 0.8569 |
| 3.0 | 0.8555 |

Se congeló:

```text
C = 0.3
```

sin microajustes posteriores.

### Metrics — Test original

Resultados sobre el TEST reservado de `917` documentos:

| Métrica | Resultado |
|---|---:|
| Accuracy | 0.8746 |
| Precision Macro | 0.8763 |
| Recall Macro | 0.8749 |
| F1 Macro | 0.8753 |
| F1 Weighted | 0.8749 |
| F1 Macro CV | 0.8574 |
| Diferencia Test-CV | +0.0179 |

### Multilingual development benchmark

Benchmark de desarrollo:

```text
80 documentos
20 casos semánticos
4 idiomas
4 categorías
```

Resultados v1.2:

```text
79 / 80 correctos
Accuracy = 98.75%
Consistencia cross-language = 95%
```

Este benchmark fue utilizado durante desarrollo y no constituye la validación final independiente.

### Final independent multilingual benchmark

Benchmark final:

```text
320 documentos
80 casos semánticos
4 idiomas
4 categorías
```

Resultados:

| Métrica | Resultado |
|---|---:|
| Accuracy | 0.7625 |
| Precision Macro | 0.8167 |
| Recall Macro | 0.7625 |
| F1 Macro | 0.7570 |
| F1 Weighted | 0.7570 |

Resultados por idioma:

| Idioma | Accuracy |
|---|---:|
| Inglés | 0.7750 |
| Español | 0.7500 |
| Español/Inglés | 0.7875 |
| Ruso | 0.7375 |

Resultados por categoría:

| Categoría | Accuracy |
|---|---:|
| Backend | 0.9000 |
| Cloud | 0.4000 |
| Data Science | 0.8375 |
| Frontend | 0.9125 |

Consistencia cross-language:

```text
64 / 80
80%
```

### Comparison v1.1 vs v1.2

Sobre el mismo benchmark multilingual final:

```text
v1.1 Accuracy = 0.5656
v1.2 Accuracy = 0.7625

Δ = +0.1969
≈ +19.69 puntos porcentuales
```

```text
v1.1 F1 Macro = 0.5705
v1.2 F1 Macro = 0.7570

Δ = +0.1864
```

Comparación pareada:

```text
Solo v1.1 correcta = 14
Solo v1.2 correcta = 77
```

Resultado:

```text
p < 0.001
```

### Operational calibration

#### Decision Margin

Calibrado mediante predicciones **Out-of-Fold de 5 folds sobre TRAIN**.

Métrica:

```text
top1_minus_top2_decision_margin
```

Threshold final:

```text
0.8132
```

#### Semantic Domain Support

Detector:

```text
NearestNeighbors
n_neighbors = 5
metric = cosine
algorithm = brute
n_jobs = 1
```

Métrica:

```text
mean_cosine_similarity_5nn
```

Threshold final:

```text
0.4266
```

### Operational metrics

#### Test original

```text
Accepted          618
Review            269
Rejected OOD       30
Coverage         67.39%
Accepted Accuracy 96.60%
Error Capture    81.74%
Accepted Errors      21
```

#### Benchmark multilingual final

```text
Accepted          120
Review            160
Rejected OOD       40
Coverage         37.50%
Accepted Accuracy 91.67%
Error Capture    86.84%
Accepted Errors      10
```

### API

Nueva interfaz:

```text
API version:   1.2.0
Model version: 1.2.0-multilingual
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

La respuesta de inferencia incorpora campos como:

```text
prediction
second_category
decision
decision_margin
domain_similarity_5nn
score_top1
score_top2
reason
```

### Deployment

Imagen:

```text
techmind:v1.2.0-multilingual
```

Base:

```text
python:3.11-slim-bookworm
```

PyTorch:

```text
torch==2.13.0+cpu
```

Runtime configurado para ejecución offline de MiniLM.

El deployment valida:

```text
TORCH_CPU_OK
SHA256
MINILM_BUILD_OK
```

Smoke test certificado:

```text
DOCKER SMOKE TEST PASSED
```

### Model integrity

Artefacto final de deployment:

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256 certificado:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

> Un SHA diferente existió durante una serialización previa de desarrollo. Para deployment debe utilizarse exclusivamente el SHA certificado anterior.

### Known limitations

La principal limitación identificada corresponde a:

```text
cloud ↔ backend
```

En el benchmark multilingual final:

```text
Cloud Accuracy = 0.4000
```

Distribución de los 80 ejemplos `cloud`:

```text
Predicho backend       42
Predicho cloud         32
Predicho datascience    6
```

La limitación se atribuye principalmente a:

- frontera conceptual entre Cloud y Backend;
- cobertura del corpus;
- contenido Cloud con fuerte componente de aplicación/backend.

No debe corregirse mediante reglas manuales como:

```text
AWS → cloud
Docker → cloud
API → backend
```

La mejora queda planteada para una futura versión del modelo.

### Version compatibility

```text
Stable fallback package/model: 1.1.0
v1.2 API interface:            1.2.0
v1.2 model version:            1.2.0-multilingual
v1.2 status:                   validated_experimental_candidate
```

---

## [1.1.0] - 2026-08-07

### Added

- Arquitectura híbrida **TF-IDF Word + TF-IDF Char**.
- Rama de caracteres con `char_wb`.
- N-gramas de caracteres `3–6`.
- Hasta `30,000` features Word.
- Hasta `30,000` features Char.
- `60,000` features totales.
- Normalización Unicode.
- Stopwords españolas controladas.
- Calibración operacional mediante predicciones **Out-of-Fold de 5 folds**.
- Nuevos campos de cobertura:
  - `word_features_activas`
  - `char_features_activas`
  - `features_activas_total`
- Campo `feature_type` en las explicaciones del modelo.
- Información de `model_version` en la API.
- Información de Word, Char y total features en `/health` y `/model-info`.
- Pruebas de regresión para textos técnicos cortos.
- Smoke test independiente del predictor.
- Validación FastAPI para v1.1.0.
- Documentación de migración desde v1.0.0.
- Guía de integración para el equipo de Backend.

### Changed

- El pipeline productivo cambia de:

```text
TF-IDF Word
      ↓
SGDClassifier
```

a:

```text
TF-IDF Word
      +
TF-IDF Char 3-6
      ↓
FeatureUnion
      ↓
SGDClassifier optimizado
```

- La cobertura operacional ahora se calcula como:

```text
features_activas_total =
word_features_activas +
char_features_activas
```

- `terminos_activos` se conserva como alias retrocompatible del total de features activas.
- La API mantiene la interfaz `1.0.0` para preservar compatibilidad con integraciones existentes.

### Fixed

- Clasificación incorrecta de textos técnicos cortos relacionados con:
  - Spring Boot
  - Java
  - API REST
  - controladores
  - servicios
  - repositorios
- Dependencia excesiva de stopwords y correlaciones estilísticas en la representación Word-only.
- Interpretación incorrecta de `word_features_activas = 0` como falta total de cobertura.

### Metrics

Resultados finales de v1.1.0:

| Métrica | Resultado |
|---|---:|
| F1 Macro CV | 0.8493 |
| F1 Macro Test | 0.8441 |
| Accuracy Test | 0.8430 |
| Precision Macro | 0.8455 |
| Recall Macro | 0.8434 |
| F1 Weighted | 0.8435 |
| Diferencia Test-CV | -0.0052 |
| Accuracy predicciones aceptadas | 0.9508 |
| Tasa revisión/rechazo | 26.83% |
| Captura de errores | 77.08% |
| Casos externos correctos | 9/9 |
| Casos externos sin cobertura | 0 |

### Operational calibration

```text
review margin: 0.64346894252355
few features threshold: 178
reject if total features: 0
```

### Model integrity

SHA-256 del artefacto final aprobado:

```text
756b2577e731336ead95852ee1d8d752408762478a23d0bbf42cc9537e136ff6
```

### Version compatibility

```text
Package version: 1.1.0
Model version:   1.1.0
API interface:   1.0.0
```

---

## [1.0.0]

### Added

- Primera versión productiva de TechMind.
- TF-IDF basado en palabras.
- SGDClassifier optimizado.
- Predictor independiente `TechMindPredictor`.
- API REST con FastAPI.
- Endpoints:
  - `/`
  - `/health`
  - `/model-info`
  - `/predict`
  - `/docs`
  - `/redoc`
  - `/openapi.json`
- Explicabilidad lineal.
- Estados operacionales:
  - `aceptada`
  - `revision`
  - `rechazada`
- Pruebas de robustez.
- Monitoring.
- Docker.
- Preparación para deployment.
- Integración con OCI.

### Metrics

Resultados finales de v1.0.0:

| Métrica | Resultado |
|---|---:|
| Accuracy Test | 0.8386 |
| Precision Macro | 0.8445 |
| Recall Macro | 0.8385 |
| F1 Macro | 0.8401 |
| F1 Weighted | 0.8397 |

### Known limitation

La arquitectura Word-only podía presentar cobertura reducida en textos técnicos cortos y depender de correlaciones estilísticas.

Un caso corto relacionado con Spring Boot y API REST fue clasificado como `cloud`, aunque `backend` era la categoría correcta.

Este comportamiento motivó el desarrollo de **TechMind v1.1.0**.
