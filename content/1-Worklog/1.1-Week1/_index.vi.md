---
title: "Tuần 1: Nền tảng AWS và lập kế hoạch"
weight: 1
chapter: false
pre: " <b>1.1.</b> "
---

# Tuần 1: Nền tảng AWS và lập kế hoạch

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Đọc yêu cầu FCAJ; chọn bài toán heart-risk MLOps và `us-east-1`; cấu hình Budget alert, IAM role, S3 private và tags.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Phạm vi IAM và chi phí dịch vụ managed ngoài dự kiến là rủi ro chính.
- **Cách xử lý/quyết định:** Dùng trust policy theo dịch vụ, quyền có phạm vi, tags và thông báo ngân sách.

## Kết quả

Môi trường AWS và guardrail chi phí sẵn sàng; role cho SageMaker và Lambda đã được chuẩn bị.

## Minh chứng

Danh mục minh chứng tham chiếu: `AWS-01, AWS-02, AWS-03, AWS-07–AWS-11`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
