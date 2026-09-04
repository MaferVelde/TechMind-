# 🧠 TechMind v2 — Ciencia de Datos

> Componente de Machine Learning y NLP de **IndexMind** para clasificación automática y multilingual de contenido técnico.

**Estado actual del modelo:** `v1.2.0-multilingual` — `validated_experimental_candidate`  
**Baseline estable / fallback:** `v1.1.0`

---

## 📌 Resumen

Este directorio contiene el desarrollo completo del componente de **Ciencia de Datos** de IndexMind, desde la preparación del dataset y los primeros modelos TF-IDF hasta la arquitectura híbrida multilingual utilizada en `v1.2.0-multilingual`.

El proyecto clasifica contenido técnico en cuatro categorías:

```text
backend
cloud
datascience
frontend
```

La evolución del modelo fue:

```text
v1.0.0
TF-IDF Word + SGDClassifier
        ↓
v1.1.0
TF-IDF Word + Character + SGDClassifier
        ↓
Notebook 06
Evaluación multilingual de v1.1
        ↓
v1.2.0-multilingual
TF-IDF Word + Character
+ MiniLM Multilingual 384
+ LinearSVC C=0.3
```

---

# 🎯 Objetivo del componente

El objetivo de Ciencia de Datos es recibir texto técnico y producir una clasificación estructurada que pueda ser consumida por el Backend de IndexMind.

Además de la categoría predicha, `v1.2` incorpora controles operativos para determinar si una respuesta debe:

```text
accepted
review
rejected_ood
rejected_invalid
```

Esto permite distinguir entre:

- una predicción suficientemente confiable;
- una predicción ambigua;
- contenido con bajo soporte dentro del dominio;
- una entrada inválida.

---

# 🗂️ Dataset

Dataset original:

```text
5,000 registros
1,250 registros por clase
```

Después de validación, resolución de conflictos y eliminación de duplicados:

```text
4,583 registros finales
```

Procesamiento relevante:

```text
27 grupos conflictivos detectados
78 filas involucradas
339 duplicados eliminados
```

Balance final:

```text
ratio ≈ 0.946
```

Split de modelado:

```text
Train = 3,666
Test  = 917
```

Split:

```text
stratified
random_state = 42
```

---

# 🏷️ Categorías

| Categoría | Ejemplos de contenido |
|---|---|
| `backend` | APIs, Java, Spring Boot, autenticación, servicios |
| `cloud` | AWS, OCI, Azure, Kubernetes, infraestructura |
| `datascience` | Python, ML, IA, NLP, Pandas, modelos |
| `frontend` | HTML, CSS, JavaScript, React, UI |

---

# 📂 Estructura principal

```text
techmind-v2/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── evaluation/
│       ├── multilingual_benchmark.csv
│       └── multilingual_final_benchmark_v1.csv
│
├── notebooks/
│   ├── 01_eda_preparacion_datos.ipynb
│   ├── 02_variantes_textuales_splits.ipynb
│   ├── 03_modelado_seleccion.ipynb
│   ├── 04_evaluacion_explicabilidad_empaquetado.ipynb
│   ├── 05_modelo_v1.1.0.ipynb
│   ├── 06_evaluacion_multilingue.ipynb
│   └── v1.2.0-multilingual/
│
├── models/
│   ├── v1.0.0/
│   ├── v1.1.0/
│   └── experimental/
│       └── v1.2.0-multilingual/
│           └── techmind_hybrid_v1_2_0_multilingual.joblib
│
├── techmind/
│   └── predictor.py
│
├── techmind_v12/
│   ├── __init__.py
│   └── predictor.py
│
├── techmind_api/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── techmind_api_v12/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── docs/
│   └── versions/
│       ├── v1.0.0/
│       ├── v1.1.0/
│       └── v1.2.0-multilingual/
│
├── reports/
│
├── deploy/
│   └── v1.2.0-multilingual/
│       ├── README.md
│       ├── ARTIFACT_CERTIFICATION.md
│       ├── requirements-v1.2.txt
│       ├── smoke_test_v12.py
│       ├── start_server.py
│       └── docker/
│           ├── Dockerfile
│           ├── Dockerfile.dockerignore
│           ├── compose.yaml
│           └── smoke_test_docker.py
│
└── tests/
```

