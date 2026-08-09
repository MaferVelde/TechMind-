# Diccionario de datos

## Dataset

El dataset original contiene aproximadamente 5,000 registros distribuidos entre:

- backend
- cloud
- datascience
- frontend

Después de limpieza y validación:

```text
Registros finales: 4,583
Clases: 4
Balance ratio: 0.946
```

## Campos principales

| Campo | Tipo | Descripción |
|---|---|---|
| `titulo` | string | Título original del contenido |
| `texto` | string | Contenido técnico |
| `categoria` | string | Clase objetivo |
| `palabras_clave` | string/list | Palabras clave |
| `titulo_limpio` | string | Título normalizado |
| `texto_limpio` | string | Texto normalizado |
| `texto_combinado` | string | Unión de título y contenido |
| `texto_combinado_ponderado` | string | Variante con mayor peso del título |

## Variantes textuales

```text
texto_modelo_base
texto_modelo_titulo
texto_combinado
texto_combinado_ponderado
```

La variante con mejor rendimiento durante la selección fue:

```text
texto_combinado_ponderado
```

## Ingeniería de características

Se generaron 21 características numéricas.

Dos características HTML constantes fueron excluidas:

```text
cantidad_etiquetas_html
tiene_html
```

Por tanto, se utilizaron 19 características numéricas en los experimentos híbridos.

## Calidad final

- documentos vacíos: 0;
- nulos críticos: 0;
- infinitos: 0;
- duplicados textuales residuales: 0;
- categorías contradictorias residuales: 0.

## Split

```text
Train: 3,666
Test:    917
random_state: 42
```
