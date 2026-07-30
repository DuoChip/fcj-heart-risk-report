---
title: "Cleanup"
weight: 11
chapter: false
pre: " <b>5.11.</b> "
---

# Cleanup runbook

**Status: TODO — these commands are planned and cleanup completion is not claimed. Add deletion and stopped-application evidence after execution.**

Preserve sanitized evidence, Registry/Pipeline history, and reports until the report is finalized. Then delete in dependency order:

```bash
# 1. Monitoring and alarm
aws sagemaker delete-monitoring-schedule --monitoring-schedule-name heart-risk-monitor --region "$AWS_REGION"
aws cloudwatch delete-alarms --alarm-names heart-risk-custom-drift heart-risk-age-drift --region "$AWS_REGION"

# 2. Endpoint; deletion is asynchronous
aws sagemaker delete-endpoint --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"
aws sagemaker wait endpoint-deleted --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"

# 3. Discover exact dependent names before deleting configs/models
aws sagemaker list-endpoint-configs --name-contains heart-risk --region "$AWS_REGION"
aws sagemaker list-models --name-contains heart-risk --region "$AWS_REGION"

# 4. API and Lambda (resolve API_ID first; do not paste an active URL)
aws apigatewayv2 get-apis --region "$AWS_REGION"
aws lambda delete-function --function-name heart-risk-api --region "$AWS_REGION"
```

Delete the resolved endpoint config/model with their explicit names. Stop/delete running Studio/JupyterLab applications from **SageMaker AI → Domains → User profiles → Applications**. Pipeline deletion is optional only after history/evidence is no longer required. Keep or archive the private S3 evidence/report prefix according to retention needs.

**Errors:** endpoint config deletion fails while endpoint deletion is pending; wait and describe state. Never use broad recursive deletion or delete the bucket before verifying the exact target.

Next: [Results and limitations](../5.12-Results-Limitations/).
