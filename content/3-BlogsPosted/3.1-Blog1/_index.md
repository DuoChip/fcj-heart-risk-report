---
title: "AWS Lambda: Cost and Performance Optimization"
weight: 1
chapter: false
pre: " <b>3.1.</b> "
---

## Published article

**Original Vietnamese title:** AWS Lambda: Chiến lược “xài đúng” và “chạy nhanh” để tối ưu chi phí

The article explains when Lambda is a good fit—event-driven processing, spiky APIs, and scheduled jobs—and when long-running, stateful, or ultra-low-latency workloads require another service.

## Main content

- Reuse the execution environment by initializing SDK and database clients outside the handler.
- Tune memory because additional memory also increases available CPU.
- Reduce cold starts and choose Provisioned Concurrency only when its continuous cost is justified.
- Keep deployment packages small and use Layers appropriately.
- Use RDS Proxy to protect relational databases from connection bursts.
- Monitor with AWS X-Ray, CloudWatch, and custom metrics.
- Design for failure with SQS dead-letter queues and understand concurrency limits.

## Relation to the internship project

These practices support the `heart-risk-api` Lambda wrapper: reuse the SageMaker Runtime client, keep validation lightweight, apply least-privilege `InvokeEndpoint`, monitor failures, and avoid continuously billed options unless latency requirements justify them.

## Publication status

- **Status:** Published in AWS Study Group VN
- **Publication date:** 29 June 2026
- **Facebook post:** [Read the published AWS Lambda article](https://www.facebook.com/groups/660548818043427/?multi_permalinks=2227143931383900&hoisted_section_header_type=recently_seen)
- **Attribution:** the post displays Nguyễn Châu and tags Phạm Đình Được

The supplied screenshot records the visible article title and attribution on Facebook:

<figure class="evidence">
  <img src="../../images/evidence/blogs/blog1-facebook-post.png" alt="Facebook evidence for the published AWS Lambda optimization article" loading="lazy">
  <figcaption>Published AWS Lambda optimization article in AWS Study Group VN — <code>blog1-facebook-post.png</code></figcaption>
</figure>

**Publication evidence:** the screenshot shows the published Lambda article and the tag for Phạm Đình Được.

## Cost and security note

Provisioned Concurrency, log retention, and downstream services can add cost even when Lambda request volume is low. Credentials must not be embedded in function code or environment variables.
