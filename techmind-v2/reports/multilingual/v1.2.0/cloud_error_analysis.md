# Cloud Error Analysis — v1.2.0-multilingual

## Resumen

La principal limitación identificada en el benchmark multilingual final corresponde a la categoría:

```text
cloud
```

Accuracy:

```text
0.4000
```

---

## Distribución de predicciones

Sobre los `80` ejemplos reales de Cloud:

```text
Predicho backend       42
Predicho cloud         32
Predicho datascience    6
```

Esto implica:

```text
32 / 80 correctos
48 / 80 errores
```

La mayoría de las confusiones fueron:

```text
cloud → backend
```

---

## Peso dentro de los errores globales

En el benchmark final v1.2:

```text
Errores totales = 76
Errores reales Cloud = 48
```

Por tanto:

```text
48 / 76 ≈ 63.16%
```

de los errores finales provienen de ejemplos cuya categoría real era `cloud`.

---

## Interpretación

El patrón sugiere que la principal dificultad no es puramente lingüística.

Los errores Cloud aparecen en diferentes idiomas, por lo que la causa probable está asociada a:

- frontera conceptual `Cloud ↔ Backend`;
- cobertura insuficiente del corpus;
- servicios Cloud descritos desde una perspectiva de aplicación;
- vocabulario compartido entre despliegue, APIs, servicios y backend;
- ejemplos híbridos donde infraestructura y lógica de aplicación se superponen.

---

## Ejemplos de reglas que NO deben agregarse

No se recomienda aplicar correcciones manuales como:

```text
si contiene "AWS" → cloud
si contiene "Docker" → cloud
si contiene "Kubernetes" → cloud
si contiene "API" → backend
```

Estas reglas:

- pueden introducir falsos positivos;
- no resuelven la frontera semántica;
- reducen capacidad de generalización;
- rompen la trazabilidad del modelo;
- contaminan la evaluación futura.

---

## Recomendación para v1.3

La mejora debe abordarse mediante una nueva versión del modelo.

Prioridades:

1. ampliar ejemplos Cloud reales;
2. agregar casos de frontera Cloud/Backend;
3. balancear servicios gestionados e infraestructura;
4. incluir ejemplos negativos cercanos;
5. realizar error analysis por subdominio;
6. reentrenar;
7. crear un nuevo benchmark independiente;
8. congelar nuevamente hiperparámetros y thresholds.

---

## Estado

Esta limitación está:

```text
known
documented
not patched with keyword rules
```

y constituye la principal prioridad técnica para una futura `v1.3`.
