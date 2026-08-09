# Migración v1.0.0 → v1.1.0

## Arquitectura

### v1.0.0

```text
TF-IDF Word → SGDClassifier
```

### v1.1.0

```text
TF-IDF Word
      +
TF-IDF Char 3-6
      ↓
FeatureUnion
      ↓
SGDClassifier
```

## Cambios

- normalización Unicode;
- stopwords controladas;
- nueva rama Char 3–6;
- 60,000 features;
- cobertura Word + Char;
- calibración OOF;
- explicabilidad con `feature_type`.

## Compatibilidad API

La API permanece en `1.0.0`.

## Regresión corregida

El caso corto de Spring Boot/API REST ahora se clasifica correctamente como `backend`.

## Importante

No recalibrar desde backend:

- review margin;
- few features threshold;
- stopwords;
- TF-IDF;
- char n-grams;
- SGDClassifier.
