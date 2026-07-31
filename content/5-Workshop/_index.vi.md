---
title: "Workshop Heart Risk MLOps"
weight: 5
chapter: false
pre: " <b>5.</b> "
---

# Xây dựng và triển khai hệ thống dự đoán nguy cơ đau tim end-to-end trên AWS SageMaker

Workshop xây dựng proof of concept MLOps có thể tái lập cho phân loại nguy cơ đau tim: chuẩn bị dữ liệu, so sánh model, quality gate, đăng ký/phê duyệt, endpoint, API, capture traffic, phát hiện drift, cảnh báo và SageMaker Pipelines.

**Đối tượng:** người học biết Python, AWS cơ bản và bài toán phân loại.  
**Thời lượng:** khoảng 8–12 giờ thực hành, không gồm thời gian chờ job.  
**Dịch vụ:** S3, SageMaker Processing/Training/HPO/Registry/Endpoint/Model Monitor/Pipelines, Lambda, API Gateway, CloudWatch, IAM, Budgets.

{{% notice warning %}}
Tài nguyên AWS có thể phát sinh phí, đặc biệt endpoint chạy liên tục. Hãy dùng Budget alert và hoàn tất runbook cleanup.
{{% /notice %}}

{{% notice warning %}}
Hệ thống chỉ phục vụ mục đích học tập và minh họa; không phải là chẩn đoán y khoa.
{{% /notice %}}

![Sơ đồ kiến trúc Heart Risk MLOps do sinh viên tự vẽ](../../images/architecture/heart-risk-architecture.jpg)

## Mục tiêu học tập và điều hướng

1. [Tổng quan](5.1-Overview/)
2. [Điều kiện tiên quyết](5.2-Prerequisites/)
3. [Kiến trúc](5.3-Architecture/)
4. [Chuẩn bị dữ liệu](5.4-Data-Preparation/)
5. [Huấn luyện mô hình](5.5-Model-Training/)
6. [Đánh giá và Registry](5.6-Evaluation-Registry/)
7. [Triển khai và API](5.7-Deployment-API/)
8. [Monitoring](5.8-Monitoring/)
9. [Pipeline](5.9-Pipeline/)
10. [Bảo mật và chi phí](5.10-Security-Cost/)
11. [Cleanup](5.11-Cleanup/)
12. [Kết quả và giới hạn](5.12-Results-Limitations/)
