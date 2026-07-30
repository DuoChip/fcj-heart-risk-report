---
title: "Week 10: Custom drift fallback and CloudWatch"
weight: 10
chapter: false
pre: " <b>1.10.</b> "
---

# Week 10: Custom drift fallback and CloudWatch

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Ran a custom Processing Job over 20 features and published `DriftDetected` and `DataQualityViolationCount` to `Custom/HeartRisk`.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** Sparse batch metrics caused missing periods to reset alarm behavior.
- **Resolution/decision:** Set `TreatMissingData=ignore` and published a fresh datapoint.

## Result

Six features drifted; values were 1 and 6; alarm reached `ALARM`.

## Evidence

Referenced evidence catalog: `W7-01a–W7-05`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
