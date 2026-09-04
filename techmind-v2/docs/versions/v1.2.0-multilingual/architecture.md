# Arquitectura — v1.2.0-multilingual

## Objetivo

La arquitectura de `v1.2.0-multilingual` combina información léxica especializada con representación semántica multilingual para mejorar la clasificación de contenido técnico.

## Flujo general

```text
Texto de entrada
      │
      ├──────────────┐
      │              │
      ▼              ▼
TF-IDF Word     TF-IDF Character
      │              │
      └──────┬───────┘
             │
             ▼
     MiniLM Multilingual
        384 dimensiones
             │
             ▼
     Concatenación híbrida
             │
             ▼
          LinearSVC
           C = 0.3
             │
             ▼
   Semantic Domain Support
             │
             ▼
        Decision Margin
             │
             ▼
      decisión operacional
```

## 1. Representación léxica

### TF-IDF Word

Captura términos técnicos, nombres de frameworks, APIs, conceptos de infraestructura y expresiones especializadas.

### TF-IDF Character

Captura fragmentos de palabras, variantes morfológicas, nombres tecnológicos y patrones útiles entre idiomas.

## 2. Representación semántica

Modelo:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Configuración:

```text
embedding_dimension = 384
normalize_embeddings = True
max_seq_length = 128
```

En el dataset final:

```text
Registros con longitud >128 tokens: 9
Proporción aproximada: 0.20%
```

Por ello no se implementó chunking en v1.2.

## 3. Combinación de características

```text
TF-IDF Word
+ TF-IDF Character
+ MiniLM 384
```

El clasificador recibe:

```text
60,384 características
```

## 4. Clasificador

```text
LinearSVC
C = 0.3
```

Búsqueda controlada:

```text
C = 0.1 → F1 Macro 0.8461
C = 0.3 → F1 Macro 0.8574
C = 1.0 → F1 Macro 0.8569
C = 3.0 → F1 Macro 0.8555
```

Se congeló `C = 0.3`.

## 5. Controles posteriores

### Semantic Domain Support

```text
NearestNeighbors
n_neighbors = 5
metric = cosine
algorithm = brute
n_jobs = 1
threshold = 0.4266
```

### Decision Margin

```text
decision_margin = score_top1 - score_top2
threshold = 0.8132
```

## 6. Estados

```text
accepted
review
rejected_ood
rejected_invalid
```

Regla:

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

## 7. Componentes

```text
techmind_v12/
techmind_api_v12/
deploy/v1.2.0-multilingual/
```

## 8. Principio de diseño

Backend debe usar `decision` como autoridad operacional.

Los valores `score_top1` y `score_top2` son scores de `LinearSVC`, no probabilidades calibradas.
