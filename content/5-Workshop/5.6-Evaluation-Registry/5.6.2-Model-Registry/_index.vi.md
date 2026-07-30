---
title: "Model Registry"
weight: 2
chapter: false
pre: " <b>5.6.2.</b> "
---

# Model Registry

## Mục tiêu và trạng thái

Dùng `heart-attack-risk-models` để truy vết và có quyết định promotion của con người.

| Version | State | Ý nghĩa |
|---:|---|---|
| 1 | Approved | version được duyệt và giữ lại |
| 2 | Approved | nguồn triển khai cho `heart-risk-endpoint` |
| 3 | PendingManualApproval | được Pipeline thành công tạo |

```bash
aws sagemaker list-model-packages   --model-package-group-name heart-attack-risk-models   --region "$AWS_REGION"
```

`W5-01` cần chứng minh trạng thái khi được cung cấp. Phê duyệt thủ công ngăn artifact được deploy chỉ vì training hoàn tất.

**Lỗi:** package từ chối `ml.t3.medium` cần deployment config được hỗ trợ; dự án dùng `ml.m5.large`. Tránh public ARN chứa account đầy đủ.

Tiếp theo: [Triển khai và API](../../5.7-Deployment-API/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **các version và trạng thái phê duyệt trong model registry**.

<figure class="evidence">
  <img src="/images/evidence/W5-01-model-versions.png" alt="Các version và trạng thái phê duyệt trong Model Registry" loading="lazy">
  <figcaption>Các version và trạng thái phê duyệt trong Model Registry — <code>W5-01-model-versions.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Danh sách phân biệt version 1–2 Approved với version 3 PendingManualApproval do Pipeline tạo.
