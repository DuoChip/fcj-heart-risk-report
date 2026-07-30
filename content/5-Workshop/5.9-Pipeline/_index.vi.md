---
title: "SageMaker Pipeline"
weight: 9
chapter: false
pre: " <b>5.9.</b> "
---

# Pipeline có quality gate

`PreprocessData → TrainModel → EvaluateModel → CheckModelQuality`; pass đăng ký, fail chạy `MetricThresholdFailed`.

1. [Execution thành công](5.9.1-Success-Execution/)
2. [Thất bại có chủ đích](5.9.2-Intentional-Failure/)
