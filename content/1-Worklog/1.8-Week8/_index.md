---
title: "Week 8: SageMaker Pipeline and final reporting"
weight: 8
chapter: false
pre: " <b>1.8.</b> "
---

**Dates:** 3 August 2026 – 15 August 2026

## Objectives and work completed

- Integrated preprocessing, training, evaluation, condition, registration, and fail steps into SageMaker Pipeline.
- Ran pass and intentional-fail executions to verify the quality gate.
- Reviewed data flow, IAM, cost, and resource lifecycle; organized the bilingual Hugo site, workshop, report, and cleanup runbook.

## Problem and decision

- The Pipeline did not exist before first creation, so definition/upsert precedes list or execute operations.
- Evidence must be retained before cleanup; deletion is not claimed without verification logs.

## Result

The successful execution registered Model Package version 3 as `PendingManualApproval`. An AUC threshold of 0.99 reached the fail step and blocked registration by design. From 10–15 August, results were reviewed, documented, and handed over to close the internship.

## Evidence

Catalog: `W8-01–W8-07`, covering the Pipeline graph, successful execution, passing condition, and intentional failure.

## Summary

The eight weeks form one continuous workflow from environment and data preparation through training, deployment, monitoring, automation, and reporting, using versioned outputs instead of manual notebook state.
