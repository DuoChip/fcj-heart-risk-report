---
title: "Execution thành công"
weight: 1
chapter: false
pre: " <b>5.9.1.</b> "
---

# Successful Pipeline execution

Execution kết thúc `Succeeded`: PreprocessData, TrainModel, EvaluateModel, CheckModelQuality, and RegisterModel đều thành công. Kết quả là Model Package version 3 với `PendingManualApproval`.

```bash
aws sagemaker list-pipeline-executions   --pipeline-name "$PIPELINE_NAME" --region "$AWS_REGION"
```

`W8-01` cần giải thích graph; `W8-02` chứng minh trạng thái tổng; `W8-03` từng step; `W8-04` condition pass. Pipeline ban đầu chưa xuất hiện vì chưa upsert; chạy định nghĩa/upsert trước khi list/execute.

**Kỳ vọng:** chỉ đăng ký sau khi ba gate pass. Dùng Pipeline execution role có phạm vi; mỗi step có thể phát sinh phí job.

Tiếp theo: [Thất bại có chủ đích](../5.9.2-Intentional-Failure/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **graph sagemaker pipeline với nhánh pass và fail**.

<figure class="evidence">
  <img src="/images/evidence/W8-01-pipeline-graph.png" alt="Graph SageMaker Pipeline với nhánh pass và fail" loading="lazy">
  <figcaption>Graph SageMaker Pipeline với nhánh pass và fail — <code>W8-01-pipeline-graph.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Graph làm rõ phụ thuộc giữa preprocessing, training, evaluation, condition, registration và failure.

Ảnh tiếp theo ghi nhận **execution heart-risk-pipeline thành công**.

<figure class="evidence">
  <img src="/images/evidence/W8-02-pipeline-success.png" alt="Execution heart-risk-pipeline thành công" loading="lazy">
  <figcaption>Execution heart-risk-pipeline thành công — <code>W8-02-pipeline-success.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Trạng thái Succeeded chứng minh workflow managed end-to-end hoàn tất.

Ảnh tiếp theo ghi nhận **trạng thái từng step trên nhánh thành công**.

<figure class="evidence">
  <img src="/images/evidence/W8-03-success-steps.png" alt="Trạng thái từng step trên nhánh thành công" loading="lazy">
  <figcaption>Trạng thái từng step trên nhánh thành công — <code>W8-03-success-steps.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Mọi step trên nhánh success hoàn tất, cung cấp minh chứng chi tiết hơn trạng thái tổng.

Ảnh tiếp theo ghi nhận **điều kiện chất lượng mô hình đã pass**.

<figure class="evidence">
  <img src="/images/evidence/W8-04-condition-pass.png" alt="Điều kiện chất lượng mô hình đã pass" loading="lazy">
  <figcaption>Điều kiện chất lượng mô hình đã pass — <code>W8-04-condition-pass.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Kết quả condition chứng minh metric đánh giá đã chọn nhánh RegisterModel.
