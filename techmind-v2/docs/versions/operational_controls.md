# Controles Operativos — v1.2.0-multilingual

## Objetivo

v1.2 incorpora dos controles para no tratar todas las predicciones como igualmente confiables:

1. soporte semántico del dominio;
2. margen de decisión.

# 1. Decision Margin

```text
decision_margin = score_top1 - score_top2
```

Métrica:

```text
top1_minus_top2_decision_margin
```

## Calibración

Se utilizaron predicciones OOF de 5 folds sobre TRAIN.

```text
OOF Accuracy = 0.8565
OOF F1 Macro = 0.8573
```

Distribución aproximada:

```text
Correctos:
mean margin   ≈ 1.4275
median margin ≈ 1.3756

Incorrectos:
mean margin   ≈ 0.4019
median margin ≈ 0.2968
```

Thresholds evaluados:

```text
Target 95% → 0.5327
Target 97% → 0.8132
Target 98% → 0.9837
```

Threshold congelado:

```text
0.8132
```

# 2. Semantic Domain Support

MiniLM produce embeddings densos incluso para textos fuera del dominio, por lo que se implementó:

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

## Distribución in-domain

Sobre TEST:

```text
mean   ≈ 0.6073
median ≈ 0.5624
p5     ≈ 0.4381
p1     ≈ 0.3950
min    ≈ 0.3489
```

## Challenge OOD

Se construyeron 120 ejemplos sintéticos fuera del dominio:

```text
10 dominios × 4 idiomas × 3 ejemplos
```

Dominios:

```text
cocina
deportes
viajes
historia
musica
literatura
salud_general
vida_cotidiana
jardineria
cine
```

Distribución OOD:

```text
mean   ≈ 0.2994
median ≈ 0.2921
p95    ≈ 0.4030
p99    ≈ 0.4214
max    ≈ 0.4263
```

Threshold congelado:

```text
0.4266
```

# 3. Regla operacional

```text
input válido?
  ├── no → rejected_invalid
  └── sí
       ↓
domain_similarity_5nn >= 0.4266?
  ├── no → rejected_ood
  └── sí
       ↓
decision_margin >= 0.8132?
  ├── no → review
  └── sí → accepted
```

# 4. Estados

## `accepted`

La predicción puede tratarse como clasificación válida.

## `review`

La predicción puede conservarse como provisional, pero debe marcarse para revisión.

## `rejected_ood`

La entrada tiene bajo soporte semántico dentro del dominio técnico de referencia.

## `rejected_invalid`

La entrada no cumple los requisitos mínimos de validez.

# 5. Rendimiento operacional

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

# 6. Nota sobre OOD

`rejected_ood` puede indicar:

- contenido realmente fuera del dominio;
- contenido técnico válido pero poco representado;
- vocabulario novedoso;
- baja cobertura semántica.

Conceptualmente también puede entenderse como:

```text
domain_support_detector
```

o:

```text
semantic_coverage_detector
```

# 7. Backend

Backend no debe recalcular los thresholds `0.4266` ni `0.8132`.

Debe utilizar directamente:

```text
decision
```
