---
title: "Self-evaluation"
weight: 6
chapter: false
pre: " <b>6.</b> "
---

## Evaluation method

This self-evaluation uses eight equally weighted criteria. Each criterion is scored on a 10-point scale and linked to evidence produced during the Heart Risk MLOps project. The target overall score is **8.0/10**.

| Criterion | Score | Level | Evidence from the project | Next improvement |
|---|---:|---|---|---|
| Knowledge | 8.5/10 | Good | Built a multi-service workflow using Amazon S3, SageMaker Processing, Training, HPO, Model Registry, Endpoint and Pipeline, plus Lambda, API Gateway and CloudWatch. | Deepen knowledge of private networking, governance and SageMaker Python SDK v3. |
| Ability to learn | 8.5/10 | Good | Progressed from local notebook experiments to managed processing, model registration, monitoring and pipeline execution. | Reproduce the environment with Infrastructure as Code and CI/CD. |
| Proactiveness | 8.0/10 | Good | Validated preprocessing locally before starting managed jobs, defined model quality gates and captured operational evidence. | Define acceptance tests and evidence requirements at the start of each milestone. |
| Discipline | 7.5/10 | Fair | Kept versioned S3 outputs, separated train/test processing and used pass/fail quality gates. | Maintain a stricter task schedule and record resource-cleanup evidence consistently. |
| Communication | 7.5/10 | Fair | Produced a bilingual technical report and shared two technical posts with the AWS Study Group community. | Make technical presentations more concise and record structured reviewer feedback. |
| Teamwork | 7.0/10 | Fair | Coordinated the publication of project learning through community posts and documented shared references; however, detailed task ownership was not recorded throughout the project. | Keep a decision log with owners, deadlines and review outcomes. |
| Problem solving | 9.0/10 | Good | Replaced a missing official drift metric with a custom Processing job, corrected sparse-metric alarm handling, changed an unsupported instance type and made Pipeline creation idempotent. | Compare the custom monitoring approach with a fully configured official Model Monitor baseline. |
| Contribution | 8.0/10 | Good | Delivered an end-to-end PoC covering training, deployment, API inference, data capture, drift alarms and Pipeline pass/fail scenarios. | Package repeated steps as reusable modules and automate deployment and cleanup. |

## Overall result

| Measure | Result |
|---|---:|
| Total | **64.0/80** |
| Average | **8.0/10** |
| Overall level | **Good** |
| Target | **Achieved** |

## Reflection

The strongest outcome is the ability to diagnose integration issues across ML and AWS services while preserving data quality and traceability. The main gaps are not in the PoC result itself, but in production readiness: Infrastructure as Code, automated tests and deployment, security hardening, and more systematic teamwork records. These are the priorities for the next iteration.
