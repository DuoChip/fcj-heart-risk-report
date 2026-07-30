---
title: "SageMaker endpoint"
weight: 1
chapter: false
pre: " <b>5.7.1.</b> "
---

# SageMaker real-time endpoint

Triển khai Approved Model Package version 2 thành `heart-risk-endpoint` trên một instance `ml.m5.large` và chờ `InService`.

```bash
aws sagemaker describe-endpoint   --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"   --query 'EndpointStatus'
```

Các field response kỳ vọng gồm `prediction`, `risk_probability`, `threshold`, `model_type` or `model_version`, and `disclaimer`. `W6-01a/b` cần chứng minh trạng thái/cấu hình; `W6-03` chứng minh inference trực tiếp. `ml.t3.medium` từng fail package validation và được xử lý bằng `ml.m5.large` được hỗ trợ.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

**Chi phí/bảo mật:** endpoint bị tính phí liên tục; gọi qua IAM có phạm vi và không public trực tiếp. Nếu `Failed`, đọc `FailureReason` và CloudWatch log.

Tiếp theo: [Lambda](../5.7.2-Lambda/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **endpoint thời gian thực ở trạng thái inservice**.

<figure class="evidence">
  <img src="/images/evidence/W6-01a-endpoint-inservice.png" alt="Endpoint thời gian thực ở trạng thái InService" loading="lazy">
  <figcaption>Endpoint thời gian thực ở trạng thái InService — <code>W6-01a-endpoint-inservice.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** InService chứng minh package đã duyệt sẵn sàng cho suy luận thời gian thực managed.

Ảnh tiếp theo ghi nhận **cấu hình endpoint và thông tin instance**.

<figure class="evidence">
  <img src="/images/evidence/W6-01b-endpoint-details.png" alt="Cấu hình endpoint và thông tin instance" loading="lazy">
  <figcaption>Cấu hình endpoint và thông tin instance — <code>W6-01b-endpoint-details.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Chi tiết liên kết deployment với endpoint configuration và instance ml.m5.large được hỗ trợ.

Ảnh tiếp theo ghi nhận **suy luận trực tiếp endpoint thành công**.

<figure class="evidence">
  <img src="/images/evidence/W6-03-direct-inference.png" alt="Suy luận trực tiếp endpoint thành công" loading="lazy">
  <figcaption>Suy luận trực tiếp endpoint thành công — <code>W6-03-direct-inference.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Gọi trực tiếp cô lập và xác minh contract model serving trước khi thêm Lambda và API Gateway.
