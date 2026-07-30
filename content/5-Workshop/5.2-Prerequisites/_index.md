---
title: "Prerequisites"
weight: 2
chapter: false
pre: " <b>5.2.</b> "
---

## Objective

Prepare a controlled environment before creating billed resources.

1. Use an AWS account and select `us-east-1`.
2. Install Git, Python 3, AWS CLI v2, and Hugo extended 0.134.3 or compatible.
3. Configure SageMaker Studio/JupyterLab without embedding access keys.
4. Create the private bucket and SageMaker/Lambda execution roles.
5. Configure AWS Budget alerts.

```bash
export AWS_REGION="us-east-1"
export PROJECT_BUCKET="heart-risk-mlops-<ACCOUNT_ID>-us-east-1-fcaj"
export PREFIX="heart-risk"
export ENDPOINT_NAME="heart-risk-endpoint"
export PIPELINE_NAME="heart-risk-pipeline"
aws sts get-caller-identity
aws s3api head-bucket --bucket "$PROJECT_BUCKET"
```

**Expected:** identity succeeds and the bucket is reachable by the authorized principal. An access-denied response means the role/bucket policy or Region must be checked; never “fix” it with public access.

Evidence expected: `AWS-01`, `AWS-02`, `AWS-08`, `AWS-12`. The supplied screenshots prove the selected Region, budget guardrail, and separate execution-role setup.

**Cost/security:** enable alerts before jobs; keep Block Public Access enabled; use roles and least privilege.

Next: [Architecture](../5.3-Architecture/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **the project consistently uses the us-east-1 region**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-01-selected-region.png" alt="The project consistently uses the us-east-1 Region" loading="lazy">
  <figcaption>The project consistently uses the us-east-1 Region — <code>AWS-01-selected-region.png</code></figcaption>
</figure>

**Technical meaning:** The selected Region matches every resource name and command used later in the workshop.

The next screenshot records **project aws budget overview**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-02-budget-overview.png" alt="Project AWS Budget overview" loading="lazy">
  <figcaption>Project AWS Budget overview — <code>AWS-02-budget-overview.png</code></figcaption>
</figure>

**Technical meaning:** The budget is a cost guardrail configured before managed jobs and the continuously billed endpoint.

The next screenshot records **main permissions of the sagemaker execution role**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-08-sagemaker-role-permissions.png" alt="Main permissions of the SageMaker execution role" loading="lazy">
  <figcaption>Main permissions of the SageMaker execution role — <code>AWS-08-sagemaker-role-permissions.png</code></figcaption>
</figure>

**Technical meaning:** The execution role supplies managed jobs with AWS permissions without credentials in notebooks.

The next screenshot records **lambda execution-role permissions**.

<figure class="evidence">
  <img src="../../images/evidence/AWS-12-lambda-role-permissions.png" alt="Lambda execution-role permissions" loading="lazy">
  <figcaption>Lambda execution-role permissions — <code>AWS-12-lambda-role-permissions.png</code></figcaption>
</figure>

**Technical meaning:** A separate Lambda role keeps API-wrapper permissions independent from SageMaker training permissions.
