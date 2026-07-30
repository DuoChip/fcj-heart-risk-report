---
title: "Tối ưu chi phí cho dự án MLOps cá nhân trên SageMaker"
weight: 1
chapter: false
pre: " <b>3.1.</b> "
---

## Giới thiệu và động lực

Endpoint chạy liên tục khác với Processing/Training Job kết thúc sau công việc. PoC vì vậy giới hạn ba HPO trial tuần tự, một endpoint, Budget alert, tags và runbook cleanup.

## Luồng và hiện thực

Liệt kê endpoint đang chạy trước khi xóa:

```bash
aws sagemaker list-endpoints --region "$AWS_REGION" --status-equals InService
```

Giữ report và minh chứng đã che thông tin trước khi xóa compute. Giữ S3 private và không nhúng credential.

## Kết quả và bài học

Giải pháp ưu tiên minh chứng đo được, hành vi lỗi rõ ràng và vận hành có ý thức chi phí. IAM role thay access key hard-code; cần che URL đang active và ARN nhạy cảm.

## Trạng thái xuất bản

- TODO: URL bài AWS Study Group
- TODO: Ngày xuất bản
- TODO: Ảnh minh chứng xuất bản
