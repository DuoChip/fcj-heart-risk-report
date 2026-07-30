---
title: "Tuần 6: Đánh giá cuối và Model Registry"
weight: 6
chapter: false
pre: " <b>1.6.</b> "
---

# Tuần 6: Đánh giá cuối và Model Registry

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

Đánh giá LR một lần trên test, kiểm tra ba quality gate và đăng ký package có version với phê duyệt thủ công.

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** Âm tính giả cần được giải thích rõ nhưng không đưa ra tuyên bố lâm sàng.
- **Cách xử lý/quyết định:** Báo cáo đủ 80 âm tính giả và giữ phê duyệt thủ công.

## Kết quả

AUC 0,885515, F1 0,768903, recall 0,818594; version 1 và 2 Approved; version 3 sau đó PendingManualApproval.

## Minh chứng

Danh mục minh chứng tham chiếu: `W5-01, W5-02`. Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công.
