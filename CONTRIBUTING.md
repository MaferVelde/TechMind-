# Contributing to IndexMind / TechMind

Gracias por tu interés en contribuir a **IndexMind / TechMind**.

Este repositorio combina componentes de:

- Ciencia de Datos
- Machine Learning
- NLP multilingual
- Backend
- API REST
- Docker
- Deployment

El objetivo de estas reglas es mantener la reproducibilidad del proyecto, preservar el historial de versiones y evitar cambios que alteren silenciosamente el comportamiento de los modelos ya validados.

---

# 1. Alcance de las contribuciones

Son bienvenidas contribuciones relacionadas con:

- corrección de errores;
- documentación;
- tests;
- mejoras de rendimiento;
- observabilidad;
- tooling;
- integración;
- refactorizaciones seguras;
- nuevos benchmarks;
- nuevas versiones del modelo;
- mejoras de deployment;
- nuevas evaluaciones;
- mejoras de explicabilidad.

---

# 2. Versiones actuales

## v1.1.0

```text
stable baseline / fallback
```

Arquitectura principal:

```text
TF-IDF Word
+
TF-IDF Character
+
SGDClassifier
```

## v1.2.0-multilingual

```text
validated_experimental_candidate
```

Arquitectura:

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

---

# 3. Componentes congelados de v1.2

Los siguientes elementos de `v1.2.0-multilingual` están congelados y **no deben modificarse dentro de la misma versión**:

```text
LinearSVC C = 0.3

Semantic Domain Support threshold = 0.4266

Decision Margin threshold = 0.8132

Embedding model =
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

Embedding dimension = 384

Classes =
backend
cloud
datascience
frontend
```

También se consideran parte del contrato operacional:

```text
accepted
review
rejected_ood
rejected_invalid
```

Si una contribución necesita modificar cualquiera de estos elementos, debe proponerse como una **nueva versión del modelo**.

Ejemplo:

```text
v1.3.0
```

y no como una modificación silenciosa de `v1.2.0-multilingual`.

---

# 4. Artefacto v1.2

Artefacto de deployment:

```text
models/experimental/v1.2.0-multilingual/
techmind_hybrid_v1_2_0_multilingual.joblib
```

SHA-256 certificado:

```text
1a495520f642416e7dd391f97417cd3d12dcd82ab11636b7f190e5ed6dafea61
```

No debe:

- reemplazarse por otro `.joblib`;
- reserializarse;
- regenerarse;
- modificarse;
- cambiarse el SHA esperado

únicamente para hacer que una prueba pase.

Si se genera un nuevo artefacto, debe tratarse como una nueva versión y documentarse en:

```text
CHANGELOG.md
docs/versions/
reports/
```

---

# 5. Flujo recomendado de trabajo

## 5.1 Crear una rama

No trabajar directamente sobre `main`.

Ejemplos:

```bash
git checkout -b fix/api-validation
```

```bash
git checkout -b docs/model-card
```

```bash
git checkout -b feature/v1.3-cloud-improvement
```

Nombres recomendados:

```text
fix/...
docs/...
test/...
feature/...
refactor/...
experiment/...
```

---

## 5.2 Mantener la rama actualizada

Antes de comenzar:

```bash
git checkout main
git pull origin main
```

Después crear la rama:

```bash
git checkout -b feature/nombre-del-cambio
```

---

# 6. Convención de commits

Se recomienda utilizar mensajes de commit descriptivos.

Formato:

```text
tipo: descripción breve
```

Tipos sugeridos:

```text
feat
fix
docs
test
refactor
perf
chore
build
ci
```

Ejemplos:

```text
docs: add v1.2 multilingual model card
```

```text
test: add v1.2 artifact integrity checks
```

```text
fix: preserve decision field in backend response
```

```text
feat: add v1.3 cloud boundary experiment
```

Evitar mensajes poco descriptivos como:

```text
update
changes
fix stuff
final
```

---

# 7. Tests

Antes de crear un Pull Request, ejecutar los tests relacionados con el cambio.

## Tests históricos

```text
tests/
```

incluye pruebas de versiones anteriores.

## Tests v1.2

```text
tests/v1.2/
```

Ejecutar:

```bash
python -m pytest tests/v1.2 -v
```

Estos tests cubren:

- integridad del artefacto;
- SHA-256;
- predictor v1.2;
- inferencia multilingual;
- estados operacionales;
- FastAPI;
- OOD;
- entradas inválidas.

---

# 8. Docker

Si la contribución afecta:

- dependencias;
- predictor;
- API;
- startup;
- modelo;
- Dockerfile;
- variables de entorno;
- healthcheck

también debe ejecutarse el smoke test Docker.

Build:

```bash
docker build \
  --progress=plain \
  -f deploy/v1.2.0-multilingual/docker/Dockerfile \
  -t techmind:v1.2.0-multilingual \
  .
```

Levantar:

```bash
docker compose \
  -f deploy/v1.2.0-multilingual/docker/compose.yaml \
  up -d
```

Smoke test:

```bash
python deploy/v1.2.0-multilingual/docker/smoke_test_docker.py
```

Resultado esperado:

