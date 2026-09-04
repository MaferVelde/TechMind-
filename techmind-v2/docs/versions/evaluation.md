# Evaluación — v1.2.0-multilingual

## Objetivo

Este documento resume la evaluación cuantitativa de la versión multilingual final.

Se distinguen:

1. validación cruzada sobre Train;
2. test original de 917 documentos;
3. benchmark multilingual final independiente de 320 documentos.

## 1. Validación cruzada

Arquitectura:

```text
TF-IDF Word + Character
+ MiniLM 384
+ LinearSVC C=0.3
```

Resultado:

```text
F1 Macro CV = 0.8574
std ≈ 0.0150
```

## 2. Test original

```text
n = 917
```

| Métrica | Resultado |
|---|---:|
| Accuracy | 0.8746 |
| Precision Macro | 0.8763 |
| Recall Macro | 0.8749 |
| F1 Macro | 0.8753 |
| F1 Weighted | 0.8749 |

```text
Test - CV ≈ +0.0179
```

## 3. Benchmark multilingual final independiente

Se construyó después de congelar:

- arquitectura;
- `C = 0.3`;
- threshold OOD `0.4266`;
- threshold margin `0.8132`.

No se utilizó para retuning posterior.

### Diseño

```text
320 documentos
80 casos semánticos
4 idiomas
4 categorías
```

Distribución:

```text
80 documentos por idioma
80 documentos por categoría
```

## Resultados globales

```text
Correctos = 244 / 320
```

| Métrica | Resultado |
|---|---:|
| Accuracy | 0.7625 |
| Precision Macro | 0.8167 |
| Recall Macro | 0.7625 |
| F1 Macro | 0.7570 |
| F1 Weighted | 0.7570 |

## Resultados por idioma

| Idioma | Accuracy | Precision Macro | Recall Macro | F1 Macro |
|---|---:|---:|---:|---:|
| EN | 0.7750 | 0.8262 | 0.7750 | 0.7718 |
| ES | 0.7500 | 0.7933 | 0.7500 | 0.7398 |
| ES-EN | 0.7875 | 0.8416 | 0.7875 | 0.7892 |
| RU | 0.7375 | 0.8034 | 0.7375 | 0.7235 |

## Resultados por categoría

| Categoría | Accuracy |
|---|---:|
| Backend | 0.9000 |
| Cloud | 0.4000 |
| Data Science | 0.8375 |
| Frontend | 0.9125 |

## Consistencia cross-language

```text
64 / 80 casos semánticos
80%
```

## Comparación v1.1 vs v1.2

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

### Por idioma

| Idioma | v1.1 Accuracy | v1.2 Accuracy | Δ |
|---|---:|---:|---:|
| EN | 0.6500 | 0.7750 | +0.1250 |
| ES | 0.5125 | 0.7500 | +0.2375 |
| ES-EN | 0.7000 | 0.7875 | +0.0875 |
| RU | 0.4000 | 0.7375 | +0.3375 |

## Test pareado

```text
Ambos correctos      167
Solo v1.1 correcto    14
Solo v1.2 correcto    77
Ambos incorrectos     62
```

Casos discordantes:

```text
91
```

v1.2 gana:

```text
77 vs 14
```

Resultado:

```text
p < 0.001
```

## Diagnóstico Cloud

Entre los 80 ejemplos `cloud`:

```text
Predicho backend      42
Predicho cloud        32
Predicho datascience   6
```

La principal confusión es:

```text
cloud → backend
```

## Conclusión

v1.2 mejora claramente el rendimiento multilingual respecto de v1.1.

La principal prioridad de una futura v1.3 debe ser mejorar la frontera `Cloud ↔ Backend` usando nuevo entrenamiento y un nuevo holdout independiente.
