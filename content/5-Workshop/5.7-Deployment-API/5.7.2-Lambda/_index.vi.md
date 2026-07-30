---
title: "Lambda wrapper"
weight: 2
chapter: false
pre: " <b>5.7.2.</b> "
---

# Lambda wrapper

`heart-risk-api` validate field bắt buộc, serialize request, chỉ gọi `heart-risk-endpoint`, và ánh xạ lỗi downstream thành response an toàn.

```python
endpoint = os.environ["ENDPOINT_NAME"]
response = runtime.invoke_endpoint(
    EndpointName=endpoint, ContentType="application/json", Body=json.dumps(payload)
)
```

Biến môi trường giữ cấu hình endpoint/model, không giữ credential. `AWS-14` and `W6-06a/b` cần chứng minh quyền đặc quyền tối thiểu `sagemaker:InvokeEndpoint`; `W6-04/05` chứng minh cấu hình. Các ảnh được cung cấp xác nhận cấu hình và role policy.

**Kỳ vọng:** event hợp lệ trả result có cấu trúc; thiếu field trả 400; prediction service không sẵn sàng trả 502 không lộ stack trace. Khi timeout, đọc log Lambda/endpoint. Lambda và log retention phát sinh phí.

Tiếp theo: [API Gateway](../5.7.3-API-Gateway/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **cấu hình lambda heart-risk-api đã triển khai**.

<figure class="evidence">
  <img src="/images/evidence/W6-04-lambda-config.png" alt="Cấu hình Lambda heart-risk-api đã triển khai" loading="lazy">
  <figcaption>Cấu hình Lambda heart-risk-api đã triển khai — <code>W6-04-lambda-config.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Cấu hình chứng minh wrapper serverless để validate và gọi endpoint đã tồn tại.

Ảnh tiếp theo ghi nhận **biến môi trường endpoint và model của lambda**.

<figure class="evidence">
  <img src="/images/evidence/W6-05-lambda-environment.png" alt="Biến môi trường endpoint và model của Lambda" loading="lazy">
  <figcaption>Biến môi trường endpoint và model của Lambda — <code>W6-05-lambda-environment.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Cấu hình ngoài tránh hard-code identifier trong logic; vẫn không được lưu secret tại đây.

Ảnh tiếp theo ghi nhận **tổng quan iam role của lambda**.

<figure class="evidence">
  <img src="/images/evidence/W6-06a-lambda-role-overview.png" alt="Tổng quan IAM role của Lambda" loading="lazy">
  <figcaption>Tổng quan IAM role của Lambda — <code>W6-06a-lambda-role-overview.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Tổng quan role xác định identity mà API wrapper sử dụng khi chạy.

Ảnh tiếp theo ghi nhận **chi tiết quyền gọi endpoint của lambda**.

<figure class="evidence">
  <img src="/images/evidence/W6-06b-lambda-role-details.png" alt="Chi tiết quyền gọi endpoint của Lambda" loading="lazy">
  <figcaption>Chi tiết quyền gọi endpoint của Lambda — <code>W6-06b-lambda-role-details.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Policy chi tiết hỗ trợ nguyên tắc đặc quyền tối thiểu bằng cách giới hạn action/resource cần thiết.
