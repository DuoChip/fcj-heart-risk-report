---
title: "Hyperparameter optimization"
weight: 3
chapter: false
pre: " <b>5.5.3.</b> "
---

# Hyperparameter optimization

## Objective and configuration

Use a deliberately small managed Bayesian search to improve XGBoost without uncontrolled cost.

```python
objective_metric_name = "validation:auc"
strategy = "Bayesian"
max_jobs, max_parallel_jobs = 3, 1
tuned = ["eta", "max-depth", "min-child-weight"]
```

| Candidate | Validation AUC | F1 | Recall |
|---|---:|---:|---:|
| LR | **0.863949** | 0.747583 | 0.789116 |
| XGBoost default | 0.854283 | 0.749749 | 0.845805 |
| XGBoost HPO | 0.860982 | 0.749522 | **0.888889** |

LR remains selected by validation AUC. Test data was not used for model/trial selection. There is no HPO screenshot, so this page intentionally has no broken evidence image.

**Troubleshooting:** no best job usually means the objective metric regex/name was not emitted. Three sequential jobs constrain cost but also limit search quality.

Next: [Evaluation and Registry](../../5.6-Evaluation-Registry/).
