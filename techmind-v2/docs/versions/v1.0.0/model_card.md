# Model Card — TechMind v1.0.0

## Arquitectura

```text
TF-IDF Word
      ↓
SGDClassifier optimizado
```

## Métricas

| Métrica | Resultado |
|---|---:|
| Accuracy | 0.8386 |
| Precision Macro | 0.8445 |
| Recall Macro | 0.8385 |
| F1 Macro | 0.8401 |
| F1 Weighted | 0.8397 |

## Features

```text
30,000 TF-IDF Word
```

## Limitación

La representación Word-only podía depender de correlaciones estilísticas y stopwords.

Un texto corto sobre Spring Boot, Java y API REST fue clasificado incorrectamente como `cloud`, lo que motivó v1.1.0.
