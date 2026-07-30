---
title: "Week 6: Final evaluation and Model Registry"
weight: 6
chapter: false
pre: " <b>1.6.</b> "
---

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Evaluated LR once on test data, checked three quality gates, and registered versioned packages with manual approval.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** False negatives require explicit interpretation without clinical claims.
- **Resolution/decision:** Reported all 80 false negatives and retained manual approval.

## Result

AUC 0.885515, F1 0.768903, recall 0.818594; versions 1 and 2 Approved; version 3 later PendingManualApproval.

## Evidence

Referenced evidence catalog: `W5-01, W5-02`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
