---
title: "Tuần 10: Custom drift fallback và CloudWatch"
weight: 10
chapter: false
pre: " <b>1.10.</b> "
---

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Chạy custom Processing Job trên 20 feature và publish `DriftDetected`, `DataQualityViolationCount` vào `Custom/HeartRisk`.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Metric batch thưa làm period thiếu ảnh hưởng trạng thái alarm.
- **Cách xử lý/quyết định:** Đặt `TreatMissingData=ignore` và publish datapoint mới.

## Kết quả

Sáu feature drift; metric bằng 1 và 6; alarm đạt `ALARM`.

## Minh chứng

Danh mục minh chứng tham chiếu: `W7-01a–W7-05`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
