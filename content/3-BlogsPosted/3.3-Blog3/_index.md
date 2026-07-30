---
title: "Custom Data Drift Monitoring with SageMaker Processing and CloudWatch"
weight: 3
chapter: false
pre: " <b>3.3.</b> "
---

## Introduction and motivation

Data Capture provides current inference records, while the 4,900-row training baseline anchors comparison. The expected official feature metric was not observed, so the project implemented a transparent fallback.

## Flow and implementation

A custom Processing Job checked 20 features: numeric standardized mean shift > 0.5 and categorical total variation distance > 0.20. Six features drifted. It published `DriftDetected=1` and `DataQualityViolationCount=6`; `TreatMissingData=ignore` prevented sparse batch periods from overwriting the useful state. These are PoC rules, not universal or clinical thresholds.

## Result and lessons

The implementation favors measurable evidence, explicit failure behavior, and cost-aware operation. IAM roles replace hard-coded keys; active URLs and sensitive ARNs must be masked.

## Publication status

- **Status:** Draft — no publication claim or URL
