---
title: "Kết quả và giới hạn"
weight: 12
chapter: false
pre: " <b>5.12.</b> "
---

# Kết quả, giới hạn và hướng phát triển

## Kết quả

| Nhóm | Kết quả |
|---|---|
| Dữ liệu | 7.000 dòng; 20 raw/36 processed feature; fit train-only |
| Model | chọn LR; test AUC 0,885515, F1 0,768903 |
| API | health/predict và hành vi 200/400/502 |
| Drift | sáu feature; custom metric 1 và 6; alarm ALARM |
| Pipeline | pass đăng ký v3 pending; test 0,99 chặn registry |

## Vấn đề và cách xử lý

| Vấn đề | Nguyên nhân | Cách xử lý |
|---|---|---|
| Nguy cơ leakage | preprocessing trước split đúng | split trước; fit train-only |
| `ml.t3.medium` bị từ chối | instance không được package hỗ trợ | dùng `ml.m5.large` |
| Thiếu official drift metric | metric mong đợi không publish khi test | custom Processing và metric |
| Alarm OK không đúng | period thưa bị coi non-breaching | `TreatMissingData=ignore`; datapoint mới |
| Ban đầu thiếu Pipeline | chưa upsert | chạy định nghĩa/upsert trước |
| Cảnh báo SDK v2 | SageMaker SDK v2 | lên kế hoạch chuyển v3 |
| Không có alarm history | thiếu permission | dùng `describe-alarms`; tùy chọn quyền history có phạm vi |

## Đóng góp cá nhân

Dataset tùy biến và thiết kế SHA-256/idempotent upload; preprocessing chống leakage; so sánh LR/XGBoost/HPO; ba gate và promotion thủ công; API error contract; Data Capture; custom drift/CloudWatch fallback; sửa sparse metric; Pipeline pass/fail; tài liệu song ngữ có thể tái lập và disclaimer.

## Giới hạn

Dữ liệu phi lâm sàng; chưa fairness/calibration; chỉ ba HPO trial; một endpoint; chưa production authentication; drift rule PoC; không quan sát official feature metric; nợ SDK v2; chưa automated retraining, CI/CD, IaC.

## Hướng phát triển

Đánh giá fairness/calibration với governance phù hợp; thêm authentication, throttling, private networking, encryption strategy, Auto Scaling, IaC/CI/CD, SDK v3, retraining tự động có phê duyệt và minh chứng chi phí.

{{% notice warning %}}
Hệ thống chỉ phục vụ mục đích học tập và minh họa; không phải là chẩn đoán y khoa.
{{% /notice %}}
