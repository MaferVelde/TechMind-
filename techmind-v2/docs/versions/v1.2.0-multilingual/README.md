# TechMind / IndexMind v1.2.0-multilingual

## Resumen

`v1.2.0-multilingual` es la evolución multilingual del modelo de clasificación técnica de **IndexMind**.

Clasifica contenido técnico en cuatro categorías:

- `backend`
- `cloud`
- `datascience`
- `frontend`

Idiomas evaluados:

- Español (`es`)
- Inglés (`en`)
- Ruso (`ru`)
- Español + Inglés (`es_en`)

## Estado

```text
validated_experimental_candidate
```

`v1.1.0` se conserva como baseline estable y fallback.

## Arquitectura

```text
TF-IDF Word + TF-IDF Character
+ MiniLM Multilingual (384)
+ LinearSVC C=0.3
```

Dimensionalidad total:

```text
60,384 características
```

## Artefacto

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256 de deployment:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

## Resultados principales

### Test original

```text
n = 917
Accuracy        0.8746
Precision Macro 0.8763
Recall Macro    0.8749
F1 Macro        0.8753
F1 Weighted     0.8749
```

### Benchmark multilingual final independiente

```text
n = 320
Accuracy        0.7625
Precision Macro 0.8167
Recall Macro    0.7625
F1 Macro        0.7570
F1 Weighted     0.7570
```

### Comparación v1.1 vs v1.2

```text
v1.1 Accuracy = 0.5656
v1.2 Accuracy = 0.7625

Δ = +0.1969
≈ +19.69 puntos porcentuales
```

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

## Documentación

- [Arquitectura](architecture.md)
- [Model Card](model_card.md)
- [Evaluación](evaluation.md)
- [Validación multilingual](multilingual_validation.md)
- [Controles operativos](operational_controls.md)
- [Deployment](deployment.md)

## Limitación principal conocida

La principal debilidad identificada corresponde a la frontera:

```text
cloud ↔ backend
```

En el benchmark multilingual final:

```text
Cloud Accuracy = 0.4000
```

Esta limitación debe abordarse en una futura versión del modelo y no mediante reglas manuales en Backend.
