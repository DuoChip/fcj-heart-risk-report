---
title: "Tuần 11: SageMaker Pipeline"
weight: 11
chapter: false
pre: " <b>1.11.</b> "
---

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Xây các bước preprocessing, training, evaluation, condition, registration, fail; chạy luồng pass và fail có chủ đích.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Pipeline chưa tồn tại trước lần upsert đầu.
- **Cách xử lý/quyết định:** Chạy định nghĩa/upsert trước khi list hoặc execute.

## Kết quả

Luồng thành công đăng ký version 3 PendingManualApproval; ngưỡng AUC 0,99 chặn đăng ký theo thiết kế.

## Minh chứng

Danh mục minh chứng tham chiếu: `W8-01–W8-07`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
