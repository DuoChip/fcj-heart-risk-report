---
title: "Logistic Regression"
weight: 1
chapter: false
pre: " <b>5.5.1.</b> "
---

# Logistic Regression

## Objective and rationale

Train an interpretable linear baseline as a managed job, independent of the notebook session.

```text
validation ROC-AUC = 0.863949
F1 = 0.747583; recall = 0.789116; precision = 0.710204
decision threshold = 0.36
```

`W3-01` should prove job status/configuration and `W3-02` the validation metrics; the supplied screenshots substantiate both results. Threshold 0.36 is part of this evaluated artifact, not a medical cutoff.

**Expected:** model artifact in S3 and metrics recorded for comparison. If metric parsing is empty, verify log regex/channel names. Training jobs incur instance-time cost and the role should only reach required S3 prefixes.

Next: [XGBoost](../5.5.2-XGBoost/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **managed logistic regression training job**.

<figure class="evidence">
  <img src="/images/evidence/W3-01-lr-training.png" alt="Managed Logistic Regression training job" loading="lazy">
  <figcaption>Managed Logistic Regression training job — <code>W3-01-lr-training.png</code></figcaption>
</figure>

**Technical meaning:** The job state and configuration establish an auditable managed training run.

The next screenshot records **logistic regression validation metrics**.

<figure class="evidence">
  <img src="/images/evidence/W3-02-lr-metrics.png" alt="Logistic Regression validation metrics" loading="lazy">
  <figcaption>Logistic Regression validation metrics — <code>W3-02-lr-metrics.png</code></figcaption>
</figure>

**Technical meaning:** These metrics support the final choice by validation AUC and preserve the evaluated threshold of 0.36.
