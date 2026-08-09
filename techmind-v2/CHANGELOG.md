# Changelog

Todos los cambios relevantes de **TechMind** se documentan en este archivo.

El proyecto utiliza versionado semántico para distinguir la evolución del modelo, del package y de la interfaz API.

---

## [1.1.0] - 2026-08-07

### Added

- Arquitectura híbrida **TF-IDF Word + TF-IDF Char**.
- Rama de caracteres con `char_wb`.
- N-gramas de caracteres `3–6`.
- Hasta `30,000` features Word.
- Hasta `30,000` features Char.
- `60,000` features totales.
- Normalización Unicode.
- Stopwords españolas controladas.
- Calibración operacional mediante predicciones **Out-of-Fold de 5 folds**.
- Nuevos campos de cobertura:
  - `word_features_activas`
  - `char_features_activas`
  - `features_activas_total`
- Campo `feature_type` en las explicaciones del modelo.
- Información de `model_version` en la API.
- Información de Word, Char y total features en `/health` y `/model-info`.
- Pruebas de regresión para textos técnicos cortos.
- Smoke test independiente del predictor.
- Validación FastAPI para v1.1.0.
- Documentación de migración desde v1.0.0.
- Guía de integración para el equipo de Backend.

### Changed

- El pipeline productivo cambia de:

```text
TF-IDF Word
      ↓
SGDClassifier
```

a:

```text
TF-IDF Word
      +
TF-IDF Char 3-6
      ↓
FeatureUnion
      ↓
SGDClassifier optimizado
```

- La cobertura operacional ahora se calcula como:

```text
features_activas_total =
word_features_activas +
char_features_activas
```

- `terminos_activos` se conserva como alias retrocompatible del total de features activas.
- La API mantiene la interfaz `1.0.0` para preservar compatibilidad con integraciones existentes.

### Fixed

- Clasificación incorrecta de textos técnicos cortos relacionados con:
  - Spring Boot
  - Java
  - API REST
  - controladores
  - servicios
  - repositorios
- Dependencia excesiva de stopwords y correlaciones estilísticas en la representación Word-only.
- Interpretación incorrecta de `word_features_activas = 0` como falta total de cobertura.

### Metrics

Resultados finales de v1.1.0:

| Métrica | Resultado |
|---|---:|
| F1 Macro CV | 0.8493 |
| F1 Macro Test | 0.8441 |
| Accuracy Test | 0.8430 |
| Precision Macro | 0.8455 |
| Recall Macro | 0.8434 |
| F1 Weighted | 0.8435 |
| Diferencia Test-CV | -0.0052 |
| Accuracy predicciones aceptadas | 0.9508 |
| Tasa revisión/rechazo | 26.83% |
| Captura de errores | 77.08% |
| Casos externos correctos | 9/9 |
| Casos externos sin cobertura | 0 |

### Operational calibration

```text
review margin: 0.64346894252355
few features threshold: 178
reject if total features: 0
```

### Model integrity

SHA-256 del artefacto final aprobado:

```text
756b2577e731336ead95852ee1d8d752408762478a23d0bbf42cc9537e136ff6
```

### Version compatibility

```text
Package version: 1.1.0
Model version:   1.1.0
API interface:   1.0.0
```

---

## [1.0.0]

### Added

- Primera versión productiva de TechMind.
- TF-IDF basado en palabras.
- SGDClassifier optimizado.
- Predictor independiente `TechMindPredictor`.
- API REST con FastAPI.
- Endpoints:
  - `/`
  - `/health`
  - `/model-info`
  - `/predict`
  - `/docs`
  - `/redoc`
  - `/openapi.json`
- Explicabilidad lineal.
- Estados operacionales:
  - `aceptada`
  - `revision`
  - `rechazada`
- Pruebas de robustez.
- Monitoring.
- Docker.
- Preparación para deployment.
- Integración con OCI.

### Metrics

Resultados finales de v1.0.0:

| Métrica | Resultado |
|---|---:|
| Accuracy Test | 0.8386 |
| Precision Macro | 0.8445 |
| Recall Macro | 0.8385 |
| F1 Macro | 0.8401 |
| F1 Weighted | 0.8397 |

### Known limitation

La arquitectura Word-only podía presentar cobertura reducida en textos técnicos cortos y depender de correlaciones estilísticas.

Un caso corto relacionado con Spring Boot y API REST fue clasificado como `cloud`, aunque `backend` era la categoría correcta.

Este comportamiento motivó el desarrollo de **TechMind v1.1.0**.
