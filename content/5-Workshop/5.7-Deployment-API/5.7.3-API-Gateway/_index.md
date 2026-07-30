---
title: "API Gateway"
weight: 3
chapter: false
pre: " <b>5.7.3.</b> "
---

# API Gateway

Create HTTP API `heart-risk-http-api` with:

```text
GET /health
POST /predict
```

Use a masked stage URL:

```bash
curl -i "$API_BASE_URL/health"
curl -i -X POST "$API_BASE_URL/predict"   -H 'content-type: application/json' --data @sample-request.json
```

| Test | Expected | Operational meaning |
|---|---:|---|
| Health | 200 | wrapper reachable |
| Valid prediction | 200 | API-to-endpoint integration works |
| Missing fields | 400 | client validation works |
| Service unavailable | 502 | downstream failure is controlled |

`W6-07` through `W6-11` should prove routes and each case when files are supplied. Never publish an active full URL; add throttling/authentication for production.

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

Next: [Data Capture](../5.7.4-Data-Capture/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **http api routes for health and prediction**.

<figure class="evidence">
  <img src="/images/evidence/W6-07-api-routes.png" alt="HTTP API routes for health and prediction" loading="lazy">
  <figcaption>HTTP API routes for health and prediction — <code>W6-07-api-routes.png</code></figcaption>
</figure>

**Technical meaning:** The route table proves GET /health and POST /predict are wired to the API integration.

The next screenshot records **successful get /health response**.

<figure class="evidence">
  <img src="/images/evidence/W6-08-health-200.png" alt="Successful GET /health response" loading="lazy">
  <figcaption>Successful GET /health response — <code>W6-08-health-200.png</code></figcaption>
</figure>

**Technical meaning:** HTTP 200 verifies that the public wrapper path is reachable without invoking a clinical conclusion.

The next screenshot records **successful post /predict response**.

<figure class="evidence">
  <img src="/images/evidence/W6-09-predict-200.png" alt="Successful POST /predict response" loading="lazy">
  <figcaption>Successful POST /predict response — <code>W6-09-predict-200.png</code></figcaption>
</figure>

**Technical meaning:** The happy path proves API Gateway, Lambda, and the SageMaker endpoint interoperate and return the documented contract.

The next screenshot records **missing-field request returns http 400**.

<figure class="evidence">
  <img src="/images/evidence/W6-10-predict-400.png" alt="Missing-field request returns HTTP 400" loading="lazy">
  <figcaption>Missing-field request returns HTTP 400 — <code>W6-10-predict-400.png</code></figcaption>
</figure>

**Technical meaning:** The controlled client error proves input validation rejects incomplete requests before model invocation.

The next screenshot records **unavailable prediction service returns http 502**.

<figure class="evidence">
  <img src="/images/evidence/W6-11-predict-502.png" alt="Unavailable prediction service returns HTTP 502" loading="lazy">
  <figcaption>Unavailable prediction service returns HTTP 502 — <code>W6-11-predict-502.png</code></figcaption>
</figure>

**Technical meaning:** The test proves downstream failures are translated into a stable API error rather than leaking an internal exception.
