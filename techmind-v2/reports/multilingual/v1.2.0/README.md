# Reports — TechMind / IndexMind v1.2.0-multilingual

Esta carpeta contiene los reportes finales consolidados de la versión multilingual `v1.2.0-multilingual`.

Estado del modelo:

```text
validated_experimental_candidate
```

Baseline estable / fallback:

```text
v1.1.0
```

---

## Archivos

### `final_benchmark.json`

Resultados del benchmark multilingual final independiente:

```text
320 documentos
80 casos semánticos
4 idiomas
4 categorías
```

El benchmark fue utilizado únicamente para evaluación final después de congelar arquitectura, `C` y thresholds.

### `v1_1_vs_v1_2.json`

Comparación directa entre v1.1 y v1.2 sobre los mismos 320 documentos.

### `operational_calibration.json`

Resultados del control operacional combinado:

```text
Semantic Domain Support
+
Decision Margin
```

### `domain_support_calibration.json`

Calibración y parámetros del detector semántico basado en 5-NN y similitud coseno.

### `cloud_error_analysis.md`

Análisis de la principal limitación conocida:

```text
cloud ↔ backend
```

### `latency_report.json`

Resultados de latencia, throughput y tiempo de carga del predictor.

---

## Modelo

Arquitectura:

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

Modelo de embeddings:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

---

## Controles operativos

### Semantic Domain Support

```text
metric = mean_cosine_similarity_5nn
n_neighbors = 5
threshold = 0.4266
```

### Decision Margin

```text
metric = top1_minus_top2_decision_margin
threshold = 0.8132
```

Estados:

```text
accepted
review
rejected_ood
rejected_invalid
```

---

## Artefacto

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256 certificado de deployment:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

---

## Nota metodológica

Los reportes de esta carpeta corresponden al estado final congelado de v1.2.

No deben utilizarse para reoptimizar retrospectivamente:

- arquitectura;
- `C`;
- threshold OOD;
- threshold de Decision Margin.

Cualquier modificación futura debe realizarse bajo una nueva versión y con un nuevo holdout independiente.
