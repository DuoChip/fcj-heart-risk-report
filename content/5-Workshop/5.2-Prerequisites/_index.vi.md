---
title: "Điều kiện tiên quyết"
weight: 2
chapter: false
pre: " <b>5.2.</b> "
---

# Điều kiện tiên quyết

## Mục tiêu

Chuẩn bị môi trường có kiểm soát trước khi tạo tài nguyên tính phí.

1. Dùng AWS account và chọn `us-east-1`.
2. Cài Git, Python 3, AWS CLI v2, Hugo extended 0.134.3 hoặc tương thích.
3. Cấu hình SageMaker Studio/JupyterLab không nhúng access key.
4. Tạo bucket private và execution role SageMaker/Lambda.
5. Cấu hình AWS Budget alert.

```bash
export AWS_REGION="us-east-1"
export PROJECT_BUCKET="heart-risk-mlops-<ACCOUNT_ID>-us-east-1-fcaj"
export PREFIX="heart-risk"
export ENDPOINT_NAME="heart-risk-endpoint"
export PIPELINE_NAME="heart-risk-pipeline"
aws sts get-caller-identity
aws s3api head-bucket --bucket "$PROJECT_BUCKET"
```

**Kỳ vọng:** nhận diện identity thành công và principal được phép truy cập bucket. Nếu access denied, kiểm tra role/bucket policy hoặc Region; không bật public để “sửa”.

Minh chứng cần có: `AWS-01`, `AWS-02`, `AWS-08`, `AWS-12`. Các ảnh được cung cấp chứng minh Region, budget guardrail và execution role riêng.

**Chi phí/bảo mật:** bật alert trước khi chạy job; giữ Block Public Access; dùng role và đặc quyền tối thiểu.

Tiếp theo: [Kiến trúc](../5.3-Architecture/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **dự án sử dụng thống nhất region us-east-1**.

<figure class="evidence">
  <img src="/images/evidence/AWS-01-selected-region.png" alt="Dự án sử dụng thống nhất Region us-east-1" loading="lazy">
  <figcaption>Dự án sử dụng thống nhất Region us-east-1 — <code>AWS-01-selected-region.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Region được chọn khớp với tên tài nguyên và lệnh ở các bước sau.

Ảnh tiếp theo ghi nhận **tổng quan aws budget của dự án**.

<figure class="evidence">
  <img src="/images/evidence/AWS-02-budget-overview.png" alt="Tổng quan AWS Budget của dự án" loading="lazy">
  <figcaption>Tổng quan AWS Budget của dự án — <code>AWS-02-budget-overview.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Budget là guardrail chi phí được cấu hình trước managed job và endpoint tính phí liên tục.

Ảnh tiếp theo ghi nhận **các quyền chính của sagemaker execution role**.

<figure class="evidence">
  <img src="/images/evidence/AWS-08-sagemaker-role-permissions.png" alt="Các quyền chính của SageMaker execution role" loading="lazy">
  <figcaption>Các quyền chính của SageMaker execution role — <code>AWS-08-sagemaker-role-permissions.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Execution role cấp quyền cho managed job mà không đặt credential trong notebook.

Ảnh tiếp theo ghi nhận **các quyền của lambda execution role**.

<figure class="evidence">
  <img src="/images/evidence/AWS-12-lambda-role-permissions.png" alt="Các quyền của Lambda execution role" loading="lazy">
  <figcaption>Các quyền của Lambda execution role — <code>AWS-12-lambda-role-permissions.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Role Lambda riêng tách quyền API wrapper khỏi quyền huấn luyện SageMaker.
