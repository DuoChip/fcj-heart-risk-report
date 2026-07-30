---
title: "Tuần 3: SageMaker Processing Job"
weight: 3
chapter: false
pre: " <b>1.3.</b> "
---

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Tải dữ liệu raw và manifest lên S3, chạy managed preprocessing và lưu train, validation, test, baseline, report, artifact.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Output cần đường dẫn ổn định và khả năng chạy lặp.
- **Cách xử lý/quyết định:** Dùng bố cục S3-first và artifact tiền xử lý tái sử dụng.

## Kết quả

Managed preprocessing hoàn tất với kích thước 4.900/1.050/1.050.

## Minh chứng

Danh mục minh chứng tham chiếu: `W2-01, W2-03`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
