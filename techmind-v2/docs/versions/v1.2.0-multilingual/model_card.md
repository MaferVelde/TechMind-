# Model Card — TechMind / IndexMind v1.2.0-multilingual

## Identificación

**Nombre**

```text
TechMind / IndexMind v1.2.0-multilingual
```

**Estado**

```text
validated_experimental_candidate
```

**Tarea**

```text
Clasificación multicategoría de contenido técnico
```

## Categorías

```text
backend
cloud
datascience
frontend
```

## Idiomas evaluados

```text
es
en
ru
es_en
```

## Arquitectura

```text
TF-IDF Word
+ TF-IDF Character
+ MiniLM Multilingual 384
+ LinearSVC C=0.3
```

Modelo semántico:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

## Dataset

Original:

```text
5,000 registros
1,250 por clase
```

Después de limpieza:

```text
4,583 registros
```

Procesos relevantes:

```text
27 grupos conflictivos
78 filas involucradas
339 duplicados eliminados
```

Split final:

```text
Train = 3,666
Test  = 917
```

## Métricas del test original

```text
Accuracy        0.8746
Precision Macro 0.8763
Recall Macro    0.8749
F1 Macro        0.8753
F1 Weighted     0.8749
```

## Benchmark multilingual final independiente

```text
320 documentos
80 casos semánticos
4 idiomas
4 categorías
```

Resultados:

```text
Accuracy        0.7625
Precision Macro 0.8167
Recall Macro    0.7625
F1 Macro        0.7570
F1 Weighted     0.7570
```

## Rendimiento por idioma

| Idioma | Accuracy |
|---|---:|
| Inglés | 0.7750 |
| Español | 0.7500 |
| Español/Inglés | 0.7875 |
| Ruso | 0.7375 |

## Rendimiento por categoría

| Categoría | Accuracy |
|---|---:|
| Backend | 0.9000 |
| Cloud | 0.4000 |
| Data Science | 0.8375 |
| Frontend | 0.9125 |

## Comparación con v1.1

```text
v1.1 Accuracy = 0.5656
v1.2 Accuracy = 0.7625
Δ = +0.1969
```

```text
v1.1 F1 Macro = 0.5705
v1.2 F1 Macro = 0.7570
Δ = +0.1864
```

## Controles operativos

```text
Domain Support threshold = 0.4266
Decision Margin threshold = 0.8132
```

## Estados

```text
accepted
review
rejected_ood
rejected_invalid
```

## Rendimiento operacional final

```text
Accepted         120
Review           160
Rejected OOD      40
Coverage         37.50%
Accepted Accuracy 91.67%
Error Capture    86.84%
Accepted Errors  10
```

## Limitaciones conocidas

La principal debilidad es la frontera:

```text
cloud ↔ backend
```

Cloud Accuracy:

```text
0.4000
```

No se recomienda corregir esta limitación con reglas manuales por palabras clave.

## Uso previsto

- clasificación de contenido técnico;
- organización de recursos;
- indexación de conocimiento;
- clasificación multilingual;
- soporte a repositorios técnicos.

## Uso no previsto

No debe utilizarse como:

- sistema de decisión de alto riesgo;
- clasificador universal;
- predictor probabilístico;
- sustituto de revisión humana en casos ambiguos.

## Scores

`score_top1` y `score_top2` son scores de decisión de `LinearSVC`.

**No son probabilidades.**

## Artefacto

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```
