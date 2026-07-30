---
title: "Model Registry"
weight: 2
chapter: false
pre: " <b>5.6.2.</b> "
---

## Objective and states

Use `heart-attack-risk-models` for lineage and a human promotion decision.

| Version | State | Meaning |
|---:|---|---|
| 1 | Approved | retained approved version |
| 2 | Approved | deployment source for `heart-risk-endpoint` |
| 3 | PendingManualApproval | created by successful Pipeline |

```bash
aws sagemaker list-model-packages   --model-package-group-name heart-attack-risk-models   --region "$AWS_REGION"
```

`W5-01` should prove the states when supplied. Manual approval prevents an evaluated artifact from being deployed merely because training completed.

**Errors:** a package that rejects `ml.t3.medium` requires a supported deployment configuration; this project uses `ml.m5.large`. Avoid publishing full account-bearing ARNs.

Next: [Deployment and API](../../5.7-Deployment-API/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **model registry versions and approval states**.

<figure class="evidence">
  <img src="../../../images/evidence/W5-01-model-versions.png" alt="Model Registry versions and approval states" loading="lazy">
  <figcaption>Model Registry versions and approval states — <code>W5-01-model-versions.png</code></figcaption>
</figure>

**Technical meaning:** The version list distinguishes Approved versions 1–2 from Pipeline-created version 3 PendingManualApproval.
