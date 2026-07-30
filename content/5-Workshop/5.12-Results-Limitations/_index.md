---
title: "Results and limitations"
weight: 12
chapter: false
pre: " <b>5.12.</b> "
---

# Results, limitations, and future work

## Results

| Area | Result |
|---|---|
| Data | 7,000 rows; 20 raw/36 processed features; train-only fit |
| Model | LR selected; test AUC 0.885515, F1 0.768903 |
| API | health/predict plus 200/400/502 behavior |
| Drift | six features; custom metrics 1 and 6; alarm ALARM |
| Pipeline | pass registers v3 pending; 0.99 test blocks registry |

## Problems encountered and resolutions

| Problem | Root cause | Resolution |
|---|---|---|
| Leakage risk | preprocessing before proper split | split first; fit train only |
| `ml.t3.medium` rejected | unsupported package instance | use `ml.m5.large` |
| Official drift metric absent | expected metric not published in test | custom Processing and metrics |
| Alarm returned/stayed OK | sparse periods treated non-breaching | `TreatMissingData=ignore`; fresh point |
| Pipeline absent initially | not upserted | run definition/upsert first |
| SDK v2 warnings | SageMaker SDK v2 | document migration to v3 |
| Alarm history denied | missing permission | use `describe-alarms`; optionally scope history permission |

## Personal contributions

Custom dataset and SHA-256/idempotent upload design; leakage-safe preprocessing; LR/XGBoost/HPO comparison; three gates and manual promotion; API error contract; Data Capture; custom drift/CloudWatch fallback; sparse metric fix; pass/fail Pipeline; bilingual reproducible documentation and disclaimer.

## Limitations

Non-clinical data; no fairness assessment or probability calibration; only three HPO trials; one endpoint; no production authentication; PoC drift rules; expected official feature metric not observed; SDK v2 debt; no automated retraining, CI/CD, or IaC.

## Future work

Evaluate fairness/calibration with appropriate governance; add authentication, throttling, private networking, encryption strategy, Auto Scaling, IaC/CI/CD, SDK v3 migration, automated-but-approved retraining, and cost evidence.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}
