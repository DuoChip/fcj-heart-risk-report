---
title: "Week 5: HPO and model selection"
weight: 5
chapter: false
pre: " <b>1.5.</b> "
---

# Week 5: HPO and model selection

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Ran three sequential Bayesian XGBoost HPO trials for `eta`, `max-depth`, and `min-child-weight`; optimized `validation:auc`.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** The test set must not influence model or trial selection.
- **Resolution/decision:** Selected only with validation results and reserved test for one final evaluation.

## Result

Best HPO AUC was 0.860982; LR remained the candidate based on validation AUC.

## Evidence

No dedicated HPO screenshot is available; the configuration and comparison metrics are documented without a broken image.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
