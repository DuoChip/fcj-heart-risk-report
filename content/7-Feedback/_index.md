---
title: "Sharing and Feedback"
weight: 7
chapter: false
pre: " <b>7.</b> "
---

## Overall experience and satisfaction

I rate my overall FCAJ internship experience **8/10**. The program gave me a practical setting in which to connect Data Engineering, Machine Learning, and AWS services through one end-to-end project instead of learning each service in isolation. Building the Heart Risk MLOps PoC helped me understand that a useful ML system includes much more than a trained model: reproducible data preparation, evaluation gates, model governance, deployment, monitoring, cost control, security, and clear documentation are equally important.

The most satisfying outcome was turning an initial notebook workflow into a system that could be explained and demonstrated from raw data to an API prediction and a drift alarm. The project is still a learning PoC rather than a production healthcare system, but it gave me a concrete view of the engineering standards required beyond experimentation.

## Most valuable learning

My most valuable learning was the transition from notebook experimentation to traceable managed workflows. I learned to:

- split data before fitting preprocessing logic to prevent leakage;
- use SageMaker Processing and Training Jobs instead of depending on a continuously running notebook;
- compare models with ROC-AUC, F1, and recall rather than selecting a model from one metric;
- register a model with manual approval and enforce pass/fail quality gates in SageMaker Pipelines;
- expose inference through Lambda and API Gateway with input validation and safe error responses;
- turn captured inference data into custom drift metrics and a CloudWatch alarm;
- treat IAM scope, resource lifetime, budget alerts, and cleanup as architecture decisions.

## Support and learning environment

The FCAJ structure encouraged independent research and implementation rather than limiting the work to following a fixed laboratory script. The report and workshop requirements also pushed me to preserve evidence, explain design decisions, and communicate the result in both Vietnamese and English.

The AWS Study Group community provided a useful environment for sharing technical knowledge. Two articles on AWS Lambda and Amazon SageMaker were published, while the third cost-focused SageMaker MLOps article is awaiting approval. Attending the Agentic AI and Hackathon solution-sharing event on 25 July also helped me compare how other teams frame problems, explain architecture, and demonstrate an MVP.

I do not attribute specific feedback to an individual mentor because no formal mentor-feedback record was supplied for this report.

## Technical and soft-skill growth

Technically, I improved in Python-based data processing, leakage-aware ML evaluation, SageMaker managed jobs, model deployment, CloudWatch monitoring, IAM, and cost-aware AWS operation. I also became more systematic about reading logs, isolating causes, testing a smaller component locally, and recording the final evidence.

In soft skills, writing a bilingual workshop improved my technical communication and ability to organize a long implementation into reproducible steps. Preparing community blog posts taught me to translate technical details into practical lessons. The event on 25 July showed me the value of a problem–solution–impact storyline. My teamwork evidence is more limited than my technical evidence, so a future project should maintain clearer task ownership, decision logs, and review records from the beginning.

## Difficulties

The main difficulties were not model training itself, but integration and operational behavior:

- `ml.t3.medium` was unsupported for a managed job, requiring a change to `ml.m5.large`;
- the expected official feature-level drift metric was unavailable, so I implemented a transparent custom Processing fallback;
- sparse custom metrics could incorrectly change alarm behavior until `TreatMissingData=ignore` was configured;
- Pipeline creation and updates required an idempotent upsert sequence;
- SageMaker SDK v2 deprecation warnings created future migration work;
- endpoint, logs, artifacts, and experiments required active cost and cleanup discipline.

These issues taught me to verify service constraints early, define observable failure behavior, and keep a fallback that remains measurable and explainable.

## Suggestions for FCAJ

I suggest adding several checkpoints to future FCAJ cohorts:

1. an early environment-readiness review covering Region, IAM, quotas, supported instance types, and budget alerts;
2. a short architecture review before learners create billable resources;
3. mandatory cost-estimation and cleanup checklists for every milestone;
4. an evidence checklist showing which screenshots, logs, metrics, and public links are expected;
5. a small bilingual report example with clear rules for claims that require verification;
6. periodic peer reviews so learners practice explaining decisions and recording feedback before the final week.

## Recommendation and career direction

I would recommend FCAJ to students who already understand basic programming and want practical experience connecting AWS services into a complete solution. The program is most valuable when learners actively experiment, read service documentation, control their budget, and document problems instead of only reproducing successful commands.

My career direction is **Data Engineering with a path toward MLOps and cloud data platforms**. After this internship, my next priorities are stronger data pipeline design, Infrastructure as Code, automated testing and CI/CD, containerization, observability, and production security. I also want to deepen SageMaker and AWS data-service knowledge so that I can build systems where data preparation, model delivery, and operations are reproducible and maintainable.
