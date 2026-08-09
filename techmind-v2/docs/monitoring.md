# Monitoring de TechMind

## Objetivo

Supervisar el comportamiento del modelo una vez desplegado y detectar cambios relevantes en datos y predicciones.

## Indicadores

- distribución de categorías;
- tasa de aceptación;
- tasa de revisión;
- tasa de rechazo;
- margen de decisión;
- cobertura;
- features activas;
- drift;
- comportamiento por lotes.

## Estructura

```text
monitoring/
├── config/
│   ├── monitoring_config.json
│   ├── reference_profile.json
│   └── reference_predictions.csv
├── batches/
└── logs/
```

## Reportes

```text
reports/monitoring/
├── monitoring_report.json
├── monitoring_summary.csv
└── figures/
```

## Referencia v1.1.0

```text
Accuracy aceptadas: 95.08%
Review/reject rate: 26.83%
Error capture rate: 77.08%
```

## Señales de alerta

- aumento sostenido de revisión;
- aumento de rechazo;
- reducción de cobertura;
- cambios fuertes en categorías;
- reducción de margen;
- drift elevado;
- aparición frecuente de nuevas tecnologías.

## Reentrenamiento

El monitoring no debe modificar automáticamente el modelo.

Un nuevo modelo debe pasar nuevamente por:

```text
Datos
  ↓
Validación
  ↓
Cross-validation
  ↓
Test reservado
  ↓
Robustez
  ↓
Calibración
  ↓
Versionado
```
