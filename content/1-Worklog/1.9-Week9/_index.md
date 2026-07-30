---
title: "Week 9: Data Capture and monitoring baseline"
weight: 9
chapter: false
pre: " <b>1.9.</b> "
---

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

Verified JSONL capture records containing endpoint input/output, metadata, and inference time; prepared baseline/current data and an hourly Model Monitor schedule.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** The missing official metric prevented evidence-based alerting.
- **Resolution/decision:** Documented the limitation and designed a custom fallback.

## Result

Real traffic was captured, but the expected official feature-level CloudWatch metric was not observed.

## Evidence

Referenced evidence catalog: `W6-12, W6-13`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
