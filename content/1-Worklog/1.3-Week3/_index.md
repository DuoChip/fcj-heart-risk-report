---
title: "Week 3: Managed Processing Job"
weight: 3
chapter: false
pre: " <b>1.3.</b> "
---

# Week 3: Managed Processing Job

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Uploaded the raw dataset and manifest to S3, then ran managed preprocessing and persisted train, validation, test, baseline, reports, and artifacts.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** Outputs needed stable paths and repeatable execution.
- **Resolution/decision:** Used an S3-first layout and reusable preprocessing artifact.

## Result

Managed preprocessing completed with split sizes 4,900/1,050/1,050.

## Evidence

Referenced evidence catalog: `W2-01, W2-03`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
