---
title: "Thất bại có chủ đích"
weight: 2
chapter: false
pre: " <b>5.9.2.</b> "
---

# Pipeline thất bại có chủ đích

Ghi đè `AucThreshold=0.99`, cao hơn kết quả 0.885515 result. Execution cuối là `Failed` **theo thiết kế**, `MetricThresholdFailed` được chạy và RegisterModel không chạy.

```bash
aws sagemaker start-pipeline-execution   --pipeline-name "$PIPELINE_NAME"   --pipeline-parameters Name=AucThreshold,Value=0.99   --region "$AWS_REGION"
```

`W8-05` cần chứng minh execution failed, `W8-06` tham số 0,99 và `W8-07` fail step. Các minh chứng cho thấy ứng viên không đạt không thể âm thầm vào registry.

**Xử lý lỗi:** không “sửa” test dự kiến này bằng cách hạ gate giữa execution. Phân biệt condition failure với infrastructure failure trong metadata/log.

Tiếp theo: [Bảo mật và chi phí](../../5.10-Security-Cost/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **pipeline execution thất bại theo thiết kế**.

<figure class="evidence">
  <img src="/images/evidence/W8-05-pipeline-failure.png" alt="Pipeline execution thất bại theo thiết kế" loading="lazy">
  <figcaption>Pipeline execution thất bại theo thiết kế — <code>W8-05-pipeline-failure.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Trạng thái fail là minh chứng guardrail được test, không phải lỗi hiện thực.

Ảnh tiếp theo ghi nhận **aucthreshold được ghi đè có chủ đích thành 0,99**.

<figure class="evidence">
  <img src="/images/evidence/W8-06-failure-parameters.png" alt="AucThreshold được ghi đè có chủ đích thành 0,99" loading="lazy">
  <figcaption>AucThreshold được ghi đè có chủ đích thành 0,99 — <code>W8-06-failure-parameters.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Tham số chứng minh gate test cố ý cao đã kích hoạt nhánh failure.

Ảnh tiếp theo ghi nhận **step metricthresholdfailed đã chặn đăng ký**.

<figure class="evidence">
  <img src="/images/evidence/W8-07-fail-step.png" alt="Step MetricThresholdFailed đã chặn đăng ký" loading="lazy">
  <figcaption>Step MetricThresholdFailed đã chặn đăng ký — <code>W8-07-fail-step.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Fail step được chạy chứng minh ứng viên dưới gate không thể vào Model Registry.
