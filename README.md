# FCAJ Internship Report — Heart Risk MLOps

Bilingual Hugo report and reproducible workshop for **Building and Deploying an End-to-End Heart Attack Risk Prediction System on AWS SageMaker**.

The site documents leakage-safe processing, managed training and HPO, quality-gated evaluation, Model Registry, real-time inference, Lambda/API Gateway, Data Capture, custom drift monitoring, CloudWatch alarms, SageMaker Pipelines, security, cost controls, and cleanup. It is an educational proof of concept, not a medical diagnosis.

Published site: <https://duochip.github.io/fcj-heart-risk-report/>

## Prerequisites

- Git
- Hugo Extended 0.134.3 (the deployment workflow pins this version)

## Run locally

```bash
git submodule update --init --recursive
hugo server -D
```

Build the production site:

```bash
hugo --minify
```

## Deployment

`.github/workflows/hugo.yml` builds with Hugo Extended 0.134.3 on pushes to `main` and publishes `public/` to the `gh-pages` branch.

GitHub Pages should use **Deploy from a branch**, with branch `gh-pages` and folder `/ (root)`. No custom domain or `CNAME` file is required for the default GitHub Pages URL.

## Content conventions

- Every main page has `_index.md` (English) and `_index.vi.md` (Vietnamese).
- Resource/API identifiers stay unchanged across languages.
- Administrative facts remain explicit `TODO` values until verified.
- Never publish credentials, private data, active API URLs, or unmasked sensitive identifiers.
- Place sanitized evidence in `static/images/evidence/`; introduce, caption, and analyze every displayed image.
- Place reviewed downloads in `static/attachments/heart-risk/`; omit links to unavailable files.
- Cleanup, event attendance, and blog publication must not be claimed without evidence.

## Important TODOs

Add verified student details, event/publication information, actual safe project source attachments, and cleanup evidence after cleanup is executed. The supplied AWS evidence catalog is already organized and linked; review masking before public deployment.
