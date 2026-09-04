# Tests — TechMind v1.2.0-multilingual

Esta carpeta contiene las pruebas de regresión y smoke tests específicos de la versión multilingual de TechMind / IndexMind.

## Estructura

```text
tests/
└── v1.2/
    ├── test_artifact_integrity.py
    ├── test_predictor_v12.py
    ├── test_multilingual_v12.py
    ├── test_operational_controls_v12.py
    ├── test_api_v12.py
    └── README.md
```

Los tests históricos de v1.0/v1.1 se mantienen fuera de esta carpeta.

---

## Cobertura

### `test_artifact_integrity.py`

Valida:

- existencia del `.joblib`;
- SHA-256 del artefacto;
- versión y estado;
- `LinearSVC`;
- `C = 0.3`;
- MiniLM de 384 dimensiones;
- `60,384` características finales;
- clases;
- `domain_reference_embeddings` con forma `(3666, 384)`;
- normalización L2;
- thresholds operativos.

### `test_predictor_v12.py`

Valida:

- carga de `TechMindPredictor`;
- `model_info()`;
- contrato de salida;
- regresión Backend;
- scores finitos;
- top-k;
- explicación diferencial TF-IDF.

### `test_multilingual_v12.py`

Valida regresiones controladas en:

- Español → Backend;
- Inglés → Cloud;
- Ruso → Data Science;
- Español/Inglés → Frontend.

No reemplaza el benchmark final de 320 documentos; funciona como smoke/regression test rápido.

### `test_operational_controls_v12.py`

Valida los cuatro estados:

```text
accepted
review
rejected_ood
rejected_invalid
```

También confirma los thresholds congelados:

```text
Semantic Domain Support = 0.4266
Decision Margin         = 0.8132
```

### `test_api_v12.py`

Valida:

```text
GET  /health
GET  /model-info
POST /predict
GET  /openapi.json
```

y comprueba versión, SHA y contrato OpenAPI.

---

## Requisitos

Ejecutar desde la raíz de:

```text
techmind-v2/
```

Instalar las dependencias de v1.2 y pytest.

Ejemplo:

```bash
python -m pip install -r deploy/v1.2.0-multilingual/requirements-v1.2.txt
python -m pip install pytest
```

---

## MiniLM local

El predictor v1.2 utiliza:

```python
SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    local_files_only=True
)
```

Por ello el modelo MiniLM debe existir previamente en la caché local.

Si todavía no está disponible, realizar una descarga única antes de ejecutar los tests:

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')"
```

Después puede ejecutarse offline.

---

## Ejecutar todos los tests v1.2

Desde `techmind-v2/`:

```bash
python -m pytest tests/v1.2 -v
```

---

## Ejecutar por componente

### Integridad

```bash
python -m pytest tests/v1.2/test_artifact_integrity.py -v
```

### Predictor

```bash
python -m pytest tests/v1.2/test_predictor_v12.py -v
```

### Multilingual

```bash
python -m pytest tests/v1.2/test_multilingual_v12.py -v
```

### Controles operativos

```bash
python -m pytest tests/v1.2/test_operational_controls_v12.py -v
```

### API

```bash
python -m pytest tests/v1.2/test_api_v12.py -v
```

---

## Artefacto esperado

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256 oficial de deployment:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

Este es el SHA vigente y funcionalmente recertificado para deployment.

---

## Nota sobre el SHA histórico

Durante desarrollo existió una serialización anterior con otro SHA.

Los tests de esta carpeta deben validar exclusivamente el artefacto vigente:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

No debe sustituirse el SHA del test por otro valor únicamente para hacer que la prueba pase.

---

## Docker

El smoke test del contenedor permanece separado en:

```text
deploy/v1.2.0-multilingual/docker/
smoke_test_docker.py
```

La división es intencional:

```text
tests/v1.2/
→ modelo, predictor y API Python

deploy/.../docker/
→ contenedor desplegado
```

---

## Estado esperado

Una ejecución correcta debe finalizar sin fallos:

```text
pytest tests/v1.2 -v
================= passed =================
```

Los tests requieren acceso al artefacto v1.2 y a la caché local de MiniLM.
