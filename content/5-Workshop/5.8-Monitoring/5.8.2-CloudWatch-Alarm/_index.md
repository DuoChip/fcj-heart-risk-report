---
title: "CloudWatch alarm"
weight: 2
chapter: false
pre: " <b>5.8.2.</b> "
---

# CloudWatch metrics and alarm

Publish batch results to namespace `Custom/HeartRisk`:

```text
DriftDetected = 1
DataQualityViolationCount = 6
```

Configure `heart-risk-custom-drift` to enter `ALARM` when `DriftDetected` breaches its threshold, with `TreatMissingData=ignore`.

```bash
aws cloudwatch describe-alarms   --alarm-names heart-risk-custom-drift --region "$AWS_REGION"
```

`W7-04` should prove both custom metrics; `W7-05` the `ALARM` state. Sparse batch metrics originally left/reset the state when empty periods were treated as non-breaching; ignoring missing periods and publishing a fresh datapoint resolved it.

**Errors/security/cost:** use `describe-alarms` if `DescribeAlarmHistory` is denied; grant history access only if needed. Keep dimensions stable and avoid sensitive data in dimensions. Metrics/alarms incur charges.

Next: [Pipeline](../../5.9-Pipeline/).

## Evidence and technical interpretation

The following supplied project screenshots connect the documented configuration to observed AWS state.

The next screenshot records **custom/heartrisk drift metrics in cloudwatch**.

<figure class="evidence">
  <img src="/images/evidence/W7-04-custom-metrics.png" alt="Custom/HeartRisk drift metrics in CloudWatch" loading="lazy">
  <figcaption>Custom/HeartRisk drift metrics in CloudWatch — <code>W7-04-custom-metrics.png</code></figcaption>
</figure>

**Technical meaning:** The metric view proves DriftDetected and DataQualityViolationCount were published outside the unavailable official feature metric.

The next screenshot records **custom drift alarm in alarm state**.

<figure class="evidence">
  <img src="/images/evidence/W7-05-custom-alarm.png" alt="Custom drift alarm in ALARM state" loading="lazy">
  <figcaption>Custom drift alarm in ALARM state — <code>W7-05-custom-alarm.png</code></figcaption>
</figure>

**Technical meaning:** The ALARM state verifies the custom metric can drive an operational signal with sparse missing periods ignored.
