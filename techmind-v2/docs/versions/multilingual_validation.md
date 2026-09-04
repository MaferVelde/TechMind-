# Validación Multilingual — v1.2.0-multilingual

## Objetivo

Evaluar la clasificación de contenido técnico multilingual bajo una taxonomía común.

Idiomas:

```text
es
en
ru
es_en
```

## 1. Benchmark multilingual de desarrollo

Archivo:

```text
data/evaluation/multilingual_benchmark.csv
```

Diseño:

```text
80 documentos
20 casos semánticos × 4 idiomas
20 documentos por idioma
20 documentos por categoría
```

Origen:

```text
synthetic_controlled
```

Este benchmark fue utilizado durante desarrollo y no debe considerarse validación final independiente.

## Resultados v1.1

```text
69 / 80
86.25%
```

Por idioma:

```text
EN    95%
ES    75%
ES-EN 95%
RU    80%
```

Consistencia cross-language:

```text
13 / 20
65%
```

## Resultados v1.2

```text
79 / 80
98.75%
```

Por idioma:

```text
EN    100%
ES    100%
ES-EN 100%
RU     95%
```

Consistencia cross-language:

```text
19 / 20
95%
```

Errores:

```text
v1.1 = 11
v1.2 = 1
```

## 2. Benchmark multilingual final independiente

Archivo:

```text
data/evaluation/multilingual_final_benchmark_v1.csv
```

SHA-256:

```text
5d994e36a49b362fa4277656e7c4254bfb7fa9bab00db3b9f194228c115e13f8
```

Origen:

```text
synthetic_controlled_independent
```

Rol:

```text
final_independent_evaluation
```

Diseño:

```text
80 casos semánticos × 4 idiomas = 320 documentos
```

Distribución:

```text
80 por idioma
80 por categoría
```

## Resultados globales

```text
244 / 320 correctos
Accuracy        0.7625
Precision Macro 0.8167
Recall Macro    0.7625
F1 Macro        0.7570
F1 Weighted     0.7570
```

## Resultados por idioma

| Idioma | Correctos | Accuracy |
|---|---:|---:|
| EN | 62 / 80 | 0.7750 |
| ES | 60 / 80 | 0.7500 |
| ES-EN | 63 / 80 | 0.7875 |
| RU | 59 / 80 | 0.7375 |

## Resultados por categoría

| Categoría | Correctos | Accuracy |
|---|---:|---:|
| Backend | 72 / 80 | 0.9000 |
| Cloud | 32 / 80 | 0.4000 |
| Data Science | 67 / 80 | 0.8375 |
| Frontend | 73 / 80 | 0.9125 |

## Consistencia cross-language

```text
64 / 80
80%
```

## Resultado operacional

```text
Accepted      120
Review        160
Rejected OOD   40
Coverage       37.50%
Accepted Accuracy 91.67%
Error Capture  86.84%
Accepted Errors 10
```

## Observación

El benchmark de desarrollo obtuvo:

```text
98.75%
```

El benchmark final independiente obtuvo:

```text
76.25%
```

La diferencia confirma que el benchmark final fue considerablemente más exigente.

El resultado que debe comunicarse como evaluación final es el benchmark independiente.

## Limitación principal

La debilidad dominante fue:

```text
cloud ↔ backend
```

Varias familias Cloud fallaron en los cuatro idiomas, lo que sugiere un problema principalmente conceptual/corpus y no exclusivamente lingüístico.
