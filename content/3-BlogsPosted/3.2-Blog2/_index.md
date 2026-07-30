---
title: "Model Registry and Quality Gates in SageMaker Pipelines"
weight: 2
chapter: false
pre: " <b>3.2.</b> "
---

# Model Registry and Quality Gates in SageMaker Pipelines

## Introduction and motivation

Model versions separate trained artifacts from promotion decisions. Versions 1 and 2 were Approved; version 2 was deployed; the Pipeline created version 3 as PendingManualApproval.

## Flow and implementation

The `ConditionStep` checks AUC ≥ 0.84, F1 ≥ 0.70, and recall ≥ 0.65. The pass branch registers; the fail branch raises `MetricThresholdFailed`. An intentional AUC threshold of 0.99 verified that registration is blocked. Auto-deployment is excluded so a person reviews evidence and cost.

## Result and lessons

The implementation favors measurable evidence, explicit failure behavior, and cost-aware operation. IAM roles replace hard-coded keys; active URLs and sensitive ARNs must be masked.

## Publication status

- TODO: AWS Study Group publication URL
- TODO: Publication date
- TODO: Publication screenshot
