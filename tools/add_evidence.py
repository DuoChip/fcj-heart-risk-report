from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "5-Workshop"


def item(name, en_caption, vi_caption, en_meaning, vi_meaning):
    return (name, en_caption, vi_caption, en_meaning, vi_meaning)


groups = {
    "5.2-Prerequisites": [
        item("AWS-01-selected-region.png", "The project consistently uses the us-east-1 Region", "Dự án sử dụng thống nhất Region us-east-1", "The selected Region matches every resource name and command used later in the workshop.", "Region được chọn khớp với tên tài nguyên và lệnh ở các bước sau."),
        item("AWS-02-budget-overview.png", "Project AWS Budget overview", "Tổng quan AWS Budget của dự án", "The budget is a cost guardrail configured before managed jobs and the continuously billed endpoint.", "Budget là guardrail chi phí được cấu hình trước managed job và endpoint tính phí liên tục."),
        item("AWS-08-sagemaker-role-permissions.png", "Main permissions of the SageMaker execution role", "Các quyền chính của SageMaker execution role", "The execution role supplies managed jobs with AWS permissions without credentials in notebooks.", "Execution role cấp quyền cho managed job mà không đặt credential trong notebook."),
        item("AWS-12-lambda-role-permissions.png", "Lambda execution-role permissions", "Các quyền của Lambda execution role", "A separate Lambda role keeps API-wrapper permissions independent from SageMaker training permissions.", "Role Lambda riêng tách quyền API wrapper khỏi quyền huấn luyện SageMaker."),
    ],
    "5.4-Data-Preparation/5.4.2-SageMaker-Processing": [
        item("W2-01-processing-completed.png", "Managed SageMaker Processing Job completed", "SageMaker Processing Job managed đã hoàn tất", "The completed state proves preprocessing ran on managed infrastructure rather than only in a local notebook.", "Trạng thái hoàn tất chứng minh preprocessing chạy trên hạ tầng managed, không chỉ trong notebook local."),
        item("W2-02-processing-log.png", "Processing log with split and data-quality checks", "Log Processing với kết quả split và kiểm tra chất lượng", "The log verifies 4,900/1,050/1,050 rows, 36 processed features, zero remaining missing values, and train-only fit.", "Log xác minh 4.900/1.050/1.050 dòng, 36 feature, không còn missing và fit train-only."),
        item("W2-03-processed-s3.png", "Processed datasets and artifacts persisted in Amazon S3", "Dataset và artifact sau xử lý được lưu trên Amazon S3", "Persisted outputs make later training and evaluation reproducible and independent of notebook memory.", "Output được lưu giúp training và evaluation tái lập, không phụ thuộc bộ nhớ notebook."),
    ],
    "5.5-Model-Training/5.5.1-Logistic-Regression": [
        item("W3-01-lr-training.png", "Managed Logistic Regression training job", "Training job Logistic Regression managed", "The job state and configuration establish an auditable managed training run.", "Trạng thái và cấu hình tạo bằng chứng cho lần huấn luyện managed có thể truy vết."),
        item("W3-02-lr-metrics.png", "Logistic Regression validation metrics", "Validation metric của Logistic Regression", "These metrics support the final choice by validation AUC and preserve the evaluated threshold of 0.36.", "Các metric hỗ trợ lựa chọn theo validation AUC và ghi nhận threshold 0,36."),
    ],
    "5.5-Model-Training/5.5.2-XGBoost": [
        item("W3-03-xgb-training.png", "Managed XGBoost training job", "Training job XGBoost managed", "A separate job proves the second algorithm was trained as an independent candidate.", "Job riêng chứng minh thuật toán thứ hai được huấn luyện như ứng viên độc lập."),
        item("W3-04-xgb-metrics.png", "Default XGBoost validation metrics", "Validation metric của XGBoost mặc định", "The result documents higher recall but lower precision and ROC-AUC than Logistic Regression.", "Kết quả ghi nhận recall cao hơn nhưng precision và ROC-AUC thấp hơn Logistic Regression."),
    ],
    "5.6-Evaluation-Registry/5.6.1-Evaluation": [
        item("W5-02-evaluation-metrics-and-confusion-matrix.png", "Final test metrics and confusion matrix", "Metric test cuối và confusion matrix", "The evidence proves all three quality gates passed while making the 80 false negatives explicit.", "Minh chứng cho thấy ba quality gate đều pass đồng thời thể hiện rõ 80 âm tính giả."),
    ],
    "5.6-Evaluation-Registry/5.6.2-Model-Registry": [
        item("W5-01-model-versions.png", "Model Registry versions and approval states", "Các version và trạng thái phê duyệt trong Model Registry", "The version list distinguishes Approved versions 1–2 from Pipeline-created version 3 PendingManualApproval.", "Danh sách phân biệt version 1–2 Approved với version 3 PendingManualApproval do Pipeline tạo."),
    ],
    "5.7-Deployment-API/5.7.1-SageMaker-Endpoint": [
        item("W6-01a-endpoint-inservice.png", "Real-time endpoint in InService state", "Endpoint thời gian thực ở trạng thái InService", "InService proves the approved package is available for managed real-time invocation.", "InService chứng minh package đã duyệt sẵn sàng cho suy luận thời gian thực managed."),
        item("W6-01b-endpoint-details.png", "Endpoint configuration and instance details", "Cấu hình endpoint và thông tin instance", "The details connect the deployment to its endpoint configuration and supported ml.m5.large instance.", "Chi tiết liên kết deployment với endpoint configuration và instance ml.m5.large được hỗ trợ."),
        item("W6-03-direct-inference.png", "Successful direct endpoint inference", "Suy luận trực tiếp endpoint thành công", "Direct invocation isolates and verifies the model-serving contract before Lambda and API Gateway are added.", "Gọi trực tiếp cô lập và xác minh contract model serving trước khi thêm Lambda và API Gateway."),
    ],
    "5.7-Deployment-API/5.7.2-Lambda": [
        item("W6-04-lambda-config.png", "Deployed heart-risk-api Lambda configuration", "Cấu hình Lambda heart-risk-api đã triển khai", "The function configuration proves the serverless validation and endpoint-invocation wrapper exists.", "Cấu hình chứng minh wrapper serverless để validate và gọi endpoint đã tồn tại."),
        item("W6-05-lambda-environment.png", "Lambda endpoint and model environment variables", "Biến môi trường endpoint và model của Lambda", "External configuration avoids hard-coding deployment identifiers in application logic; secrets must still never be stored here.", "Cấu hình ngoài tránh hard-code identifier trong logic; vẫn không được lưu secret tại đây."),
        item("W6-06a-lambda-role-overview.png", "Lambda IAM role overview", "Tổng quan IAM role của Lambda", "The role overview establishes the identity used by the API wrapper at runtime.", "Tổng quan role xác định identity mà API wrapper sử dụng khi chạy."),
        item("W6-06b-lambda-role-details.png", "Detailed Lambda endpoint-invocation permission", "Chi tiết quyền gọi endpoint của Lambda", "The detailed policy supports the least-privilege claim by limiting the wrapper to required actions/resources.", "Policy chi tiết hỗ trợ nguyên tắc đặc quyền tối thiểu bằng cách giới hạn action/resource cần thiết."),
    ],
    "5.7-Deployment-API/5.7.3-API-Gateway": [
        item("W6-07-api-routes.png", "HTTP API routes for health and prediction", "Các route HTTP API cho health và prediction", "The route table proves GET /health and POST /predict are wired to the API integration.", "Bảng route chứng minh GET /health và POST /predict được nối với API integration."),
        item("W6-08-health-200.png", "Successful GET /health response", "Response GET /health thành công", "HTTP 200 verifies that the public wrapper path is reachable without invoking a clinical conclusion.", "HTTP 200 xác minh đường dẫn wrapper hoạt động mà không đưa ra kết luận lâm sàng."),
        item("W6-09-predict-200.png", "Successful POST /predict response", "Response POST /predict thành công", "The happy path proves API Gateway, Lambda, and the SageMaker endpoint interoperate and return the documented contract.", "Happy path chứng minh API Gateway, Lambda và SageMaker endpoint tích hợp và trả đúng contract."),
        item("W6-10-predict-400.png", "Missing-field request returns HTTP 400", "Request thiếu field trả HTTP 400", "The controlled client error proves input validation rejects incomplete requests before model invocation.", "Client error có kiểm soát chứng minh validation chặn request thiếu trước khi gọi model."),
        item("W6-11-predict-502.png", "Unavailable prediction service returns HTTP 502", "Prediction service không sẵn sàng trả HTTP 502", "The test proves downstream failures are translated into a stable API error rather than leaking an internal exception.", "Test chứng minh lỗi downstream được đổi thành API error ổn định thay vì lộ exception nội bộ."),
    ],
    "5.7-Deployment-API/5.7.4-Data-Capture": [
        item("W6-02-data-capture-config.png", "Data Capture configured for 100% input and output", "Data Capture được cấu hình 100% input và output", "The endpoint configuration establishes capture intent and the S3 destination.", "Endpoint configuration xác lập cấu hình capture và S3 destination."),
        item("W6-12-capture-files.png", "Inference capture JSONL files stored in S3", "Các file JSONL inference capture lưu trong S3", "Created objects prove real invocations produced persisted capture data, beyond configuration alone.", "Object được tạo chứng minh invocation thật sinh dữ liệu capture, không chỉ có cấu hình."),
        item("W6-13-capture-record.png", "Captured record containing endpoint input and output", "Record capture chứa input và output endpoint", "The record structure verifies endpointInput, endpointOutput, event metadata, and inference time are available for monitoring.", "Cấu trúc record xác minh endpointInput, endpointOutput, metadata và inference time sẵn sàng cho monitoring."),
    ],
    "5.8-Monitoring/5.8.1-Drift-Processing": [
        item("W7-01a-custom-processing-job.png", "Custom drift Processing Job details", "Chi tiết custom drift Processing Job", "The job details prove the fallback drift analysis executed on managed SageMaker infrastructure.", "Chi tiết job chứng minh drift fallback chạy trên hạ tầng SageMaker managed."),
        item("W7-01b-processing-job-list.png", "Custom drift Processing Job history", "Lịch sử custom drift Processing Job", "The job list provides operational traceability across executions.", "Danh sách job cung cấp khả năng truy vết vận hành giữa các execution."),
        item("W7-02-drift-report.png", "Custom drift report summary", "Tóm tắt custom drift report", "The report verifies 4,900 baseline rows, 7,000 current rows, 20 checked features, and six violations.", "Report xác minh 4.900 baseline, 7.000 current, 20 feature và sáu violation."),
        item("W7-03a-drift-features-summary.png", "Summary of six drifted features", "Tóm tắt sáu feature bị drift", "The summary names the affected numeric and categorical features instead of reporting only a binary alarm.", "Tóm tắt nêu tên feature numeric/categorical bị ảnh hưởng thay vì chỉ báo alarm nhị phân."),
        item("W7-03b-drift-features-details.png", "Feature-level custom drift details", "Chi tiết custom drift theo feature", "Feature-level values make the PoC threshold decision inspectable and reproducible.", "Giá trị theo feature giúp quyết định theo ngưỡng PoC có thể kiểm tra và tái lập."),
    ],
    "5.8-Monitoring/5.8.2-CloudWatch-Alarm": [
        item("W7-04-custom-metrics.png", "Custom/HeartRisk drift metrics in CloudWatch", "Drift metric Custom/HeartRisk trong CloudWatch", "The metric view proves DriftDetected and DataQualityViolationCount were published outside the unavailable official feature metric.", "Metric view chứng minh DriftDetected và DataQualityViolationCount được publish thay cho official feature metric không xuất hiện."),
        item("W7-05-custom-alarm.png", "Custom drift alarm in ALARM state", "Custom drift alarm ở trạng thái ALARM", "The ALARM state verifies the custom metric can drive an operational signal with sparse missing periods ignored.", "Trạng thái ALARM xác minh custom metric tạo tín hiệu vận hành khi period thiếu thưa được ignore."),
    ],
    "5.9-Pipeline/5.9.1-Success-Execution": [
        item("W8-01-pipeline-graph.png", "SageMaker Pipeline graph with pass and fail branches", "Graph SageMaker Pipeline với nhánh pass và fail", "The graph makes preprocessing, training, evaluation, condition, registration, and failure dependencies explicit.", "Graph làm rõ phụ thuộc giữa preprocessing, training, evaluation, condition, registration và failure."),
        item("W8-02-pipeline-success.png", "Successful heart-risk-pipeline execution", "Execution heart-risk-pipeline thành công", "The overall Succeeded state proves the end-to-end managed workflow completed.", "Trạng thái Succeeded chứng minh workflow managed end-to-end hoàn tất."),
        item("W8-03-success-steps.png", "Step-level states on the successful path", "Trạng thái từng step trên nhánh thành công", "Every required success-path step completed, providing finer evidence than the overall status alone.", "Mọi step trên nhánh success hoàn tất, cung cấp minh chứng chi tiết hơn trạng thái tổng."),
        item("W8-04-condition-pass.png", "Model quality condition passed", "Điều kiện chất lượng mô hình đã pass", "The condition result proves the evaluated metrics selected the RegisterModel branch.", "Kết quả condition chứng minh metric đánh giá đã chọn nhánh RegisterModel."),
    ],
    "5.9-Pipeline/5.9.2-Intentional-Failure": [
        item("W8-05-pipeline-failure.png", "Pipeline execution failed by design", "Pipeline execution thất bại theo thiết kế", "The failure state is evidence of the tested guardrail, not an implementation defect.", "Trạng thái fail là minh chứng guardrail được test, không phải lỗi hiện thực."),
        item("W8-06-failure-parameters.png", "Intentional AucThreshold override of 0.99", "AucThreshold được ghi đè có chủ đích thành 0,99", "The parameter proves the deliberately unreachable test gate that triggered the failure branch.", "Tham số chứng minh gate test cố ý cao đã kích hoạt nhánh failure."),
        item("W8-07-fail-step.png", "MetricThresholdFailed step blocked registration", "Step MetricThresholdFailed đã chặn đăng ký", "The executed fail step proves a candidate below the gate cannot enter Model Registry.", "Fail step được chạy chứng minh ứng viên dưới gate không thể vào Model Registry."),
    ],
    "5.10-Security-Cost": [
        item("AWS-03-budget-alerts.png", "Budget alerts configured for cost control", "Budget alert được cấu hình để kiểm soát chi phí", "Alert thresholds provide notification guardrails; they do not by themselves prove an exact final bill.", "Ngưỡng alert cung cấp guardrail thông báo; bản thân chúng không chứng minh tổng chi phí."),
        item("AWS-07-s3-tags.png", "Project tags applied to the S3 resource", "Project tag được gắn cho tài nguyên S3", "Tags support ownership and cost/governance identification across project resources.", "Tag hỗ trợ xác định ownership và cost/governance giữa các tài nguyên."),
        item("AWS-09-sagemaker-role-trust.png", "SageMaker execution-role trust relationship", "Trust relationship của SageMaker execution role", "The trust policy limits role assumption to the SageMaker service rather than arbitrary principals.", "Trust policy giới hạn việc assume role cho SageMaker thay vì principal tùy ý."),
        item("AWS-10-sagemaker-s3-policy.png", "SageMaker role S3 access policy", "Policy truy cập S3 của SageMaker role", "The policy documents the storage scope required for data, artifacts, reports, and capture.", "Policy ghi nhận phạm vi storage cần cho data, artifact, report và capture."),
        item("AWS-11-sagemaker-passrole-policy.png", "Scoped iam:PassRole policy for managed jobs", "Policy iam:PassRole có phạm vi cho managed job", "Scoped PassRole enables managed jobs while avoiding a broad role-passing permission.", "PassRole có phạm vi cho phép managed job mà không cấp quyền truyền role quá rộng."),
        item("AWS-13-lambda-role-trust.png", "Lambda execution-role trust relationship", "Trust relationship của Lambda execution role", "The trust relationship establishes Lambda—not clients—as the principal assuming the wrapper role.", "Trust relationship xác lập Lambda, không phải client, là principal assume wrapper role."),
        item("AWS-14-lambda-invoke-policy.png", "Least-privilege Lambda endpoint invocation policy", "Policy Lambda gọi endpoint theo đặc quyền tối thiểu", "The policy restricts Lambda to the required SageMaker endpoint invocation instead of general SageMaker administration.", "Policy giới hạn Lambda ở quyền gọi endpoint cần thiết thay vì quản trị SageMaker chung."),
    ],
}


