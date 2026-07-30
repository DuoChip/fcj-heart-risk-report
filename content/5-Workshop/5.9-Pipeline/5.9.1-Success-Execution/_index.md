---
title: "Successful execution"
weight: 1
chapter: false
pre: " <b>5.9.1.</b> "
---

# Successful Pipeline execution

The execution finished `Succeeded`: PreprocessData, TrainModel, EvaluateModel, CheckModelQuality, and RegisterModel all succeeded. The result was Model Package version 3 with `PendingManualApproval`.

```bash
aws sagemaker list-pipeline-executions   --pipeline-name "$PIPELINE_NAME" --region "$AWS_REGION"
```

`W8-01` should explain graph shape; `W8-02` overall success; `W8-03` each step; `W8-04` condition pass. The pipeline initially did not appear because it had not been upserted; run the pipeline definition/upsert before listing/executing.

**Expected:** registration occurs only after all three gates pass. Use a scoped Pipeline execution role and remember each step can incur job cost.

Next: [Intentional failure](../5.9.2-Intentional-Failure/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **sagemaker pipeline graph with pass and fail branches**.

<figure class="evidence">
  <img src="../../../images/evidence/W8-01-pipeline-graph.png" alt="SageMaker Pipeline graph with pass and fail branches" loading="lazy">
  <figcaption>SageMaker Pipeline graph with pass and fail branches — <code>W8-01-pipeline-graph.png</code></figcaption>
</figure>

**Technical meaning:** The graph makes preprocessing, training, evaluation, condition, registration, and failure dependencies explicit.

The next screenshot records **successful heart-risk-pipeline execution**.

<figure class="evidence">
  <img src="../../../images/evidence/W8-02-pipeline-success.png" alt="Successful heart-risk-pipeline execution" loading="lazy">
  <figcaption>Successful heart-risk-pipeline execution — <code>W8-02-pipeline-success.png</code></figcaption>
</figure>

**Technical meaning:** The overall Succeeded state proves the end-to-end managed workflow completed.

The next screenshot records **step-level states on the successful path**.

<figure class="evidence">
  <img src="../../../images/evidence/W8-03-success-steps.png" alt="Step-level states on the successful path" loading="lazy">
  <figcaption>Step-level states on the successful path — <code>W8-03-success-steps.png</code></figcaption>
</figure>

**Technical meaning:** Every required success-path step completed, providing finer evidence than the overall status alone.

The next screenshot records **model quality condition passed**.

<figure class="evidence">
  <img src="../../../images/evidence/W8-04-condition-pass.png" alt="Model quality condition passed" loading="lazy">
  <figcaption>Model quality condition passed — <code>W8-04-condition-pass.png</code></figcaption>
</figure>

**Technical meaning:** The condition result proves the evaluated metrics selected the RegisterModel branch.