> Algunas rutas de v1.2 deben agregarse al repositorio si todavía no han sido publicadas.

---

# 📓 Notebooks

## 01 — EDA y preparación de datos

```text
01_eda_preparacion_datos.ipynb
```

Incluye:

- análisis exploratorio;
- distribución de clases;
- limpieza y normalización;
- resolución de conflictos;
- análisis de duplicados;
- ingeniería de características;
- validaciones de calidad.

Resultado final:

```text
4,583 registros válidos
21 características numéricas generadas
0 duplicados
0 contradicciones
0 nulos críticos
```

---

## 02 — Variantes textuales y splits

```text
02_variantes_textuales_splits.ipynb
```

Construye y compara:

```text
texto_modelo_base
texto_modelo_titulo
texto_combinado
texto_combinado_ponderado
```

También genera el split reproducible Train/Test.

---

## 03 — Modelado y selección

```text
03_modelado_seleccion.ipynb
```

Compara:

- Logistic Regression;
- LinearSVC;
- SGDClassifier;
- diferentes variantes textuales;
- configuración híbrida con características numéricas.

Entre los resultados obtenidos durante el proceso:

```text
TF-IDF + LinearSVC
F1 Macro CV ≈ 0.8357
```

y:

```text
TF-IDF + SGDClassifier optimizado
F1 Macro CV ≈ 0.8432
```

---

## 04 — Evaluación, explicabilidad y empaquetado

```text
04_evaluacion_explicabilidad_empaquetado.ipynb
```

Incluye:

- evaluación final de v1.0;
- matriz de confusión;
- métricas por clase;
- explicabilidad;
- serialización;
- construcción de predictor;
- pruebas independientes de carga e inferencia.

---

## 05 — Modelo v1.1.0

```text
05_modelo_v1.1.0.ipynb
```

Surge del análisis de limitaciones de v1.0 en textos técnicos cortos.

v1.1 incorpora:

```text
TF-IDF Word
+
TF-IDF Character
```

con:

```text
≈ 60,000 características
```

Objetivos principales:

- mejorar cobertura;
- capturar nombres tecnológicos;
- reducir sensibilidad a vocabulario exacto;
- mejorar robustez en entradas breves;
- conservar compatibilidad con el predictor existente.

`v1.1.0` permanece como:

```text
stable baseline / fallback
```

---

## 06 — Evaluación Multilingüe de v1.1

```text
06_evaluacion_multilingue.ipynb
```

Evalúa si `v1.1.0` podía generalizar a diferentes idiomas antes de desarrollar un modelo semántico multilingual.

Benchmark:

```text
80 documentos
20 casos semánticos
4 idiomas
4 categorías
```

Idiomas:

```text
ES
EN
RU
ES-EN
```

Resultados:

```text
Correctas                69 / 80
Accuracy global          86.25%
Consistencia cross-lang  65.00%
Captura de errores       100.00%
```

Por idioma:

| Idioma | Accuracy |
|---|---:|
| Inglés | 95% |
| Español | 75% |
| Español/Inglés | 95% |
| Ruso | 80% |

Hallazgos:

- v1.1 mostró cierta generalización multilingual;
- los char n-grams ayudaron especialmente en idiomas con menor cobertura léxica;
- ruso tuvo buen número de aciertos, pero baja confianza operacional;
- `datascience`, `cloud` y algunos casos `frontend` mostraron sensibilidad lingüística;
- la consistencia entre traducciones equivalentes fue solo 65%.

Conclusión:

```text
TF-IDF Word + Character
no era suficiente para representar
semántica multilingual de forma robusta.
```

Esta evidencia motivó directamente `v1.2.0-multilingual`.

---

# 🔄 Evolución de modelos

## v1.0.0 — Baseline productivo

Arquitectura:

```text
TF-IDF Word
+
SGDClassifier optimizado
```

Resultados:

| Métrica | Resultado |
|---|---:|
| Accuracy Test | 0.8386 |
| Precision Macro | 0.8445 |
| Recall Macro | 0.8385 |
| F1 Macro | 0.8401 |
| F1 Weighted | 0.8397 |

Artefacto histórico:

```text
models/techmind_modelo_final.joblib
```

SHA-256 histórico:

