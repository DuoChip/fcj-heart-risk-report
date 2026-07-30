---
title: "Đánh giá cuối"
weight: 1
chapter: false
pre: " <b>5.6.1.</b> "
---

# Đánh giá cuối

| Metric | Giá trị |
|---|---:|
| ROC-AUC | 0,885515 |
| Accuracy | 0,793333 |
| Precision | 0,724900 |
| Recall | 0,818594 |
| F1 | 0,768903 |
| False Negative Rate | 0,181406 |

| | Dự đoán negative | Dự đoán positive |
|---|---:|---:|
| Thực tế negative | TN 472 | FP 137 |
| Thực tế positive | FN 80 | TP 361 |

Model vượt AUC ≥ 0,84, F1 ≥ 0,70, recall ≥ 0,65. 80 âm tính giả là positive label bị model bỏ sót; đây là giới hạn quan trọng, không phải bằng chứng an toàn lâm sàng. `W5-02` cần xác nhận metric/confusion matrix khi được cung cấp.

**Xử lý lỗi:** không tune sau khi xem test. Sai khác thường do threshold hoặc preprocessing artifact khác. Evaluation job có phí compute/storage; bảo vệ test data và report.

{{% notice warning %}}
Hệ thống chỉ phục vụ mục đích học tập và minh họa; không phải là chẩn đoán y khoa.
{{% /notice %}}

Tiếp theo: [Model Registry](../5.6.2-Model-Registry/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **metric test cuối và confusion matrix**.

<figure class="evidence">
  <img src="/images/evidence/W5-02-evaluation-metrics-and-confusion-matrix.png" alt="Metric test cuối và confusion matrix" loading="lazy">
  <figcaption>Metric test cuối và confusion matrix — <code>W5-02-evaluation-metrics-and-confusion-matrix.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Minh chứng cho thấy ba quality gate đều pass đồng thời thể hiện rõ 80 âm tính giả.
