---
title: "Week 11: SageMaker Pipeline"
weight: 11
chapter: false
pre: " <b>1.11.</b> "
---

# Week 11: SageMaker Pipeline

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Built preprocessing, training, evaluation, condition, registration, and fail steps; ran pass and intentional-fail executions.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** The pipeline was absent before its first upsert.
- **Resolution/decision:** Ran the pipeline definition/upsert before listing or executing it.

## Result

Success registered version 3 as PendingManualApproval; AUC threshold 0.99 blocked registration by design.

## Evidence

Referenced evidence catalog: `W8-01–W8-07`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
