---
title: "Cleanup"
weight: 11
chapter: false
pre: " <b>5.11.</b> "
---

# Runbook cleanup

**Trạng thái: TODO — đây là lệnh dự kiến và chưa tuyên bố cleanup hoàn tất. Thêm minh chứng xóa tài nguyên và dừng ứng dụng sau khi chạy.**

Giữ minh chứng đã che thông tin, history Registry/Pipeline và report đến khi báo cáo hoàn tất. Sau đó xóa theo thứ tự phụ thuộc:

```bash
# 1. Monitoring and alarm
aws sagemaker delete-monitoring-schedule --monitoring-schedule-name heart-risk-monitor --region "$AWS_REGION"
aws cloudwatch delete-alarms --alarm-names heart-risk-custom-drift heart-risk-age-drift --region "$AWS_REGION"

# 2. Endpoint; deletion is asynchronous
aws sagemaker delete-endpoint --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"
aws sagemaker wait endpoint-deleted --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"

# 3. Discover exact dependent names before deleting configs/models
aws sagemaker list-endpoint-configs --name-contains heart-risk --region "$AWS_REGION"
aws sagemaker list-models --name-contains heart-risk --region "$AWS_REGION"

# 4. API and Lambda (resolve API_ID first; do not paste an active URL)
aws apigatewayv2 get-apis --region "$AWS_REGION"
aws lambda delete-function --function-name heart-risk-api --region "$AWS_REGION"
```

Xóa endpoint config/model đã resolve bằng tên cụ thể. Dừng/xóa Studio/JupyterLab application đang chạy tại **SageMaker AI → Domains → User profiles → Applications**. Chỉ tùy chọn xóa Pipeline sau khi không cần history/minh chứng. Giữ hoặc archive prefix S3 private theo yêu cầu retention.

**Lỗi:** xóa endpoint config thất bại khi endpoint còn đang xóa; hãy chờ và kiểm tra trạng thái. Không xóa recursive phạm vi rộng hoặc xóa bucket trước khi xác minh target.

Tiếp theo: [Kết quả và giới hạn](../5.12-Results-Limitations/).