```text
DOCKER SMOKE TEST PASSED
```

---

# 9. Cambios en Ciencia de Datos

Una modificación del modelo debe documentar como mínimo:

- motivación;
- hipótesis;
- dataset utilizado;
- split;
- benchmark;
- métrica principal;
- comparación contra baseline;
- hiperparámetros;
- impacto operacional;
- limitaciones;
- reproducibilidad.

No se aceptan cambios basados únicamente en mejorar ejemplos individuales.

---

# 10. Nuevas versiones del modelo

Si una contribución modifica:

- arquitectura;
- clases;
- encoder;
- embedding model;
- classifier;
- hiperparámetros;
- thresholds;
- reglas operacionales

debe proponerse una nueva versión.

Una nueva versión debe incluir:

```text
models/<version>/
docs/versions/<version>/
reports/<version>/
tests/
CHANGELOG.md
```

y, cuando corresponda:

```text
deploy/<version>/
```

---

# 11. Benchmarks

## Benchmark de desarrollo

Puede utilizarse para:

- diagnóstico;
- comparación;
- experimentación.

## Benchmark final independiente

No debe utilizarse para:

- retuning;
- selección de hiperparámetros;
- selección de thresholds;
- ajustes manuales posteriores.

Si una nueva versión se desarrolla después de haber visto el benchmark final anterior, debe utilizar un **nuevo holdout independiente** para evaluación final.

---

# 12. Regla sobre Cloud ↔ Backend

La principal limitación conocida de v1.2 es:

```text
cloud ↔ backend
```

No deben introducirse reglas manuales como:

```text
AWS → cloud
Docker → cloud
API → backend
```

Las mejoras deben realizarse mediante:

- nuevos datos;
- nuevos experimentos;
- reentrenamiento;
- validación;
- nuevo benchmark.

---

# 13. API y contrato operacional

Backend debe utilizar:

```text
decision
```

como autoridad operacional.

Los scores:

```text
score_top1
score_top2
```

son scores de `LinearSVC`.

No son probabilidades.

No deben exponerse como:

```text
probabilidad
confidence_percentage
porcentaje_confianza
```

sin una calibración probabilística explícita en una nueva versión.

---

# 14. Documentación

Los cambios relevantes deben actualizar la documentación correspondiente.

## Modelo

```text
docs/versions/
```

## Resultados

```text
reports/
```

## Historial

```text
CHANGELOG.md
```

## README

Actualizar únicamente cuando el cambio afecte:

- arquitectura;
- versiones;
- métricas;
- uso;
- instalación;
- deployment.

---

# 15. Pull Requests

Todo Pull Request debe explicar:

## Qué cambia

Descripción clara del cambio.

## Por qué

Motivación técnica.

## Cómo se validó

Tests, métricas o evidencias.

## Impacto

Indicar si afecta:

- API;
- modelo;
- artefacto;
- Docker;
- documentación;
- compatibilidad;
- deployment.

---

# 16. Checklist para Pull Request

Antes de enviar un PR:

- [ ] El cambio está en una rama separada.
- [ ] El código ejecuta correctamente.
- [ ] Los tests relevantes pasan.
- [ ] No se modificó el artefacto v1.2 accidentalmente.
- [ ] El SHA certificado sigue siendo correcto, si aplica.
- [ ] No se modificaron thresholds congelados dentro de v1.2.
- [ ] No se añadieron reglas manuales por palabras clave.
- [ ] La documentación fue actualizada si corresponde.
- [ ] `CHANGELOG.md` fue actualizado si el cambio es relevante.
- [ ] No se subieron caches, archivos temporales o secretos.
- [ ] No se incluyeron credenciales, tokens o contraseñas.

---

# 17. Archivos que no deben subirse

Evitar subir:

```text
.env
.env.*
__pycache__/
*.pyc
.ipynb_checkpoints/
.cache/
huggingface cache
model downloads duplicados
logs locales
credenciales
tokens
keys
```

Los archivos grandes deben versionarse únicamente cuando sean necesarios para reproducibilidad o deployment.

---

# 18. Seguridad

Nunca incluir en commits:

- contraseñas;
- API keys;
- claves OCI;
- tokens GitHub;
- certificados privados;
- secretos de deployment.

Si un secreto se publica accidentalmente, debe rotarse inmediatamente.

---

# 19. Licencia

Al contribuir a este repositorio, se entiende que la contribución puede distribuirse bajo la licencia definida en:

```text
LICENSE
```

Los modelos preentrenados, librerías y otros recursos de terceros conservan sus respectivas licencias.

---

# 20. Código de conducta

Se espera una colaboración profesional, técnica y respetuosa.

Las discusiones deben centrarse en:

- evidencia;
- reproducibilidad;
- calidad de implementación;
- impacto técnico.

---

# 21. Resumen

El principio central de contribución es:

> **No modificar silenciosamente un modelo ya validado.**

La evolución debe ser:

```text
hipótesis
  ↓
experimento
  ↓
evaluación
  ↓
documentación
  ↓
nueva versión
```

Esto permite conservar:

- trazabilidad;
- reproducibilidad;
- comparabilidad;
- rollback;
- integridad del proyecto.
