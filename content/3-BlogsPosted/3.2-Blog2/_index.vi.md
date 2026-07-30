---
title: "Model Registry và Quality Gate trong SageMaker Pipeline"
weight: 2
chapter: false
pre: " <b>3.2.</b> "
---

# Model Registry và Quality Gate trong SageMaker Pipeline

## Giới thiệu và động lực

Model version tách artifact đã train khỏi quyết định promotion. Version 1 và 2 Approved; version 2 được deploy; Pipeline tạo version 3 PendingManualApproval.

## Luồng và hiện thực

`ConditionStep` kiểm tra AUC ≥ 0,84, F1 ≥ 0,70 và recall ≥ 0,65. Nhánh pass đăng ký; nhánh fail tạo `MetricThresholdFailed`. Ngưỡng AUC 0,99 có chủ đích xác minh việc chặn đăng ký. Không auto-deploy để người phụ trách rà soát minh chứng và chi phí.

## Kết quả và bài học

Giải pháp ưu tiên minh chứng đo được, hành vi lỗi rõ ràng và vận hành có ý thức chi phí. IAM role thay access key hard-code; cần che URL đang active và ARN nhạy cảm.

## Trạng thái xuất bản

- TODO: URL bài AWS Study Group
- TODO: Ngày xuất bản
- TODO: Ảnh minh chứng xuất bản
