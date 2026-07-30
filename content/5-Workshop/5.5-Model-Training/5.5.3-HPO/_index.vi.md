---
title: "Tối ưu siêu tham số"
weight: 3
chapter: false
pre: " <b>5.5.3.</b> "
---

# Tối ưu siêu tham số

## Mục tiêu và cấu hình

Dùng managed Bayesian search nhỏ có chủ đích để cải thiện XGBoost mà không mất kiểm soát chi phí.

```python
objective_metric_name = "validation:auc"
strategy = "Bayesian"
max_jobs, max_parallel_jobs = 3, 1
tuned = ["eta", "max-depth", "min-child-weight"]
```

| Candidate | Validation AUC | F1 | Recall |
|---|---:|---:|---:|
| LR | **0.863949** | 0.747583 | 0.789116 |
| XGBoost default | 0.854283 | 0.749749 | 0.845805 |
| XGBoost HPO | 0.860982 | 0.749522 | **0.888889** |

LR vẫn được chọn theo validation AUC. Không dùng test để chọn model/trial. Không có ảnh HPO nên trang chủ động không chèn link ảnh hỏng.

**Xử lý lỗi:** không có best job thường do objective metric regex/name không được emit. Ba job tuần tự giới hạn phí nhưng cũng giới hạn chất lượng search.

Tiếp theo: [Đánh giá và Registry](../../5.6-Evaluation-Registry/).
