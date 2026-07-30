---
title: "Architecture"
weight: 3
chapter: false
pre: " <b>5.3.</b> "
---

# Architecture

## Objective and flow

![Heart-risk AWS architecture](/images/architecture/heart-risk-architecture.svg)

**Offline:** raw S3 → Processing → split/artifacts → Training/HPO → Evaluation → Registry.  
**Online:** API Gateway → Lambda validation → endpoint → response; Data Capture writes JSONL to S3.  
**Monitoring:** capture/baseline → custom Processing → report → custom metrics → alarm.  
**Pipeline:** condition checks AUC/F1/recall; pass registers, fail emits `MetricThresholdFailed`.

| Implemented in PoC | Recommended for production |
|---|---|
| One endpoint instance | Auto Scaling and multi-AZ operational design |
| Public HTTP integration without production auth | Cognito/API keys/WAF and throttling |
| Service IAM roles, private S3 | VPC-only networking and KMS key strategy |
| Manual scripts and Pipeline | IaC, CI/CD, automated retraining with approval |

The SVG is an original documentation diagram, not evidence of resource state. Validate actual state through console/CLI and sanitized screenshots.

**Troubleshooting:** if arrows do not match artifact paths, inspect S3 URIs and Pipeline properties rather than copying objects manually. Services incur Region-specific charges.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

Next: [Data preparation](../5.4-Data-Preparation/).
