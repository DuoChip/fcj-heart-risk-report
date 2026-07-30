---
title: "API Gateway"
weight: 3
chapter: false
pre: " <b>5.7.3.</b> "
---

# API Gateway

Tạo HTTP API `heart-risk-http-api` với:

```text
GET /health
POST /predict
```

Dùng stage URL đã che:

```bash
curl -i "$API_BASE_URL/health"
curl -i -X POST "$API_BASE_URL/predict"   -H 'content-type: application/json' --data @sample-request.json
```

| Test | Kỳ vọng | Ý nghĩa vận hành |
|---|---:|---|
| Health | 200 | wrapper truy cập được |
| Prediction hợp lệ | 200 | tích hợp API-endpoint hoạt động |
| Thiếu field | 400 | validate phía client hoạt động |
| Service không sẵn sàng | 502 | lỗi downstream được kiểm soát |

`W6-07` through `W6-11` cần chứng minh route và từng case khi có file. Không public URL active đầy đủ; thêm throttling/authentication cho production.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

Tiếp theo: [Data Capture](../5.7.4-Data-Capture/).

## Minh chứng và diễn giải kỹ thuật

Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được.

Ảnh tiếp theo ghi nhận **các route http api cho health và prediction**.

<figure class="evidence">
  <img src="/images/evidence/W6-07-api-routes.png" alt="Các route HTTP API cho health và prediction" loading="lazy">
  <figcaption>Các route HTTP API cho health và prediction — <code>W6-07-api-routes.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Bảng route chứng minh GET /health và POST /predict được nối với API integration.

Ảnh tiếp theo ghi nhận **response get /health thành công**.

<figure class="evidence">
  <img src="/images/evidence/W6-08-health-200.png" alt="Response GET /health thành công" loading="lazy">
  <figcaption>Response GET /health thành công — <code>W6-08-health-200.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** HTTP 200 xác minh đường dẫn wrapper hoạt động mà không đưa ra kết luận lâm sàng.

Ảnh tiếp theo ghi nhận **response post /predict thành công**.

<figure class="evidence">
  <img src="/images/evidence/W6-09-predict-200.png" alt="Response POST /predict thành công" loading="lazy">
  <figcaption>Response POST /predict thành công — <code>W6-09-predict-200.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Happy path chứng minh API Gateway, Lambda và SageMaker endpoint tích hợp và trả đúng contract.

Ảnh tiếp theo ghi nhận **request thiếu field trả http 400**.

<figure class="evidence">
  <img src="/images/evidence/W6-10-predict-400.png" alt="Request thiếu field trả HTTP 400" loading="lazy">
  <figcaption>Request thiếu field trả HTTP 400 — <code>W6-10-predict-400.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Client error có kiểm soát chứng minh validation chặn request thiếu trước khi gọi model.

Ảnh tiếp theo ghi nhận **prediction service không sẵn sàng trả http 502**.

<figure class="evidence">
  <img src="/images/evidence/W6-11-predict-502.png" alt="Prediction service không sẵn sàng trả HTTP 502" loading="lazy">
  <figcaption>Prediction service không sẵn sàng trả HTTP 502 — <code>W6-11-predict-502.png</code></figcaption>
</figure>

**Ý nghĩa kỹ thuật:** Test chứng minh lỗi downstream được đổi thành API error ổn định thay vì lộ exception nội bộ.