```text
488ec7d47f7697f870fde6877d8df54e5ce1fedbc29842dd669a1014c7715cfb
```

---

## v1.1.0 — Word + Character

Arquitectura:

```text
TF-IDF Word
+
TF-IDF Character
+
SGDClassifier
```

Objetivo:

```text
mejor cobertura léxica
+
mayor robustez técnica
```

Artefacto:

```text
models/v1.1.0/
techmind_modelo_final_v1_1_0.joblib
```

SHA-256:

```text
756b2577e731336ead95852ee1d8d752408762478a23d0bbf42cc9537e136ff6
```

Estado:

```text
stable baseline / fallback
```

---

## v1.2.0-multilingual — Modelo actual

Estado:

```text
validated_experimental_candidate
```

Arquitectura:

```text
TF-IDF Word
+
TF-IDF Character
+
MiniLM Multilingual 384
        ↓
    LinearSVC
      C=0.3
```

Modelo de embeddings:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Dimensión:

```text
384
```

Espacio total del clasificador:

```text
60,384 características
```

---

# 🧪 Selección de arquitectura v1.2

Antes del modelo híbrido se probó MiniLM como representación independiente.

Resultados aproximados:

```text
Logistic Regression  F1 ≈ 0.7604
LinearSVC            F1 ≈ 0.7729
SGD hinge            F1 ≈ 0.7724
```

Conclusión:

```text
MiniLM aporta representación semántica,
pero por sí solo pierde discriminación
sobre vocabulario técnico especializado.
```

Por ello se combinó con TF-IDF.

---

## Búsqueda de C

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

---

# 📊 Evaluación v1.2

## Test original

```text
n = 917
```

| Métrica | Resultado |
|---|---:|
| Accuracy | **0.8746** |
| Precision Macro | **0.8763** |
| Recall Macro | **0.8749** |
| F1 Macro | **0.8753** |
| F1 Weighted | **0.8749** |

Validación cruzada:

```text
F1 Macro CV = 0.8574
```

---

# 🌍 Benchmark multilingual final independiente

Archivo:

```text
data/evaluation/multilingual_final_benchmark_v1.csv
```

Diseño:

```text
80 casos semánticos
× 4 idiomas
= 320 documentos
```

Distribución:

```text
80 por idioma
80 por categoría
```

El benchmark se utilizó únicamente como evaluación final después de congelar arquitectura, `C` y thresholds.

Resultados:

```text
244 / 320 correctos
```

| Métrica | Resultado |
|---|---:|
| Accuracy | **0.7625** |
| Precision Macro | **0.8167** |
| Recall Macro | **0.7625** |
| F1 Macro | **0.7570** |
| F1 Weighted | **0.7570** |

---

## Por idioma

| Idioma | Accuracy |
|---|---:|
| Inglés | **0.7750** |
| Español | **0.7500** |
| Español/Inglés | **0.7875** |
| Ruso | **0.7375** |

---

## Por categoría

| Categoría | Accuracy |
|---|---:|
| Backend | **0.9000** |
| Cloud | **0.4000** |
| Data Science | **0.8375** |
| Frontend | **0.9125** |

Consistencia cross-language:

```text
64 / 80
80%
```

---

# 📈 Comparación multilingual v1.1 vs v1.2

Sobre el mismo benchmark final de 320 documentos:

| Modelo | Accuracy | F1 Macro |
|---|---:|---:|
| v1.1 | 0.5656 | 0.5705 |
| v1.2 | **0.7625** | **0.7570** |

Mejora absoluta:

```text
Accuracy +0.1969
≈ +19.69 puntos porcentuales
```

```text
F1 Macro +0.1864
```

---

# 🛡️ Controles operativos v1.2

## Semantic Domain Support

Se utiliza:

```text
NearestNeighbors
n_neighbors = 5
metric = cosine
algorithm = brute
n_jobs = 1
```

Métrica:

```text
domain_similarity_5nn
```

Threshold congelado:

```text
0.4266
```

---

## Decision Margin

```text
decision_margin =
score_top1 - score_top2
```

Threshold:

```text
0.8132
```

---

## Regla operacional

```text
Entrada válida?
  ├── No → rejected_invalid
  └── Sí
       ↓
domain_similarity_5nn >= 0.4266?
  ├── No → rejected_ood
  └── Sí
       ↓
decision_margin >= 0.8132?
  ├── No → review
  └── Sí → accepted
```

