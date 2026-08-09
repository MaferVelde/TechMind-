# Model Card — TechMind v1.1.0

## Identificación

- **Modelo:** TechMind
- **Model version:** `1.1.0`
- **Package version:** `1.1.0`
- **API interface:** `1.0.0`

## Objetivo

Clasificar contenido técnico en:

- backend
- cloud
- datascience
- frontend

## Arquitectura

```text
TF-IDF Word
      +
TF-IDF Char 3-6
      ↓
FeatureUnion
      ↓
SGDClassifier optimizado
```

## Features

```text
Word:  30,000
Char:  30,000
Total: 60,000
```

## Resultados

| Métrica | Resultado |
|---|---:|
| F1 Macro CV | 0.8493 |
| F1 Macro Test | 0.8441 |
| Accuracy Test | 0.8430 |
| Precision Macro | 0.8455 |
| Recall Macro | 0.8434 |
| F1 Weighted | 0.8435 |
| Diferencia Test-CV | -0.0052 |

## Rendimiento operacional

| Métrica | Resultado |
|---|---:|
| Accuracy de predicciones aceptadas | 95.08% |
| Tasa revisión/rechazo | 26.83% |
| Captura de errores | 77.08% |
| Casos externos correctos | 9/9 |
| Casos externos sin cobertura | 0 |

## Calibración operacional

```text
review margin: 0.64346894252355
few features threshold: 178
reject if total features: 0
```

La calibración se realizó con predicciones Out-of-Fold de 5 folds sobre entrenamiento.

## Estados

### aceptada

Predicción utilizable automáticamente.

### revision

Predicción válida, pero se recomienda revisión humana.

### rechazada

La predicción no debe utilizarse como resultado confiable.

## Explicabilidad

El predictor puede devolver:

- `positive_terms`
- `negative_terms`
- `differential_terms`

Cada feature puede indicar:

```text
feature_type = word | char
```

## Limitaciones

- Solo clasifica cuatro categorías.
- `margen_decision` no es probabilidad.
- Textos extremadamente cortos o multidisciplinarios pueden requerir revisión.
- Las explicaciones describen asociaciones matemáticas, no causalidad.
- El modelo puede requerir actualización ante drift significativo.

## Integridad

SHA-256 del artefacto final:

```text
756b2577e731336ead95852ee1d8d752408762478a23d0bbf42cc9537e136ff6
```
