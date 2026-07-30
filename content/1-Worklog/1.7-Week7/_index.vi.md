---
title: "Tuần 7: Endpoint và suy luận trực tiếp"
weight: 7
chapter: false
pre: " <b>1.7.</b> "
---

# Tuần 7: Endpoint và suy luận trực tiếp

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Triển khai Model Package version 2 lên `heart-risk-endpoint`, bật 100% Data Capture input/output và gọi endpoint trực tiếp.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** `ml.t3.medium` không được cấu hình package hỗ trợ.
- **Cách xử lý/quyết định:** Đổi instance triển khai được phép sang `ml.m5.large`.

## Kết quả

Endpoint `ml.m5.large` đạt `InService` và trả đúng contract dự đoán.

## Minh chứng

Danh mục minh chứng tham chiếu: `W6-01a, W6-01b, W6-02, W6-03`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
