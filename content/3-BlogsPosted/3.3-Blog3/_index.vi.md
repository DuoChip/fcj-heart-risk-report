---
title: "Giám sát Data Drift tùy chỉnh bằng SageMaker Processing và CloudWatch"
weight: 3
chapter: false
pre: " <b>3.3.</b> "
---

# Giám sát Data Drift tùy chỉnh bằng SageMaker Processing và CloudWatch

## Giới thiệu và động lực

Data Capture cung cấp record suy luận hiện tại, còn baseline 4.900 dòng từ train làm mốc. Không quan sát thấy official feature metric nên dự án tạo fallback minh bạch.

## Luồng và hiện thực

Custom Processing Job kiểm tra 20 feature: standardized mean shift numeric > 0,5 và total variation distance categorical > 0,20. Sáu feature drift. Job publish `DriftDetected=1`, `DataQualityViolationCount=6`; `TreatMissingData=ignore` tránh period batch thưa làm sai trạng thái hữu ích. Đây là quy tắc PoC, không phải ngưỡng phổ quát hay lâm sàng.

## Kết quả và bài học

Giải pháp ưu tiên minh chứng đo được, hành vi lỗi rõ ràng và vận hành có ý thức chi phí. IAM role thay access key hard-code; cần che URL đang active và ARN nhạy cảm.

## Trạng thái xuất bản

- TODO: URL bài AWS Study Group
- TODO: Ngày xuất bản
- TODO: Ảnh minh chứng xuất bản
