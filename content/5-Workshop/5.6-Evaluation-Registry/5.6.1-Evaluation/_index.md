---
title: "Final evaluation"
weight: 1
chapter: false
pre: " <b>5.6.1.</b> "
---

# Final evaluation

| Metric | Value |
|---|---:|
| ROC-AUC | 0.885515 |
| Accuracy | 0.793333 |
| Precision | 0.724900 |
| Recall | 0.818594 |
| F1 | 0.768903 |
| False Negative Rate | 0.181406 |

| | Predicted negative | Predicted positive |
|---|---:|---:|
| Actual negative | TN 472 | FP 137 |
| Actual positive | FN 80 | TP 361 |

The model passes AUC ≥ 0.84, F1 ≥ 0.70, and recall ≥ 0.65. The 80 false negatives are positive labels missed by this evaluated model; this is a material limitation, not evidence of clinical safety. `W5-02` should substantiate the metrics/confusion matrix when supplied.

**Troubleshooting:** do not tune after viewing test results. A mismatch often means a different threshold or preprocessing artifact. Evaluation jobs have storage/compute cost; protect test data and reports.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

Next: [Model Registry](../5.6.2-Model-Registry/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **final test metrics and confusion matrix**.

<figure class="evidence">
  <img src="/images/evidence/W5-02-evaluation-metrics-and-confusion-matrix.png" alt="Final test metrics and confusion matrix" loading="lazy">
  <figcaption>Final test metrics and confusion matrix — <code>W5-02-evaluation-metrics-and-confusion-matrix.png</code></figcaption>
</figure>

**Technical meaning:** The evidence proves all three quality gates passed while making the 80 false negatives explicit.
