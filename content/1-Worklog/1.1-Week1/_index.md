---
title: "Week 1: AWS foundation and project planning"
weight: 1
chapter: false
pre: " <b>1.1.</b> "
---

**Dates:** 15 June 2026 – 21 June 2026

## Objectives and work completed

Reviewed FCAJ requirements; selected the heart-risk MLOps use case and `us-east-1`; configured Budget alerts, IAM roles, private S3 storage, and tags.

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** IAM scope and unexpected managed-service cost were the main risks.
- **Resolution/decision:** Used service trust policies, scoped permissions, tags, and budget notifications.

## Result

AWS environment and cost guardrails were ready; SageMaker and Lambda roles were prepared.

## Evidence

Referenced evidence catalog: `AWS-01, AWS-02, AWS-03, AWS-07–AWS-11`. The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state.
