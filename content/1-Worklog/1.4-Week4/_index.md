---
title: "Week 4: Logistic Regression and XGBoost"
weight: 4
chapter: false
pre: " <b>1.4.</b> "
---

# Week 4: Logistic Regression and XGBoost

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Ran managed Logistic Regression and default XGBoost training jobs and compared validation behavior.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** A single metric did not describe the error trade-off.
- **Resolution/decision:** Compared AUC, F1, recall, precision, and the LR threshold 0.36.

## Result

LR AUC 0.863949; XGBoost AUC 0.854283. XGBoost recall was higher but precision and AUC were lower.

## Evidence

Referenced evidence catalog: `W3-01–W3-04`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
