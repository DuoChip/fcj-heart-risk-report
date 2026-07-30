---
title: "Lambda wrapper"
weight: 2
chapter: false
pre: " <b>5.7.2.</b> "
---

# Lambda wrapper

`heart-risk-api` validates required fields, serializes the endpoint request, invokes only `heart-risk-endpoint`, and maps downstream errors to safe responses.

```python
endpoint = os.environ["ENDPOINT_NAME"]
response = runtime.invoke_endpoint(
    EndpointName=endpoint, ContentType="application/json", Body=json.dumps(payload)
)
```

Environment variables hold endpoint/model configuration, never credentials. `AWS-14` and `W6-06a/b` should prove least-privilege `sagemaker:InvokeEndpoint`; `W6-04/05` configuration. The supplied screenshots substantiate the configuration and role policy.

**Expected:** valid events return structured results; missing fields return 400; unavailable prediction service returns 502 without an internal stack trace. Inspect Lambda/endpoint logs on timeout. Lambda and log retention incur usage/storage costs.

Next: [API Gateway](../5.7.3-API-Gateway/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **deployed heart-risk-api lambda configuration**.

<figure class="evidence">
  <img src="/images/evidence/W6-04-lambda-config.png" alt="Deployed heart-risk-api Lambda configuration" loading="lazy">
  <figcaption>Deployed heart-risk-api Lambda configuration — <code>W6-04-lambda-config.png</code></figcaption>
</figure>

**Technical meaning:** The function configuration proves the serverless validation and endpoint-invocation wrapper exists.

The next screenshot records **lambda endpoint and model environment variables**.

<figure class="evidence">
  <img src="/images/evidence/W6-05-lambda-environment.png" alt="Lambda endpoint and model environment variables" loading="lazy">
  <figcaption>Lambda endpoint and model environment variables — <code>W6-05-lambda-environment.png</code></figcaption>
</figure>

**Technical meaning:** External configuration avoids hard-coding deployment identifiers in application logic; secrets must still never be stored here.

The next screenshot records **lambda iam role overview**.

<figure class="evidence">
  <img src="/images/evidence/W6-06a-lambda-role-overview.png" alt="Lambda IAM role overview" loading="lazy">
  <figcaption>Lambda IAM role overview — <code>W6-06a-lambda-role-overview.png</code></figcaption>
</figure>

**Technical meaning:** The role overview establishes the identity used by the API wrapper at runtime.

The next screenshot records **detailed lambda endpoint-invocation permission**.

<figure class="evidence">
  <img src="/images/evidence/W6-06b-lambda-role-details.png" alt="Detailed Lambda endpoint-invocation permission" loading="lazy">
  <figcaption>Detailed Lambda endpoint-invocation permission — <code>W6-06b-lambda-role-details.png</code></figcaption>
</figure>

**Technical meaning:** The detailed policy supports the least-privilege claim by limiting the wrapper to required actions/resources.
