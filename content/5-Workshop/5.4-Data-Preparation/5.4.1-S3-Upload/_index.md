---
title: "S3 upload"
weight: 1
chapter: false
pre: " <b>5.4.1.</b> "
---

# S3 upload and dataset versioning

## Objective and background

Upload the canonical 7,000-row CSV to `s3://$PROJECT_BUCKET/heart-risk/raw/heart_attack_dataset.csv`, calculate SHA-256, and store a manifest so repeated runs can detect the same content.

```bash
sha256sum heart_attack_dataset.csv
aws s3 cp heart_attack_dataset.csv   "s3://$PROJECT_BUCKET/$PREFIX/raw/heart_attack_dataset.csv"   --region "$AWS_REGION"
```

An idempotent uploader should compare the local digest with manifest/object metadata: skip identical content and require an explicit version/change path when different.

**Expected:** a private object and manifest under `heart-risk`; no public ACL. The source uploader is not present locally, so no fabricated attachment is linked.

**Errors:** `AccessDenied` means scoped IAM/bucket policy needs correction; a digest mismatch means do not silently overwrite. S3 storage/requests cost money, though usually less than always-on compute.

Next: [SageMaker Processing](../5.4.2-SageMaker-Processing/).
