---
title: "Tuần 5: HPO và lựa chọn mô hình"
weight: 5
chapter: false
pre: " <b>1.5.</b> "
---

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Chạy ba trial Bayesian HPO tuần tự cho `eta`, `max-depth`, `min-child-weight`; tối ưu `validation:auc`.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Test set không được ảnh hưởng lựa chọn model hoặc trial.
- **Cách xử lý/quyết định:** Chỉ chọn theo validation và dành test cho một lần đánh giá cuối.

## Kết quả

HPO AUC tốt nhất là 0,860982; LR vẫn là ứng viên theo validation AUC.

## Minh chứng

Không có ảnh HPO riêng; cấu hình và metric so sánh được trình bày mà không tạo link ảnh hỏng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
