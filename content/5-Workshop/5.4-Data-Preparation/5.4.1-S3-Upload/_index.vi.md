---
title: "Upload S3"
weight: 1
chapter: false
pre: " <b>5.4.1.</b> "
---

# Upload S3 và version dữ liệu

## Mục tiêu và khái niệm

Upload CSV 7.000 dòng chuẩn lên `s3://$PROJECT_BUCKET/heart-risk/raw/heart_attack_dataset.csv`, calculate SHA-256, and store a manifest so repeated runs can detect the same content.

```bash
sha256sum heart_attack_dataset.csv
aws s3 cp heart_attack_dataset.csv   "s3://$PROJECT_BUCKET/$PREFIX/raw/heart_attack_dataset.csv"   --region "$AWS_REGION"
```

Uploader idempotent cần so digest local với manifest/object metadata: bỏ qua nội dung giống nhau và yêu cầu version/change path rõ ràng nếu khác.

**Kỳ vọng:** object private và manifest dưới `heart-risk`; không có public ACL. Source uploader không có trong workspace nên không tạo link attachment giả.

**Lỗi:** `AccessDenied` yêu cầu sửa IAM/bucket policy đúng phạm vi; digest mismatch không được overwrite âm thầm. S3 storage/request có phí nhưng thường thấp hơn compute chạy liên tục.

Tiếp theo: [SageMaker Processing](../5.4.2-SageMaker-Processing/).
