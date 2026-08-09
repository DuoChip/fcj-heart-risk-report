---
title: "Proposal"
weight: 2
chapter: false
pre: " <b>2.</b> "
---

# Project proposal

## 1. Executive summary

The proposal plans an educational MLOps proof of concept that turns a local heart-risk classification experiment into a reproducible AWS workflow. It is not intended for clinical use.

## 2. Background and problem statement

A notebook alone lacks reproducible managed processing, model version management, quality gates, real-time deployment, API access, monitoring/alerting, and an automated pass/fail workflow.

## 3. Target users

- Students and engineers learning AWS SageMaker MLOps
- ML teams evaluating a reproducible PoC workflow
- Application developers integrating a non-clinical prediction API

## 4. Objectives and scope

The scope covers versioned data, leakage-safe processing, LR/XGBoost training and HPO, final evaluation, Model Registry, one real-time endpoint, Lambda/API Gateway, Data Capture, custom drift monitoring, CloudWatch, Pipeline automation, documentation, and cleanup. Clinical validation, diagnosis, production authentication, CI/CD, IaC, fairness analysis, and automated retraining are out of scope.

## 5. Expected outputs

Versioned S3 data/manifest; train/validation/test data; preprocessing/model artifacts; HPO and evaluation reports; Registry versions; approved deployed model; endpoint and API; capture JSONL; drift report; metrics/alarm; Pipeline pass/fail executions; cleanup runbook and, after execution, evidence.

## 6. Success criteria

| Gate/check | Target |
|---|---:|
| Test ROC-AUC | ≥ 0.84 |
| Test F1 | ≥ 0.70 |
| Test recall | ≥ 0.65 |
| API tests | 200, 400, 502 handled |
| Monitoring | custom metrics and alarm |
| Pipeline | pass registers; fail blocks |

## 7. Solution architecture

![Hand-created Heart Risk MLOps architecture](../images/architecture/heart-risk-architecture.jpg)

This student-created architecture diagram connects the offline SageMaker workflow, online API inference path, and monitoring path. It is the submitted architecture artifact rather than an automatically generated diagram.

## 8. AWS services and rationale

| Service | Selection rationale |
|---|---|
| Amazon S3 | Durable storage for raw/processed data, capture, reports, artifacts |
| SageMaker Processing/Training/HPO | Reproducible jobs independent of a notebook |
| Model Registry | Versions, metadata, manual approval |
| SageMaker Endpoint | Managed real-time inference |
| Lambda and API Gateway | Validation wrapper and HTTP integration |
| CloudWatch | Logs, custom metrics, alarms |
| SageMaker Pipeline | Automated quality-gated workflow |
| AWS Budgets | Cost visibility and alerts |

## 9. Data and ML approach

The 7,000-row dataset has 22 original columns. `patient_id` is excluded, leaving 20 raw features and target `heart_attack_risk` (~42% positive). A stratified 70/15/15 split yields 4,900/1,050/1,050 rows. The preprocessor is fitted only on train: numeric median imputation and scaling, categorical most-frequent imputation and one-hot encoding, producing 36 features with zero missing values.

## 10. Eight-week timeline

Weeks 1–3 cover onboarding, AWS foundations, and SageMaker; week 4 prepares the project environment; week 5 processes data; week 6 trains, evaluates, and registers the model; week 7 deploys the endpoint, API, and monitoring; week 8 automates the Pipeline and completes reporting. The internship runs from 15 June 2026 to 15 August 2026.

## 11. Budget and controls

Budget alerts, tags, only three sequential HPO trials, one endpoint instance, job-based processing/training, and dependency-ordered cleanup constrain spend. **No exact final cost is claimed without Cost Explorer evidence.**

## 12. Risks and mitigation

| Risk | Mitigation |
|---|---|
| Data leakage | Split first; fit preprocessing on train only |
| Over-permissioned roles | Separate trust policies and scoped S3/endpoint access |
| Endpoint cost | One PoC instance; delete after evidence |
| Missing official drift metric | Custom managed drift job and explicit PoC thresholds |
| Unsafe interpretation | Disclaimer, limitations, no clinical users/claims |

## 13. Expected benefits

The project demonstrates reproducibility, traceability, operational monitoring, controlled promotion, and failure-safe automation across AWS services.

## 14. Ethical and medical limitations

The dataset is non-clinical; no fairness assessment or probability calibration is performed. Predictions must not guide care.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}