---

# 🚦 Rendimiento operacional

## Test original

```text
Accepted       618
Review         269
Rejected OOD    30
Coverage        67.39%
Accepted Accuracy 96.60%
Error Capture   81.74%
Accepted Errors 21
```

## Benchmark multilingual final

```text
Accepted       120
Review         160
Rejected OOD    40
Coverage        37.50%
Accepted Accuracy 91.67%
Error Capture   86.84%
Accepted Errors 10
```

---

# ⚠️ Limitación conocida — Cloud ↔ Backend

La principal debilidad del benchmark final fue:

```text
cloud
```

Accuracy:

```text
0.4000
```

Distribución para los 80 casos Cloud:

```text
Predicho backend      42
Predicho cloud        32
Predicho datascience   6
```

La principal confusión es:

```text
cloud → backend
```

No se deben añadir reglas manuales como:

```text
AWS → cloud
Docker → cloud
API → backend
```

La solución debe abordarse en una futura versión mediante:

- nuevo corpus;
- mejores ejemplos de frontera;
- reentrenamiento;
- nuevo benchmark independiente.

---

# 📦 Artefactos

## v1.0

```text
models/techmind_modelo_final.joblib
```

SHA:

```text
488ec7d47f7697f870fde6877d8df54e5ce1fedbc29842dd669a1014c7715cfb
```

## v1.1

```text
models/v1.1.0/
techmind_modelo_final_v1_1_0.joblib
```

SHA:

```text
756b2577e731336ead95852ee1d8d752408762478a23d0bbf42cc9537e136ff6
```

## v1.2

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256 certificado de deployment:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

> Un SHA anterior de otra serialización existió durante desarrollo. Para deployment debe utilizarse exclusivamente el SHA certificado anterior.

---

# 🔍 Predictor v1.2

Paquete:

```text
techmind_v12/
```

Clase:

```python
TechMindPredictor
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

El predictor implementa:

- validación de entrada;
- embeddings MiniLM;
- representación TF-IDF;
- clasificación LinearSVC;
- cálculo de margen;
- 5-NN semántico;
- decisión operacional;
- top-k opcional;
- explicación TF-IDF opcional.

---

# ⚠️ Scores ≠ probabilidades

`LinearSVC` produce scores de decisión.

Por ello:

```text
score_top1
score_top2
```

no deben interpretarse ni presentarse como probabilidades.

Ejemplo:

```text
score_top1 = 1.58
```

no significa:

```text
158% de confianza
```

La autoridad operacional es:

```text
decision
```

---

# 🔎 Explicabilidad

Puede solicitarse mediante:

```json
{
  "include_explanation": true,
  "explanation_top_n": 8
}
```

La explicación disponible se concentra en contribuciones diferenciales de las características TF-IDF.

No representa una explicación completa del embedding MiniLM.

---

# 🌐 API del modelo v1.2

Paquete:

```text
techmind_api_v12/
```

Versiones:

```text
API   = 1.2.0
Model = 1.2.0-multilingual
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

---

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

---

## Model Info

```http
GET /model-info
```

Permite verificar:

```text
model_version
status
classifier
classifier_C
embedding_model
embedding_dimension
classes
domain_control
confidence_control
artifact_sha256
scores_are_probabilities
```

---

# 🐳 Deployment

Paquete:

```text
deploy/v1.2.0-multilingual/
```

Stack del contenedor:

```text
Python 3.11
FastAPI
Uvicorn
Scikit-Learn
Sentence Transformers
PyTorch CPU
Joblib
NumPy
SciPy
```

PyTorch:

```text
torch==2.13.0+cpu
```

Imagen:

```text
techmind:v1.2.0-multilingual
```

El modelo MiniLM se incorpora durante el build para permitir runtime offline.

---

# ⚡ Quick Start — Docker

Desde la raíz del proyecto:

## 1. Verificar artefacto

Linux:

```bash
sha256sum models/experimental/v1.2.0-multilingual/techmind_hybrid_v1_2_0_multilingual.joblib
```

PowerShell:

```powershell
Get-FileHash `
  ".\models\experimental\v1.2.0-multilingual\techmind_hybrid_v1_2_0_multilingual.joblib" `
  -Algorithm SHA256
```

