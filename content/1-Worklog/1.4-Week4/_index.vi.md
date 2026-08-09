---
title: "Tuần 4: Logistic Regression và XGBoost"
weight: 4
chapter: false
pre: " <b>1.4.</b> "
---

**Thời gian:** 06/07/2026 – 12/07/2026

## Mục tiêu và công việc hoàn thành

Chạy managed training job cho Logistic Regression và XGBoost mặc định, sau đó so sánh trên validation.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Một metric không diễn tả đủ đánh đổi lỗi.
- **Cách xử lý/quyết định:** So sánh AUC, F1, recall, precision và threshold 0,36 của LR.

## Kết quả

LR AUC 0,863949; XGBoost AUC 0,854283. XGBoost có recall cao hơn nhưng precision và AUC thấp hơn.

## Minh chứng

Danh mục minh chứng tham chiếu: `W3-01–W3-04`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
