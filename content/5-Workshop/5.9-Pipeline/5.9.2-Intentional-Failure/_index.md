---
title: "Intentional failure"
weight: 2
chapter: false
pre: " <b>5.9.2.</b> "
---

# Intentional Pipeline failure

Override `AucThreshold=0.99`, above the evaluated 0.885515 result. The final execution is `Failed` **by design**, `MetricThresholdFailed` executes, and RegisterModel does not.

```bash
aws sagemaker start-pipeline-execution   --pipeline-name "$PIPELINE_NAME"   --pipeline-parameters Name=AucThreshold,Value=0.99   --region "$AWS_REGION"
```

`W8-05` should prove failed execution, `W8-06` the 0.99 parameter, and `W8-07` the fail step. Together they prove a low-quality candidate cannot silently enter the registry.

**Troubleshooting:** do not “fix” this expected test by lowering the gate mid-execution. Distinguish condition failure from infrastructure failure in step metadata/logs.

Next: [Security and cost](../../5.10-Security-Cost/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **pipeline execution failed by design**.

<figure class="evidence">
  <img src="../../../images/evidence/W8-05-pipeline-failure.png" alt="Pipeline execution failed by design" loading="lazy">
  <figcaption>Pipeline execution failed by design — <code>W8-05-pipeline-failure.png</code></figcaption>
</figure>

**Technical meaning:** The failure state is evidence of the tested guardrail, not an implementation defect.

The next screenshot records **intentional aucthreshold override of 0.99**.

<figure class="evidence">
  <img src="../../../images/evidence/W8-06-failure-parameters.png" alt="Intentional AucThreshold override of 0.99" loading="lazy">
  <figcaption>Intentional AucThreshold override of 0.99 — <code>W8-06-failure-parameters.png</code></figcaption>
</figure>

**Technical meaning:** The parameter proves the deliberately unreachable test gate that triggered the failure branch.

The next screenshot records **metricthresholdfailed step blocked registration**.

<figure class="evidence">
  <img src="../../../images/evidence/W8-07-fail-step.png" alt="MetricThresholdFailed step blocked registration" loading="lazy">
  <figcaption>MetricThresholdFailed step blocked registration — <code>W8-07-fail-step.png</code></figcaption>
</figure>

**Technical meaning:** The executed fail step proves a candidate below the gate cannot enter Model Registry.
