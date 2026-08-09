---
title: "Week 7: Model deployment, API, and monitoring"
weight: 7
chapter: false
pre: " <b>1.7.</b> "
---

**Dates:** 27 July 2026 – 2 August 2026

## Objectives and work completed

- Deployed Model Package version 2 to `heart-risk-endpoint` on `ml.m5.large` with 100% input/output Data Capture.
- Built `heart-risk-api` Lambda with least-privilege endpoint invocation and exposed `GET /health` and `POST /predict` through API Gateway.
- Verified JSONL capture, prepared baseline/current data, and implemented a custom Processing fallback when the expected feature-level metric did not appear.
- Published `DriftDetected` and `DataQualityViolationCount` to `Custom/HeartRisk` and configured a CloudWatch alarm.

## Problem and decision

- The package did not support `ml.t3.medium`, so deployment used `ml.m5.large`.
- Public errors were normalized to avoid exposing internals or an active URL.
- Sparse batch metrics use `TreatMissingData=ignore` to preserve meaningful alarm behavior.

## Result

The endpoint reached `InService`; the API handled HTTP 200, 400, and 502 as designed. Data Capture recorded real traffic. The custom monitor found six drifted features, published values 1 and 6, and moved the alarm to `ALARM`.

## Evidence

Catalog: `W6-01a–W6-13`, `W7-01a–W7-05`. Evidence is analyzed in the corresponding workshop pages.

## Reflection and next step

These outputs feed the final week's Pipeline integration, quality-gate testing, and reporting.
