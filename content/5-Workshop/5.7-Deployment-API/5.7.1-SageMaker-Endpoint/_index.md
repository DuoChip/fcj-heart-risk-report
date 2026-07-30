---
title: "SageMaker endpoint"
weight: 1
chapter: false
pre: " <b>5.7.1.</b> "
---

# SageMaker real-time endpoint

Deploy Approved Model Package version 2 as `heart-risk-endpoint` on one `ml.m5.large` instance and wait for `InService`.

```bash
aws sagemaker describe-endpoint   --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"   --query 'EndpointStatus'
```

Expected response fields are `prediction`, `risk_probability`, `threshold`, `model_type` or `model_version`, and `disclaimer`. `W6-01a/b` should prove live state/config; `W6-03` direct inference. `ml.t3.medium` previously failed package validation, resolved with supported `ml.m5.large`.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

**Cost/security:** endpoint uptime is continuously billed; invoke through scoped IAM and do not expose it publicly. If status is `Failed`, inspect `FailureReason` and CloudWatch logs.

Next: [Lambda](../5.7.2-Lambda/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **real-time endpoint in inservice state**.

<figure class="evidence">
  <img src="../../../images/evidence/W6-01a-endpoint-inservice.png" alt="Real-time endpoint in InService state" loading="lazy">
  <figcaption>Real-time endpoint in InService state — <code>W6-01a-endpoint-inservice.png</code></figcaption>
</figure>

**Technical meaning:** InService proves the approved package is available for managed real-time invocation.

The next screenshot records **endpoint configuration and instance details**.

<figure class="evidence">
  <img src="../../../images/evidence/W6-01b-endpoint-details.png" alt="Endpoint configuration and instance details" loading="lazy">
  <figcaption>Endpoint configuration and instance details — <code>W6-01b-endpoint-details.png</code></figcaption>
</figure>

**Technical meaning:** The details connect the deployment to its endpoint configuration and supported ml.m5.large instance.

The next screenshot records **successful direct endpoint inference**.

<figure class="evidence">
  <img src="../../../images/evidence/W6-03-direct-inference.png" alt="Successful direct endpoint inference" loading="lazy">
  <figcaption>Successful direct endpoint inference — <code>W6-03-direct-inference.png</code></figcaption>
</figure>

**Technical meaning:** Direct invocation isolates and verifies the model-serving contract before Lambda and API Gateway are added.
