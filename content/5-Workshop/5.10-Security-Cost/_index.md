---
title: "Security and cost"
weight: 10
chapter: false
pre: " <b>5.10.</b> "
---

## Controls implemented

- IAM roles instead of access keys; SageMaker/Lambda trust policies separated.
- SageMaker S3 access scoped to the project bucket/prefix; `iam:PassRole` limited to managed-job needs.
- Lambda restricted to `sagemaker:InvokeEndpoint` on the required endpoint.
- S3 private; no real patient/private data; public screenshots must mask account IDs, active URLs, and sensitive ARNs.
- Budget and alerts, project tags, three HPO trials, one endpoint, and job-based compute.

Expected evidence `AWS-02/03/07–14` proves budgets, tagging, role permissions/trust and scoped policies when supplied. Configuration screenshots do not prove an exact final cost, so none is claimed.

```bash
aws sagemaker list-endpoints --region "$AWS_REGION"
aws cloudwatch describe-alarms --region "$AWS_REGION"
```

The endpoint is the principal continuously billed resource; Processing/Training/HPO jobs charge while running, and S3/logs/metrics also have usage costs. Retain evidence before cleanup, then remove compute.

**Troubleshooting:** AccessDenied should be fixed by identifying the exact denied action/resource—not by adding administrator access.

Next: [Cleanup](../5.11-Cleanup/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **budget alerts configured for cost control**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-03-budget-alerts.png" alt="Budget alerts configured for cost control" loading="lazy">
  <figcaption>Budget alerts configured for cost control — <code>AWS-03-budget-alerts.png</code></figcaption>
</figure>

**Technical meaning:** Alert thresholds provide notification guardrails; they do not by themselves prove an exact final bill.

The next screenshot records **project tags applied to the s3 resource**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-07-s3-tags.png" alt="Project tags applied to the S3 resource" loading="lazy">
  <figcaption>Project tags applied to the S3 resource — <code>AWS-07-s3-tags.png</code></figcaption>
</figure>

**Technical meaning:** Tags support ownership and cost/governance identification across project resources.

The next screenshot records **sagemaker execution-role trust relationship**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-09-sagemaker-role-trust.png" alt="SageMaker execution-role trust relationship" loading="lazy">
  <figcaption>SageMaker execution-role trust relationship — <code>AWS-09-sagemaker-role-trust.png</code></figcaption>
</figure>

**Technical meaning:** The trust policy limits role assumption to the SageMaker service rather than arbitrary principals.

The next screenshot records **sagemaker role s3 access policy**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-10-sagemaker-s3-policy.png" alt="SageMaker role S3 access policy" loading="lazy">
  <figcaption>SageMaker role S3 access policy — <code>AWS-10-sagemaker-s3-policy.png</code></figcaption>
</figure>

**Technical meaning:** The policy documents the storage scope required for data, artifacts, reports, and capture.

The next screenshot records **scoped iam:passrole policy for managed jobs**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-11-sagemaker-passrole-policy.png" alt="Scoped iam:PassRole policy for managed jobs" loading="lazy">
  <figcaption>Scoped iam:PassRole policy for managed jobs — <code>AWS-11-sagemaker-passrole-policy.png</code></figcaption>
</figure>

**Technical meaning:** Scoped PassRole enables managed jobs while avoiding a broad role-passing permission.

The next screenshot records **lambda execution-role trust relationship**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-13-lambda-role-trust.png" alt="Lambda execution-role trust relationship" loading="lazy">
  <figcaption>Lambda execution-role trust relationship — <code>AWS-13-lambda-role-trust.png</code></figcaption>
</figure>

**Technical meaning:** The trust relationship establishes Lambda—not clients—as the principal assuming the wrapper role.

The next screenshot records **least-privilege lambda endpoint invocation policy**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-14-lambda-invoke-policy.png" alt="Least-privilege Lambda endpoint invocation policy" loading="lazy">
  <figcaption>Least-privilege Lambda endpoint invocation policy — <code>AWS-14-lambda-invoke-policy.png</code></figcaption>
</figure>

**Technical meaning:** The policy restricts Lambda to the required SageMaker endpoint invocation instead of general SageMaker administration.
