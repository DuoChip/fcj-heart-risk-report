---
title: "Tuần 8: Lambda và API Gateway"
weight: 8
chapter: false
pre: " <b>1.8.</b> "
---

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Tạo `heart-risk-api`, cấu hình biến môi trường và quyền gọi endpoint tối thiểu, sau đó cung cấp `GET /health`, `POST /predict`.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Lỗi public không được lộ nội bộ hoặc URL API đang hoạt động.
- **Cách xử lý/quyết định:** Validate input và trả lỗi có cấu trúc an toàn.

## Kết quả

Xác minh HTTP 200 health/prediction, 400 thiếu field và 502 có kiểm soát khi downstream lỗi.

## Minh chứng

Danh mục minh chứng tham chiếu: `W6-04–W6-11`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
