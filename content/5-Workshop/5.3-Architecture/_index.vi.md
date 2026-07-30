---
title: "Kiến trúc"
weight: 3
chapter: false
pre: " <b>5.3.</b> "
---

## Mục tiêu và luồng

![Kiến trúc AWS Heart-risk](../../../images/architecture/heart-risk-architecture.svg)

**Offline:** raw S3 → Processing → split/artifact → Training/HPO → Evaluation → Registry.  
**Online:** API Gateway → Lambda validate → endpoint → response; Data Capture ghi JSONL vào S3.  
**Monitoring:** capture/baseline → custom Processing → report → custom metric → alarm.  
**Pipeline:** condition kiểm tra AUC/F1/recall; pass đăng ký, fail tạo `MetricThresholdFailed`.

| Đã hiện thực trong PoC | Khuyến nghị production |
|---|---|
| Một endpoint instance | Auto Scaling và thiết kế vận hành multi-AZ |
| HTTP integration chưa có production auth | Cognito/API key/WAF và throttling |
| Service IAM role, S3 private | VPC-only và chiến lược KMS key |
| Script thủ công và Pipeline | IaC, CI/CD, automated retraining có phê duyệt |

SVG là sơ đồ tài liệu gốc, không phải minh chứng trạng thái tài nguyên. Cần kiểm tra trạng thái thật bằng console/CLI và ảnh đã che thông tin.

**Xử lý lỗi:** nếu artifact path không khớp, kiểm tra S3 URI và Pipeline property thay vì copy thủ công. Dịch vụ phát sinh phí theo Region.

{{% notice warning %}}
Hệ thống chỉ phục vụ mục đích học tập và minh họa; không phải là chẩn đoán y khoa.
{{% /notice %}}

Tiếp theo: [Chuẩn bị dữ liệu](../5.4-Data-Preparation/).
