---
title: "XGBoost"
weight: 2
chapter: false
pre: " <b>5.5.2.</b> "
---

# XGBoost

## Objective and comparison

Test a tree-based model that can learn nonlinear interactions.

| Model | AUC | F1 | Recall | Precision |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.863949 | 0.747583 | 0.789116 | 0.710204 |
| XGBoost default | 0.854283 | 0.749749 | 0.845805 | 0.673285 |

XGBoost improved recall but reduced precision and the primary selection metric, AUC. `W3-03` should prove the managed job and `W3-04` its metrics; the supplied screenshots substantiate both results.

**Expected:** an independently versioned artifact, not an overwrite of LR. If XGBoost input format fails, verify label position/content type. Limit job size and delete transient artifacts only after evidence is retained.

Next: [HPO](../5.5.3-HPO/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **managed xgboost training job**.

<figure class="evidence">
  <img src="/images/evidence/W3-03-xgb-training.png" alt="Managed XGBoost training job" loading="lazy">
  <figcaption>Managed XGBoost training job — <code>W3-03-xgb-training.png</code></figcaption>
</figure>

**Technical meaning:** A separate job proves the second algorithm was trained as an independent candidate.

The next screenshot records **default xgboost validation metrics**.

<figure class="evidence">
  <img src="/images/evidence/W3-04-xgb-metrics.png" alt="Default XGBoost validation metrics" loading="lazy">
  <figcaption>Default XGBoost validation metrics — <code>W3-04-xgb-metrics.png</code></figcaption>
</figure>

**Technical meaning:** The result documents higher recall but lower precision and ROC-AUC than Logistic Regression.
