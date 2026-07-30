---
title: "Amazon SageMaker: AI/ML and Cost Optimization"
weight: 2
chapter: false
pre: " <b>3.2.</b> "
---

## Published article

**Original Vietnamese title:** Amazon SageMaker: AI/ML của AWS và Cách tối ưu để không tốn tiền oan

The article presents SageMaker as a platform spanning Studio, managed Training Jobs, and inference hosting rather than only a cloud notebook.

## Main content

- Separate Studio experimentation from managed training and inference.
- Consider Managed Spot Training with checkpointing for interruptible workloads.
- Bound HPO job counts and parallelism before scaling the search.
- Match CPU/GPU instance families to the algorithm and dataset.
- Treat continuously running real-time endpoints as a primary cost risk.
- Evaluate Auto Scaling, Serverless Inference, quantization, and SageMaker Neo according to traffic and latency.
- Use SageMaker Pipelines, Model Registry, staging, and controlled deployment for MLOps.

## Relation to the internship project

The heart-risk PoC follows several of these principles: managed jobs instead of notebook-bound training, three sequential HPO trials, one endpoint instance, Model Registry/manual approval, quality gates, Pipeline automation, Budget alerts, and an explicit cleanup runbook.

## Publication status

- **Status:** Published in AWS Study Group VN
- **Publication date:** 29 June 2026
- **Facebook post:** [Read the published Amazon SageMaker article](https://www.facebook.com/groups/awsstudygroupfcj/posts/2227364341361859/?notif_id=1785325679108331&notif_t=tagged_with_story&ref=notif)
- **Attribution:** the post displays Nguyễn Châu and tags Phạm Đình Được

The supplied screenshot records the visible article title and attribution on Facebook:

<figure class="evidence">
  <img src="../../images/evidence/blogs/blog2-facebook-post.png" alt="Facebook evidence for the published Amazon SageMaker cost optimization article" loading="lazy">
  <figcaption>Published Amazon SageMaker cost optimization article in AWS Study Group VN — <code>blog2-facebook-post.png</code></figcaption>
</figure>

**Publication evidence:** the screenshot shows the published SageMaker article and the tag for Phạm Đình Được.

## Cost and security note

Cost-saving techniques must be validated against workload reliability and latency. IAM roles, private data storage, bounded experiments, monitoring, and cleanup remain mandatory.