def refresh_availability_text():
    replacements = {
        "The actual screenshot files were not present in this repository at implementation time; add sanitized originals under `static/images/evidence/` before publication.":
            "The referenced sanitized screenshots are now available under `static/images/evidence/` and are analyzed in the corresponding workshop pages.",
        "Các file ảnh thật chưa có trong repository khi hiện thực; cần thêm bản đã che thông tin nhạy cảm vào `static/images/evidence/` trước khi public.":
            "Các ảnh minh chứng đã được bổ sung vào `static/images/evidence/` và được phân tích tại các trang workshop tương ứng.",
        "These would prove Region, budget, and role setup, but image files are currently TODO.":
            "The supplied screenshots prove the selected Region, budget guardrail, and separate execution-role setup.",
        "Các ảnh sẽ chứng minh Region, budget và role nhưng file hiện vẫn là TODO.":
            "Các ảnh được cung cấp chứng minh Region, budget guardrail và execution role riêng.",
        "actual images remain to be supplied.":
            "the supplied screenshots substantiate both results.",
        "cần bổ sung file ảnh thật.":
            "các ảnh được cung cấp xác nhận hai kết quả.",
        "images are not currently available.":
            "the supplied screenshots substantiate both results.",
        "hiện chưa có file ảnh.":
            "các ảnh được cung cấp xác nhận hai kết quả.",
        "Files are pending.":
            "The supplied screenshots substantiate the configuration and role policy.",
        "Các file ảnh đang chờ bổ sung.":
            "Các ảnh được cung cấp xác nhận cấu hình và role policy.",
        "A screenshot catalog exists in the specification, but the actual files must be supplied before evidence can render.":
            "The supplied evidence catalog is rendered and interpreted throughout the workshop.",
        "Đặc tả có catalog ảnh nhưng cần cung cấp file thật trước khi render minh chứng.":
            "Catalog minh chứng đã được hiển thị và diễn giải xuyên suốt workshop.",
    }
    for path in (ROOT / "content").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")

    # HPO and cleanup are the two factual exceptions to the supplied catalog.
    exceptions = {
        ROOT / "content/1-Worklog/1.5-Week5/_index.md":
            "No dedicated HPO screenshot is available; the configuration and comparison metrics are documented without a broken image.",
        ROOT / "content/1-Worklog/1.5-Week5/_index.vi.md":
            "Không có ảnh HPO riêng; cấu hình và metric so sánh được trình bày mà không tạo link ảnh hỏng.",
        ROOT / "content/1-Worklog/1.12-Week12/_index.md":
            "Cleanup evidence is still TODO and completion is not claimed.",
        ROOT / "content/1-Worklog/1.12-Week12/_index.vi.md":
            "Minh chứng cleanup vẫn là TODO và báo cáo không tuyên bố đã hoàn tất.",
    }
    for path, sentence in exceptions.items():
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if line.startswith("Referenced evidence catalog:") or line.startswith("Danh mục minh chứng tham chiếu:"):
                lines[index] = sentence
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


