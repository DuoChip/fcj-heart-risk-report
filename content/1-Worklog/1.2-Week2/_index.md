---
title: "Week 2: Dataset review and preprocessing design"
weight: 2
chapter: false
pre: " <b>1.2.</b> "
---

# Week 2: Dataset review and preprocessing design

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Inspected 7,000 rows and 22 columns; excluded `patient_id`; identified 11 missing-value columns; designed a stratified 70/15/15 split and train-only preprocessing.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** Fitting transformations before splitting could leak validation/test information.
- **Resolution/decision:** Split first; fit median/mode imputation, one-hot encoding, and scaling on training data only.

## Result

Produced 36 processed features, no duplicates, and zero missing values after processing.

## Evidence

Referenced evidence catalog: `W2-02`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
