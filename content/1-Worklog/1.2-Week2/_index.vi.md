---
title: "Tuần 2: Khảo sát dữ liệu và thiết kế tiền xử lý"
weight: 2
chapter: false
pre: " <b>1.2.</b> "
---

**Thời gian:** 22/06/2026 – 28/06/2026

## Mục tiêu và công việc hoàn thành

Khảo sát 7.000 dòng, 22 cột; loại `patient_id`; xác định 11 cột thiếu; thiết kế split phân tầng 70/15/15 và fit tiền xử lý chỉ trên train.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Fit phép biến đổi trước khi split có thể làm rò rỉ thông tin validation/test.
- **Cách xử lý/quyết định:** Split trước; fit median/mode imputation, one-hot encoding và scaling chỉ trên train.

## Kết quả

Tạo 36 feature sau xử lý, không có dòng trùng và không còn giá trị thiếu.

## Minh chứng

Danh mục minh chứng tham chiếu: `W2-02`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
