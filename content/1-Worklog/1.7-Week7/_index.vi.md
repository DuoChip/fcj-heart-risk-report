---
title: "Tuần 7: Triển khai mô hình, API và giám sát"
weight: 7
chapter: false
pre: " <b>1.7.</b> "
---

**Thời gian:** 27/07/2026 – 02/08/2026

## Mục tiêu và công việc hoàn thành

- Triển khai Model Package version 2 lên `heart-risk-endpoint` bằng `ml.m5.large` và bật 100% Data Capture input/output.
- Xây Lambda `heart-risk-api`, cấu hình quyền gọi endpoint tối thiểu và cung cấp `GET /health`, `POST /predict` qua API Gateway.
- Kiểm tra JSONL capture, chuẩn bị baseline/current data và hiện thực custom Processing fallback khi feature-level metric chính thức không xuất hiện.
- Publish `DriftDetected`, `DataQualityViolationCount` vào `Custom/HeartRisk` và cấu hình CloudWatch Alarm.

## Vấn đề và quyết định

- `ml.t3.medium` không được package hỗ trợ nên chuyển sang `ml.m5.large`.
- Lỗi public được chuẩn hóa để không lộ chi tiết nội bộ hay URL đang hoạt động.
- Metric batch thưa dùng `TreatMissingData=ignore` để không làm sai trạng thái alarm.

## Kết quả

Endpoint đạt `InService`; API trả đúng HTTP 200, 400 và 502. Data Capture ghi nhận traffic thật. Custom monitor phát hiện 6 feature drift, publish metric giá trị 1 và 6; alarm đạt `ALARM`.

## Minh chứng

Danh mục: `W6-01a–W6-13`, `W7-01a–W7-05`. Ảnh được trình bày và phân tích trong workshop tương ứng.

## Nhìn lại và bước tiếp theo

Kết quả triển khai và giám sát là đầu vào để tuần cuối tích hợp Pipeline, kiểm thử quality gate và hoàn thiện báo cáo.