Debe ser:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

## 2. Construir imagen

```bash
docker build \
  --progress=plain \
  -f deploy/v1.2.0-multilingual/docker/Dockerfile \
  -t techmind:v1.2.0-multilingual \
  .
```

## 3. Levantar contenedor

```bash
docker compose \
  -f deploy/v1.2.0-multilingual/docker/compose.yaml \
  up -d
```

## 4. Verificar estado

```bash
docker inspect techmind-v12 \
  --format '{{.State.Status}} / {{.State.Health.Status}}'
```

Esperado:

```text
running / healthy
```

## 5. Smoke test

```bash
python deploy/v1.2.0-multilingual/docker/smoke_test_docker.py
```

Debe finalizar con:

```text
DOCKER SMOKE TEST PASSED
```

---

# ✅ Smoke Test certificado

El smoke test valida:

```text
/health
/model-info
SHA-256
/predict
English
Español
Русский
OOD
```

---

# 📚 Documentación v1.2

```text
docs/versions/v1.2.0-multilingual/
├── README.md
├── architecture.md
├── model_card.md
├── evaluation.md
├── multilingual_validation.md
├── operational_controls.md
└── deployment.md
```

Cada documento tiene una función específica:

| Archivo | Contenido |
|---|---|
| `README.md` | Resumen de la versión |
| `architecture.md` | Arquitectura híbrida |
| `model_card.md` | Model Card |
| `evaluation.md` | Métricas y comparación |
| `multilingual_validation.md` | Benchmarks multilingual |
| `operational_controls.md` | Margin + Domain Support |
| `deployment.md` | Docker, API y despliegue |

---

# 🔄 Versionado

| Versión | Arquitectura | Rol |
|---|---|---|
| `v1.0.0` | TF-IDF Word + SGD | Histórico |
| `v1.1.0` | TF-IDF Word+Char + SGD | **Stable baseline / fallback** |
| `v1.2.0-multilingual` | TF-IDF Word+Char + MiniLM + LinearSVC | **Validated experimental candidate** |

---

# 🧭 Roadmap de Ciencia de Datos

## v1.3 — candidato futuro

Prioridades:

- mejorar frontera `cloud ↔ backend`;
- ampliar corpus multilingual;
- incorporar ejemplos técnicos underrepresented;
- crear un nuevo holdout independiente;
- evaluar calibración adicional;
- mejorar explicabilidad híbrida;
- ampliar pruebas automatizadas;
- integrar CI/CD del modelo.

---

# ✅ Estado actual

| Componente | Estado |
|---|---|
| Preparación de datos | ✅ |
| EDA | ✅ |
| Splits reproducibles | ✅ |
| v1.0 | ✅ |
| v1.1 | ✅ |
| Evaluación multilingual v1.1 | ✅ |
| MiniLM multilingual | ✅ |
| Modelo híbrido v1.2 | ✅ |
| LinearSVC C=0.3 | ✅ |
| Semantic Domain Support | ✅ |
| Decision Margin | ✅ |
| Benchmark final independiente | ✅ |
| Predictor v1.2 | ✅ |
| FastAPI v1.2 | ✅ |
| Artefacto certificado | ✅ |
| Docker CPU-only | ✅ |
| Smoke Test Docker | ✅ |
| Documentación v1.2 | ✅ |

---

# 📌 Resumen técnico

```text
Proyecto:
IndexMind / TechMind

Componente:
Ciencia de Datos

Taxonomía:
backend
cloud
datascience
frontend

Historia:
v1.0 → v1.1 → v1.2 multilingual

Stable fallback:
v1.1.0

Modelo actual:
v1.2.0-multilingual

Estado:
validated_experimental_candidate

Arquitectura:
TF-IDF Word
+ TF-IDF Character
+ MiniLM 384
+ LinearSVC C=0.3

Controles:
Domain Support 5NN = 0.4266
Decision Margin = 0.8132

Idiomas evaluados:
ES / EN / RU / ES-EN

SHA-256 deployment:
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

---

## 🔗 Proyecto completo

Repositorio principal:

```text
https://github.com/MaferVelde/TechMind-
```

Sitio:

```text
https://indexmind.tech/
```

