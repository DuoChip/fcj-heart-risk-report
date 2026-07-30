---
title: "Data Capture"
weight: 4
chapter: false
pre: " <b>5.7.4.</b> "
---

Enable 100% input and output capture in JSONL to the private project S3 prefix.

```text
EnableCapture=true
InitialSamplingPercentage=100
CaptureOptions=[Input, Output]
```

An actual record contains `endpointInput`, `endpointOutput`, `eventMetadata`, and `inferenceTime`. `W6-02` should prove configuration, `W6-12` generated files, and `W6-13` record content. Supplying only configuration would not prove traffic was captured.

**Expected:** new invocations create timestamped JSONL objects. If none appear, verify capture destination, endpoint config, permissions, traffic, and delivery delay. Captured payloads can contain sensitive information: use synthetic/non-private data, private S3, retention, and restricted readers.

Next: [Monitoring](../../5.8-Monitoring/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **data capture configured for 100% input and output**.

<figure class="evidence">
  <img src="../../../images/evidence/W6-02-data-capture-config.png" alt="Data Capture configured for 100% input and output" loading="lazy">
  <figcaption>Data Capture configured for 100% input and output — <code>W6-02-data-capture-config.png</code></figcaption>
</figure>

**Technical meaning:** The endpoint configuration establishes capture intent and the S3 destination.

The next screenshot records **inference capture jsonl files stored in s3**.

<figure class="evidence">
  <img src="../../../images/evidence/W6-12-capture-files.png" alt="Inference capture JSONL files stored in S3" loading="lazy">
  <figcaption>Inference capture JSONL files stored in S3 — <code>W6-12-capture-files.png</code></figcaption>
</figure>

**Technical meaning:** Created objects prove real invocations produced persisted capture data, beyond configuration alone.

The next screenshot records **captured record containing endpoint input and output**.

<figure class="evidence">
  <img src="../../../images/evidence/W6-13-capture-record.png" alt="Captured record containing endpoint input and output" loading="lazy">
  <figcaption>Captured record containing endpoint input and output — <code>W6-13-capture-record.png</code></figcaption>
</figure>

**Technical meaning:** The record structure verifies endpointInput, endpointOutput, event metadata, and inference time are available for monitoring.
