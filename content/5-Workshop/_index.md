---
title: "Heart Risk MLOps Workshop"
weight: 5
chapter: false
pre: " <b>5.</b> "
---

# Building and Deploying an End-to-End Heart Attack Risk Prediction System on AWS SageMaker

This workshop builds a reproducible end-to-end MLOps proof of concept for binary heart-attack risk classification: prepare data, compare models, enforce quality gates, register and approve, deploy a real-time endpoint, expose an API, capture traffic, detect drift, alert, and automate with SageMaker Pipelines.

**Audience:** learners familiar with Python, AWS fundamentals, and basic classification.  
**Duration:** approximately 8–12 guided hours, excluding job waiting time.  
**Services:** S3, SageMaker Processing/Training/HPO/Registry/Endpoint/Model Monitor/Pipelines, Lambda, API Gateway, CloudWatch, IAM, Budgets.

{{% notice warning %}}
AWS resources can incur charges, especially a continuously running endpoint. Use Budget alerts and complete the cleanup runbook.
{{% /notice %}}

{{% notice warning %}}
Educational demonstration only; not a medical diagnosis.
{{% /notice %}}

![Heart-risk MLOps architecture](../images/architecture/heart-risk-architecture.svg)

## Learning objectives and navigation

1. [Overview](5.1-Overview/)
2. [Prerequisites](5.2-Prerequisites/)
3. [Architecture](5.3-Architecture/)
4. [Data preparation](5.4-Data-Preparation/)
5. [Model training](5.5-Model-Training/)
6. [Evaluation and Registry](5.6-Evaluation-Registry/)
7. [Deployment and API](5.7-Deployment-API/)
8. [Monitoring](5.8-Monitoring/)
9. [Pipeline](5.9-Pipeline/)
10. [Security and cost](5.10-Security-Cost/)
11. [Cleanup](5.11-Cleanup/)
12. [Results and limitations](5.12-Results-Limitations/)
