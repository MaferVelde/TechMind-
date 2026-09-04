# Documentación de TechMind

Esta carpeta contiene la documentación técnica oficial de **TechMind**, el motor de clasificación utilizado por **IndexMind**.

La documentación se organiza en dos niveles:

- documentación estable en la raíz de `docs/`;
- documentación específica de cada versión dentro de `docs/versions/`.

---

## Documentos principales

Los documentos ubicados directamente en `docs/` corresponden a la versión estable de referencia:

- `architecture.md` — arquitectura general del sistema.
- `data_dictionary.md` — diccionario de datos.
- `model_card.md` — ficha técnica del modelo estable.
- `api_reference.md` — referencia de la API REST estable.
- `monitoring.md` — estrategia de monitoreo.

---

## Documentación por versión

```text
versions/
├── v1.0.0/
├── v1.1.0/
└── v1.2.0-multilingual/
```

### v1.0.0

Primera versión productiva basada en:

```text
TF-IDF Word
+
SGDClassifier
```

### v1.1.0

Versión estable de referencia y fallback:

```text
TF-IDF Word
+
TF-IDF Character
+
SGDClassifier
```

Estado:

```text
stable baseline / fallback
```

### v1.2.0-multilingual

Evolución multilingual basada en:

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

Estado:

```text
validated_experimental_candidate
```

Documentación específica:

```text
docs/versions/v1.2.0-multilingual/
├── README.md
├── architecture.md
├── model_card.md
├── evaluation.md
├── multilingual_validation.md
├── operational_controls.md
└── deployment.md
```

---

## Versiones de referencia

### Versión estable

```text
Package:       1.1.0
Model:         1.1.0
API interface: 1.0.0
Status:        stable baseline / fallback
```

### Candidato multilingual

```text
Model:         1.2.0-multilingual
API interface: 1.2.0
Status:        validated_experimental_candidate
```

> La documentación ubicada directamente en `docs/` continúa representando la versión estable `v1.1.0`.
>
> La documentación de `v1.2.0-multilingual` se mantiene separada dentro de `docs/versions/v1.2.0-multilingual/` porque esta versión aún se considera un candidato experimental validado y no reemplaza al fallback estable.

---

## Relación con IndexMind

```text
IndexMind
   ↓
Backend / Frontend
   ↓
TechMind
   ↓
Modelo de clasificación
```

**IndexMind** es la solución presentada al usuario final.

**TechMind** es el motor de Ciencia de Datos / Machine Learning responsable de la clasificación técnica.

---

## Estado actual

| Componente | Versión | Estado |
|---|---|---|
| Baseline estable | `v1.1.0` | Stable / fallback |
| Modelo multilingual | `v1.2.0-multilingual` | Validated experimental candidate |
| API estable | `1.0.0` | Compatible con v1.1 |
| API multilingual | `1.2.0` | Disponible para v1.2 |
| Docker v1.2 | `v1.2.0-multilingual` | Validado |
| Documentación v1.2 | `docs/versions/v1.2.0-multilingual/` | Completa |

---

## Navegación recomendada

Para comprender la evolución del proyecto:

```text
v1.0.0
   ↓
v1.1.0
   ↓
06_evaluacion_multilingue.ipynb
   ↓
v1.2.0-multilingual
```

Para revisar la versión multilingual más reciente, comenzar por:

```text
docs/versions/v1.2.0-multilingual/README.md
```
