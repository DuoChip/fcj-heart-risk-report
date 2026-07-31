---
title: "Running SageMaker MLOps on USD 200: 13 Budget Decisions"
weight: 3
chapter: false
pre: " <b>3.3.</b> "
---

## Submitted article

**Original title:** Chạy SageMaker MLOps với 200 USD: 13 quyết định để không cháy budget

The article summarizes cost-management lessons from the Heart Risk SageMaker capstone. Its central message is that cloud cost is driven less by the amount of development effort than by resources left running, oversized experiments, missing lifecycle rules, and incomplete cleanup planning.

The figures are educational estimates from the project period and may change. Readers are directed to verify current prices with AWS Pricing Calculator before applying the recommendations.

## Thirteen decisions

### Compute

1. Benchmark a small instance before scaling up.
2. Avoid GPU instances when the algorithm and dataset do not need them.
3. Keep the student PoC in one AWS Region.
4. Delete the real-time endpoint immediately after demonstrations.

### Data and storage

5. Configure S3 lifecycle policies for temporary logs and artifacts.
6. Reuse processed datasets instead of repeating unchanged preprocessing.
7. Avoid retraining for improvements that do not provide meaningful value.
8. Tag resources with project, owner, environment, and cleanup metadata.

### Pipeline and training

9. Bound HPO jobs and parallelism.
10. Run a scheduled cleanup checklist or script.
11. Use ephemeral SageMaker Training Jobs instead of keeping notebook compute running for training.

### IAM and networking

12. Apply least-privilege IAM instead of `AdministratorAccess`.
13. Avoid a NAT Gateway when the architecture does not require it; evaluate VPC endpoints or suitable public access instead.

## Connection to the internship project

The project used bounded HPO, managed jobs, a single endpoint for the PoC, budget alerts, IAM roles, tagged/versioned outputs, and a cleanup runbook. The submitted article also emphasizes a design principle learned during the internship: cleanup, lifecycle, and cost controls should be planned when resources are designed—not added only after development.

Cost values in the article are estimates, not verified AWS billing guarantees. Some instance availability and pricing vary by Region, service mode, and time.

## Publication status

- **Status:** **Pending approval**
- **Public URL:** Not available while the community post is awaiting approval
- **Submission evidence:** the supplied Facebook screenshot displays the article title and identifies Đoàn Mạnh Tất, Nguyễn Châu, and Phạm Đình Được

<figure class="evidence">
  <img src="../../images/evidence/blogs/blog3-facebook-pending-review.jpg" alt="Facebook submission awaiting approval for the SageMaker MLOps budget article" loading="lazy">
  <figcaption>Blog 3 submitted to AWS Study Group VN and awaiting approval — <code>blog3-facebook-pending-review.jpg</code></figcaption>
</figure>

The screenshot proves that the article was submitted; it does not prove public publication or provide a public permalink.
