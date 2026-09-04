# Archived deployment — TechMind v1.0.0

This directory preserves the historical deployment files generated during the
v1.0.0 stage of the project.

## Status

```text
historical / archived / not for current deployment
```

These files are kept only for traceability. They are **not** the recommended
deployment path for IndexMind / TechMind.

The archived v1.0 deployment may reference files that were part of the original
packaging workflow and are no longer present at the repository root.

## Current deployment

Use the validated v1.2 multilingual deployment instead:

```text
deploy/v1.2.0-multilingual/
```

The current v1.2 deployment includes:

- CPU-only Docker build;
- FastAPI service;
- certified v1.2 artifact;
- SHA-256 validation;
- offline SentenceTransformer runtime support;
- health checks;
- Docker smoke tests.

## Version roles

```text
v1.0.0                 historical first production version
v1.1.0                 stable baseline / fallback
v1.2.0-multilingual    validated experimental candidate
```

Do not use the files in this archive as the source of truth for v1.2 deployment,
API configuration, model hashes, or dependency versions.
