---
title: "Tổng quan"
weight: 1
chapter: false
pre: " <b>5.1.</b> "
---

# Tổng quan workshop

## Mục tiêu và tiêu chí thành công

Xây luồng truy vết từ raw data có version đến API được monitor và Pipeline có quality gate. LR cuối đạt test AUC 0,885515, F1 0,768903, recall 0,818594, vượt gate 0,84/0,70/0,65.

| Thành phần | Kết quả đã xác minh |
|---|---|
| Processing | 4.900/1.050/1.050; 36 feature; không missing |
| Registry/deployment | version 2 Approved và deployed |
| API | 200, 400 và 502 có kiểm soát |
| Drift | 6/20 violation; alarm `ALARM` |
| Pipeline | success đăng ký v3 pending; fail chặn |

![Kiến trúc tách luồng offline, online, monitoring và gate](/images/architecture/heart-risk-architecture.svg)

Sơ đồ làm rõ ranh giới dịch vụ và luồng artifact lấy S3 làm trung tâm.

## Đóng góp và tùy biến cá nhân

Dự án thay use case mẫu bằng dataset riêng; thêm SHA-256/idempotent upload, train-only preprocessing, so sánh LR/XGBoost, Bayesian HPO, ba quality gate, Registry/manual approval, endpoint/Lambda/API test 200/400/502, Data Capture, custom drift/metric, xử lý sparse alarm, Pipeline pass/fail và ngôn ngữ y khoa thận trọng.

## Điều kiện, lỗi, chi phí và bước tiếp

Dùng `us-east-1`, S3 private, service role, Budget alert và không đặt credential trong code. Catalog minh chứng đã được hiển thị và diễn giải xuyên suốt workshop.

{{% notice warning %}}
Hệ thống chỉ phục vụ mục đích học tập và minh họa; không phải là chẩn đoán y khoa.
{{% /notice %}}

Tiếp theo: [Điều kiện tiên quyết](../5.2-Prerequisites/).
