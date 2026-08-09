# Referencia de API — TechMind

## Versionado

```text
Package:       1.1.0
Model:         1.1.0
API interface: 1.0.0
```

## Endpoints

```text
GET  /
GET  /health
GET  /model-info
POST /predict
GET  /docs
GET  /redoc
GET  /openapi.json
```

## GET /health

Debe responder HTTP 200 y `ready=true` antes de enviar tráfico a `/predict`.

## GET /model-info

Incluye:

- model_version;
- model_sha256;
- classes;
- word_features;
- char_features;
- total_features;
- limits;
- margin_thresholds.

## POST /predict

### Request

```json
{
  "textos": [
    "Este contenido explica cómo crear una API REST con Spring Boot y Java, incluyendo controladores, servicios y repositorios."
  ],
  "incluir_explicacion": true,
  "top_n_explicacion": 8,
  "top_k": 4
}
```

## Campos principales

| Campo | Descripción |
|---|---|
| `categoria_predicha` | Clase principal |
| `segunda_categoria` | Segunda clase |
| `estado` | aceptada, revision o rechazada |
| `margen_decision` | Diferencia entre scores |
| `requiere_revision` | Revisión humana |
| `prediccion_utilizable` | Puede utilizarse |
| `word_features_activas` | Features Word activas |
| `char_features_activas` | Features Char activas |
| `features_activas_total` | Cobertura total |
| `terminos_activos` | Alias retrocompatible |

## Scores

```json
{
  "margin_is_probability": false
}
```

Los scores no deben convertirse a porcentajes.

## Cobertura

```text
word_features_activas = 0
char_features_activas = 215
features_activas_total = 215
```

Este caso tiene cobertura válida gracias a la rama Char.

## Caso de regresión

El texto corto de Spring Boot / API REST debe producir:

```text
categoria_predicha = backend
estado = aceptada
prediccion_utilizable = true
```
