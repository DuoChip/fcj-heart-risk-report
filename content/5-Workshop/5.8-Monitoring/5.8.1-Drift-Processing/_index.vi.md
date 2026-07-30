---
title: "Custom drift Processing"
weight: 1
chapter: false
pre: " <b>5.8.1.</b> "
---

# Custom drift Processing

## Luồng và quy tắc PoC

Data Capture/S3 current data → custom SageMaker Processing → report → CloudWatch.

| Kiểm tra | Giá trị |
|---|---:|
| Baseline/current | 4.900 / 7.000 dòng |
| Feature/violation | 20 / 6 |
| Drift | age, resting_bp, cholesterol, bmi, smoking_status, stress_level |

Numeric drift khi standardized mean shift > 0,5; categorical drift khi total variation distance > 0,20.

{{% notice warning %}}
Đây là quy tắc proof of concept minh bạch, không phải ngưỡng lâm sàng hay chuẩn production phổ quát.
{{% /notice %}}

`W7-01a/b` cần chứng minh managed execution/history; `W7-02` chứng minh số lượng; `W7-03a/b` chứng minh feature. Nếu không flatten được schema capture, kiểm tra encoding JSONL input/output trước khi tính drift. Processing compute tính phí theo lần chạy.

Tiếp theo: [CloudWatch alarm](../5.8.2-CloudWatch-Alarm/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **chi tiết custom drift processing job**.

<figure class="evidence">
  <img src="/images/evidence/W7-01a-custom-processing-job.png" alt="Chi tiết custom drift Processing Job" loading="lazy">
  <figcaption>Chi tiết custom drift Processing Job — <code>W7-01a-custom-processing-job.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Chi tiết job chứng minh drift fallback chạy trên hạ tầng SageMaker managed.

Ảnh tiếp theo ghi nhận **lịch sử custom drift processing job**.

<figure class="evidence">
  <img src="/images/evidence/W7-01b-processing-job-list.png" alt="Lịch sử custom drift Processing Job" loading="lazy">
  <figcaption>Lịch sử custom drift Processing Job — <code>W7-01b-processing-job-list.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Danh sách job cung cấp khả năng truy vết vận hành giữa các execution.

Ảnh tiếp theo ghi nhận **tóm tắt custom drift report**.

<figure class="evidence">
  <img src="/images/evidence/W7-02-drift-report.png" alt="Tóm tắt custom drift report" loading="lazy">
  <figcaption>Tóm tắt custom drift report — <code>W7-02-drift-report.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Report xác minh 4.900 baseline, 7.000 current, 20 feature và sáu violation.

Ảnh tiếp theo ghi nhận **tóm tắt sáu feature bị drift**.

<figure class="evidence">
  <img src="/images/evidence/W7-03a-drift-features-summary.png" alt="Tóm tắt sáu feature bị drift" loading="lazy">
  <figcaption>Tóm tắt sáu feature bị drift — <code>W7-03a-drift-features-summary.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Tóm tắt nêu tên feature numeric/categorical bị ảnh hưởng thay vì chỉ báo alarm nhị phân.

Ảnh tiếp theo ghi nhận **chi tiết custom drift theo feature**.

<figure class="evidence">
  <img src="/images/evidence/W7-03b-drift-features-details.png" alt="Chi tiết custom drift theo feature" loading="lazy">
  <figcaption>Chi tiết custom drift theo feature — <code>W7-03b-drift-features-details.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Giá trị theo feature giúp quyết định theo ngưỡng PoC có thể kiểm tra và tái lập.
