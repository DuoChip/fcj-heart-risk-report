---
title: "Overview"
weight: 1
chapter: false
pre: " <b>5.1.</b> "
---

# Workshop overview

## Objective and success criteria

Build a traceable flow from versioned raw data to monitored API and quality-gated Pipeline. The final LR model achieved test AUC 0.885515, F1 0.768903, and recall 0.818594, passing gates 0.84/0.70/0.65.

| Component | Verified result |
|---|---|
| Processing | 4,900/1,050/1,050; 36 features; no missing values |
| Registry/deployment | version 2 Approved and deployed |
| API | 200, 400, and controlled 502 |
| Drift | 6/20 violations; alarm `ALARM` |
| Pipeline | success registers v3 pending; intentional fail blocks |

![Student-created architecture showing data, training, inference, and monitoring flows](../../images/architecture/heart-risk-architecture.jpg)

The student-created diagram establishes the main AWS service relationships and makes the S3-centered training and inference flow explicit.

## Personal Contributions and Customizations

The project replaces the sample use case with a custom dataset; adds SHA-256 versioning/idempotent upload, train-only preprocessing, LR/XGBoost comparison, Bayesian HPO, three quality gates, Registry/manual approval, endpoint/Lambda/API tests (200/400/502), Data Capture, custom drift fallback and metrics, sparse-alarm resolution, Pipeline pass/fail paths, and cautious medical limitations.

## Prerequisite, errors, cost and next step

Use `us-east-1`, private S3, service roles, Budget alerts, and no credentials in code. The supplied evidence catalog is rendered and interpreted throughout the workshop.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

Next: [Prerequisites](../5.2-Prerequisites/).
