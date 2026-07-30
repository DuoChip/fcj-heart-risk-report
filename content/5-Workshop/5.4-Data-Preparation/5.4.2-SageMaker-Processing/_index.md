---
title: "SageMaker Processing"
weight: 2
chapter: false
pre: " <b>5.4.2.</b> "
---

# SageMaker Processing

## Objective

Create reproducible train/validation/test data without leakage.

```python
# Pseudocode: split before fitting transformations
train, temp = stratified_split(raw, train_size=0.70, target="heart_attack_risk")
validation, test = stratified_split(temp, train_size=0.50, target="heart_attack_risk")
preprocessor.fit(train[feature_columns])  # fit_scope = "train_only"
```

Numeric missing values use median imputation and scaling; categorical values use most-frequent imputation and one-hot encoding. `patient_id` is excluded.

| Check | Expected |
|---|---:|
| Split rows | 4,900 / 1,050 / 1,050 |
| Raw/processed features | 20 / 36 |
| Missing after processing | 0 |
| Fit scope | `train_only` |

Evidence slots `W2-01`, `W2-02`, `W2-03` respectively prove managed completion, logged quality checks, and persisted S3 outputs. The image files must be added before publication.

**Troubleshooting:** feature-count mismatch usually means category vocabulary or excluded columns changed. Never refit on validation/test. Stop failed jobs and inspect CloudWatch logs to control cost.

Next: [Model training](../../5.5-Model-Training/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **managed sagemaker processing job completed**.

<figure class="evidence">
  <img src="/images/evidence/W2-01-processing-completed.png" alt="Managed SageMaker Processing Job completed" loading="lazy">
  <figcaption>Managed SageMaker Processing Job completed — <code>W2-01-processing-completed.png</code></figcaption>
</figure>

**Technical meaning:** The completed state proves preprocessing ran on managed infrastructure rather than only in a local notebook.

The next screenshot records **processing log with split and data-quality checks**.

<figure class="evidence">
  <img src="/images/evidence/W2-02-processing-log.png" alt="Processing log with split and data-quality checks" loading="lazy">
  <figcaption>Processing log with split and data-quality checks — <code>W2-02-processing-log.png</code></figcaption>
</figure>

**Technical meaning:** The log verifies 4,900/1,050/1,050 rows, 36 processed features, zero remaining missing values, and train-only fit.

The next screenshot records **processed datasets and artifacts persisted in amazon s3**.

<figure class="evidence">
  <img src="/images/evidence/W2-03-processed-s3.png" alt="Processed datasets and artifacts persisted in Amazon S3" loading="lazy">
  <figcaption>Processed datasets and artifacts persisted in Amazon S3 — <code>W2-03-processed-s3.png</code></figcaption>
</figure>

**Technical meaning:** Persisted outputs make later training and evaluation reproducible and independent of notebook memory.
