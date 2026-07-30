---
title: "Week 8: Lambda and API Gateway"
weight: 8
chapter: false
pre: " <b>1.8.</b> "
---

# Week 8: Lambda and API Gateway

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Created `heart-risk-api`, configured environment variables and least-privilege endpoint invocation, then exposed `GET /health` and `POST /predict`.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** Public errors must not reveal internals or active API URLs.
- **Resolution/decision:** Validated inputs and returned safe structured errors.

## Result

Verified HTTP 200 health/prediction, 400 missing fields, and controlled 502 downstream failure.

## Evidence

Referenced evidence catalog: `W6-04–W6-11`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
