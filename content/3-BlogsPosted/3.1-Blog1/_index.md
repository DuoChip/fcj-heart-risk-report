---
title: "Cost Optimization for a Personal SageMaker MLOps Project"
weight: 1
chapter: false
pre: " <b>3.1.</b> "
---

## Introduction and motivation

Continuously running endpoints differ from processing and training jobs that stop when work ends. The PoC therefore used three sequential HPO trials, one endpoint instance, Budget alerts, tags, and a cleanup runbook.

## Flow and implementation

List active endpoints before deletion:

```bash
aws sagemaker list-endpoints --region "$AWS_REGION" --status-equals InService
```

Retain reports and sanitized evidence before deleting compute. Keep the S3 bucket private and never embed credentials.

## Result and lessons

The implementation favors measurable evidence, explicit failure behavior, and cost-aware operation. IAM roles replace hard-coded keys; active URLs and sensitive ARNs must be masked.

## Publication status

- TODO: AWS Study Group publication URL
- TODO: Publication date
- TODO: Publication screenshot
