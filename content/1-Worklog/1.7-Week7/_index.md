---
title: "Week 7: Endpoint and direct inference"
weight: 7
chapter: false
pre: " <b>1.7.</b> "
---

# Week 7: Endpoint and direct inference

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Deployed Model Package version 2 to `heart-risk-endpoint`, enabled 100% input/output Data Capture, and invoked the endpoint directly.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** `ml.t3.medium` was unsupported by the package deployment configuration.
- **Resolution/decision:** Changed the allowed deployment instance to `ml.m5.large`.

## Result

The `ml.m5.large` endpoint reached `InService` and returned the prediction contract.

## Evidence

Referenced evidence catalog: `W6-01a, W6-01b, W6-02, W6-03`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
