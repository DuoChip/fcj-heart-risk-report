---
title: "Tuần 9: Data Capture và monitoring baseline"
weight: 9
chapter: false
pre: " <b>1.9.</b> "
---

# Tuần 9: Data Capture và monitoring baseline

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Xác minh JSONL chứa input/output endpoint, metadata, inference time; chuẩn bị baseline/current và lịch Model Monitor mỗi giờ.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Thiếu metric chính thức làm cản trở cảnh báo có minh chứng.
- **Cách xử lý/quyết định:** Ghi rõ giới hạn và thiết kế custom fallback.

## Kết quả

Traffic thật đã được capture nhưng không quan sát thấy feature-level CloudWatch metric mong đợi.

## Minh chứng

Danh mục minh chứng tham chiếu: `W6-12, W6-13`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
