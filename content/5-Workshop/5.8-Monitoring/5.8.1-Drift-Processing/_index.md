---
title: "Custom drift Processing"
weight: 1
chapter: false
pre: " <b>5.8.1.</b> "
---

# Custom drift Processing

## Flow and PoC rules

Data Capture/S3 current data → custom SageMaker Processing → report → CloudWatch.

| Check | Value |
|---|---:|
| Baseline/current rows | 4,900 / 7,000 |
| Features/violations | 20 / 6 |
| Drifted | age, resting_bp, cholesterol, bmi, smoking_status, stress_level |

Numeric drift is standardized mean shift > 0.5; categorical drift is total variation distance > 0.20.

{{% notice warning %}}
These thresholds are transparent proof-of-concept rules, not clinical or universal production standards.
{{% /notice %}}

`W7-01a/b` should prove managed execution/history; `W7-02` counts; `W7-03a/b` feature results. If the capture schema cannot be flattened, inspect JSONL input/output encoding before calculating drift. Processing compute is billed per run.

Next: [CloudWatch alarm](../5.8.2-CloudWatch-Alarm/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **custom drift processing job details**.

<figure class="evidence">
  <img src="/images/evidence/W7-01a-custom-processing-job.png" alt="Custom drift Processing Job details" loading="lazy">
  <figcaption>Custom drift Processing Job details — <code>W7-01a-custom-processing-job.png</code></figcaption>
</figure>

**Technical meaning:** The job details prove the fallback drift analysis executed on managed SageMaker infrastructure.

The next screenshot records **custom drift processing job history**.

<figure class="evidence">
  <img src="/images/evidence/W7-01b-processing-job-list.png" alt="Custom drift Processing Job history" loading="lazy">
  <figcaption>Custom drift Processing Job history — <code>W7-01b-processing-job-list.png</code></figcaption>
</figure>

**Technical meaning:** The job list provides operational traceability across executions.

The next screenshot records **custom drift report summary**.

<figure class="evidence">
  <img src="/images/evidence/W7-02-drift-report.png" alt="Custom drift report summary" loading="lazy">
  <figcaption>Custom drift report summary — <code>W7-02-drift-report.png</code></figcaption>
</figure>

**Technical meaning:** The report verifies 4,900 baseline rows, 7,000 current rows, 20 checked features, and six violations.

The next screenshot records **summary of six drifted features**.

<figure class="evidence">
  <img src="/images/evidence/W7-03a-drift-features-summary.png" alt="Summary of six drifted features" loading="lazy">
  <figcaption>Summary of six drifted features — <code>W7-03a-drift-features-summary.png</code></figcaption>
</figure>

**Technical meaning:** The summary names the affected numeric and categorical features instead of reporting only a binary alarm.

The next screenshot records **feature-level custom drift details**.

<figure class="evidence">
  <img src="/images/evidence/W7-03b-drift-features-details.png" alt="Feature-level custom drift details" loading="lazy">
  <figcaption>Feature-level custom drift details — <code>W7-03b-drift-features-details.png</code></figcaption>
</figure>

**Technical meaning:** Feature-level values make the PoC threshold decision inspectable and reproducible.