refresh_availability_text()


def render(items, asset_prefix, vi=False):
    heading = "## Evidence and technical interpretation" if not vi else "## Minh chứng và diễn giải kỹ thuật"
    intro = (
        "The following supplied project screenshots connect the documented configuration to observed AWS state."
        if not vi
        else "Các ảnh dự án được cung cấp dưới đây liên kết cấu hình đã mô tả với trạng thái AWS quan sát được."
    )
    blocks = [heading, "", intro]
    for name, en_caption, vi_caption, en_meaning, vi_meaning in items:
        caption = vi_caption if vi else en_caption
        meaning = vi_meaning if vi else en_meaning
        lead = (
            f"The next screenshot records **{caption.lower()}**."
            if not vi
            else f"Ảnh tiếp theo ghi nhận **{caption.lower()}**."
        )
        label = "Technical meaning" if not vi else "Ý nghĩa kỹ thuật"
        blocks.extend([
            "",
            lead,
            "",
            f'<figure class="evidence">',
            f'  <img src="{asset_prefix}images/evidence/{name}" alt="{caption}" loading="lazy">',
            f"  <figcaption>{caption} — <code>{name}</code></figcaption>",
            "</figure>",
            "",
            f"**{label}:** {meaning}",
        ])
    return "\n".join(blocks) + "\n"


for rel, items in groups.items():
    # A rendered workshop URL has the "5-workshop" segment plus every segment
    # in rel. Walk back to the site root before entering static/images.
    for suffix, vi in (("_index.md", False), ("_index.vi.md", True)):
        asset_prefix = "../" * (1 + len(Path(rel).parts) + int(vi))
        path = CONTENT / rel / suffix
        text = path.read_text(encoding="utf-8")
        marker = "\n## Evidence and technical interpretation" if not vi else "\n## Minh chứng và diễn giải kỹ thuật"
        if marker in text:
            text = text.split(marker, 1)[0].rstrip() + "\n"
        path.write_text(text.rstrip() + "\n\n" + render(items, asset_prefix, vi), encoding="utf-8")

expected = {entry[0] for entries in groups.values() for entry in entries}
actual = {path.name for path in (ROOT / "static" / "images" / "evidence").glob("*.png")}
missing = sorted(expected - actual)
unused = sorted(actual - expected)
if missing:
    raise SystemExit("Missing evidence files: " + ", ".join(missing))
if unused:
    raise SystemExit("Unmapped evidence files: " + ", ".join(unused))

print(f"Attached {len(expected)} evidence images to bilingual workshop pages.")
