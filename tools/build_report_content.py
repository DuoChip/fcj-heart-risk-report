from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"


def page(path, title, weight, pre, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    body = body.strip()
    # The Learn theme already renders the front-matter title as the page H1.
    # Remove only an identical leading body H1 to avoid duplicate headings.
    body = re.sub(
        rf"\A#\s+{re.escape(title)}\s*\n+",
        "",
        body,
        count=1,
    )
    path.write_text(
        f'---\ntitle: "{title}"\nweight: {weight}\nchapter: false\npre: " <b>{pre}</b> "\n---\n\n{body}\n',
        encoding="utf-8",
    )


def pair(folder, en_title, vi_title, weight, pre, en, vi):
    page(folder / "_index.md", en_title, weight, pre, en)
    page(folder / "_index.vi.md", vi_title, weight, pre, vi)


def notice(text):
    return "{{% notice warning %}}\n" + text + "\n{{% /notice %}}"


disclaimer_en = notice("Educational demonstration only; not a medical diagnosis.")
disclaimer_vi = notice("Hệ thống chỉ phục vụ mục đích học tập và minh họa; không phải là chẩn đoán y khoa.")


# The old tree is entirely sample content. Rebuild it deterministically.
if CONTENT.exists():
    shutil.rmtree(CONTENT)
CONTENT.mkdir()

home_en = f"""
# FCAJ Internship Report

## Student information

| Field | Value |
|---|---|
| Full name | TODO: Enter full name |
| Phone number | TODO: Enter phone number |
| Email | TODO: Enter email |
| University | TODO: Enter university |
| Major | TODO: Enter major |
| FCAJ class | TODO: Enter FCAJ class |
| Internship company | TODO: Enter internship company |
| Internship position | TODO: Enter internship position |
| Internship duration | TODO: Enter verified dates |

## Project

**Building and Deploying an End-to-End Heart Attack Risk Prediction System on AWS SageMaker**

This internship project builds an end-to-end machine-learning and MLOps workflow on AWS for heart-attack risk classification. The solution covers data management, managed preprocessing, model training and tuning, quality-gated evaluation, model registration, real-time deployment, API integration, data capture, drift monitoring, CloudWatch alerts, and SageMaker Pipeline automation.

{disclaimer_en}

## Report content

1. [Worklog](1-Worklog/)
2. [Proposal](2-Proposal/)
3. [Blogs Posted](3-BlogsPosted/)
4. [Events Participated](4-EventParticipated/)
5. [Workshop](5-Workshop/)
6. [Self-evaluation](6-Self-evaluation/)
7. [Sharing and Feedback](7-Feedback/)
"""
home_vi = f"""
# Báo cáo thực tập FCAJ

## Thông tin sinh viên

| Trường thông tin | Giá trị |
|---|---|
| Họ và tên | TODO: Nhập họ và tên |
| Số điện thoại | TODO: Nhập số điện thoại |
| Email | TODO: Nhập email |
| Trường | TODO: Nhập tên trường |
| Chuyên ngành | TODO: Nhập chuyên ngành |
| Lớp FCAJ | TODO: Nhập lớp FCAJ |
| Công ty thực tập | TODO: Nhập công ty thực tập |
| Vị trí thực tập | TODO: Nhập vị trí thực tập |
| Thời gian thực tập | TODO: Nhập thời gian đã xác minh |

## Dự án

**Xây dựng và triển khai hệ thống dự đoán nguy cơ đau tim end-to-end trên AWS SageMaker**

Dự án thực tập xây dựng quy trình machine learning và MLOps end-to-end trên AWS cho bài toán phân loại nguy cơ đau tim. Giải pháp bao gồm quản lý dữ liệu, xử lý dữ liệu managed, huấn luyện và tối ưu mô hình, đánh giá bằng quality gate, đăng ký mô hình, triển khai thời gian thực, tích hợp API, Data Capture, giám sát drift, CloudWatch Alarm và tự động hóa bằng SageMaker Pipeline.

{disclaimer_vi}

## Nội dung báo cáo

1. [Nhật ký thực tập](1-Worklog/)
2. [Đề xuất dự án](2-Proposal/)
3. [Blog đã viết](3-BlogsPosted/)
4. [Sự kiện tham gia](4-EventParticipated/)
5. [Workshop](5-Workshop/)
6. [Tự đánh giá](6-Self-evaluation/)
7. [Chia sẻ và phản hồi](7-Feedback/)
"""
page(CONTENT / "_index.md", "FCAJ Internship Report - Heart Risk MLOps", 1, "", home_en)
page(CONTENT / "_index.vi.md", "Báo cáo thực tập FCAJ - Heart Risk MLOps", 1, "", home_vi)


pair(CONTENT / "1-Worklog", "Worklog", "Nhật ký thực tập", 1, "1.",
"""# Twelve-week worklog

This worklog records objectives, managed AWS activities, verified technical results, problems, decisions, evidence references, and next steps. Exact calendar dates remain **TODO** until administrative records are supplied.

| Week | Focus |
|---:|---|
| 1–3 | AWS foundation, data design, managed preprocessing |
| 4–6 | Training, HPO, evaluation, Model Registry |
| 7–9 | Endpoint, API, Data Capture, monitoring baseline |
| 10–12 | Custom drift, Pipeline, documentation and planned cleanup |""",
"""# Nhật ký 12 tuần

Nhật ký ghi lại mục tiêu, hoạt động AWS managed, kết quả kỹ thuật đã xác minh, vấn đề, quyết định, tham chiếu minh chứng và bước tiếp theo. Ngày cụ thể giữ ở trạng thái **TODO** cho đến khi có hồ sơ hành chính.

| Tuần | Trọng tâm |
|---:|---|
| 1–3 | Nền tảng AWS, thiết kế dữ liệu, tiền xử lý managed |
| 4–6 | Huấn luyện, HPO, đánh giá, Model Registry |
| 7–9 | Endpoint, API, Data Capture, monitoring baseline |
| 10–12 | Custom drift, Pipeline, tài liệu và kế hoạch cleanup |""")

weeks = [
("AWS foundation and project planning", "Nền tảng AWS và lập kế hoạch",
 "Reviewed FCAJ requirements; selected the heart-risk MLOps use case and `us-east-1`; configured Budget alerts, IAM roles, private S3 storage, and tags.",
 "Đọc yêu cầu FCAJ; chọn bài toán heart-risk MLOps và `us-east-1`; cấu hình Budget alert, IAM role, S3 private và tags.",
 "AWS environment and cost guardrails were ready; SageMaker and Lambda roles were prepared.",
 "Môi trường AWS và guardrail chi phí sẵn sàng; role cho SageMaker và Lambda đã được chuẩn bị.",
 "IAM scope and unexpected managed-service cost were the main risks.", "Phạm vi IAM và chi phí dịch vụ managed ngoài dự kiến là rủi ro chính.",
 "Used service trust policies, scoped permissions, tags, and budget notifications.", "Dùng trust policy theo dịch vụ, quyền có phạm vi, tags và thông báo ngân sách.",
 "AWS-01, AWS-02, AWS-03, AWS-07–AWS-11"),
("Dataset review and preprocessing design", "Khảo sát dữ liệu và thiết kế tiền xử lý",
 "Inspected 7,000 rows and 22 columns; excluded `patient_id`; identified 11 missing-value columns; designed a stratified 70/15/15 split and train-only preprocessing.",
 "Khảo sát 7.000 dòng, 22 cột; loại `patient_id`; xác định 11 cột thiếu; thiết kế split phân tầng 70/15/15 và fit tiền xử lý chỉ trên train.",
 "Produced 36 processed features, no duplicates, and zero missing values after processing.", "Tạo 36 feature sau xử lý, không có dòng trùng và không còn giá trị thiếu.",
 "Fitting transformations before splitting could leak validation/test information.", "Fit phép biến đổi trước khi split có thể làm rò rỉ thông tin validation/test.",
 "Split first; fit median/mode imputation, one-hot encoding, and scaling on training data only.", "Split trước; fit median/mode imputation, one-hot encoding và scaling chỉ trên train.",
 "W2-02"),
("Managed Processing Job", "SageMaker Processing Job",
 "Uploaded the raw dataset and manifest to S3, then ran managed preprocessing and persisted train, validation, test, baseline, reports, and artifacts.",
 "Tải dữ liệu raw và manifest lên S3, chạy managed preprocessing và lưu train, validation, test, baseline, report, artifact.",
 "Managed preprocessing completed with split sizes 4,900/1,050/1,050.", "Managed preprocessing hoàn tất với kích thước 4.900/1.050/1.050.",
 "Outputs needed stable paths and repeatable execution.", "Output cần đường dẫn ổn định và khả năng chạy lặp.",
 "Used an S3-first layout and reusable preprocessing artifact.", "Dùng bố cục S3-first và artifact tiền xử lý tái sử dụng.",
 "W2-01, W2-03"),
("Logistic Regression and XGBoost", "Logistic Regression và XGBoost",
 "Ran managed Logistic Regression and default XGBoost training jobs and compared validation behavior.",
 "Chạy managed training job cho Logistic Regression và XGBoost mặc định, sau đó so sánh trên validation.",
 "LR AUC 0.863949; XGBoost AUC 0.854283. XGBoost recall was higher but precision and AUC were lower.",
 "LR AUC 0,863949; XGBoost AUC 0,854283. XGBoost có recall cao hơn nhưng precision và AUC thấp hơn.",
 "A single metric did not describe the error trade-off.", "Một metric không diễn tả đủ đánh đổi lỗi.",
 "Compared AUC, F1, recall, precision, and the LR threshold 0.36.", "So sánh AUC, F1, recall, precision và threshold 0,36 của LR.",
 "W3-01–W3-04"),
("HPO and model selection", "HPO và lựa chọn mô hình",
 "Ran three sequential Bayesian XGBoost HPO trials for `eta`, `max-depth`, and `min-child-weight`; optimized `validation:auc`.",
 "Chạy ba trial Bayesian HPO tuần tự cho `eta`, `max-depth`, `min-child-weight`; tối ưu `validation:auc`.",
 "Best HPO AUC was 0.860982; LR remained the candidate based on validation AUC.", "HPO AUC tốt nhất là 0,860982; LR vẫn là ứng viên theo validation AUC.",
 "The test set must not influence model or trial selection.", "Test set không được ảnh hưởng lựa chọn model hoặc trial.",
 "Selected only with validation results and reserved test for one final evaluation.", "Chỉ chọn theo validation và dành test cho một lần đánh giá cuối.",
 "No dedicated HPO screenshot is available; metrics/configuration are documented without a broken image."),
("Final evaluation and Model Registry", "Đánh giá cuối và Model Registry",
 "Evaluated LR once on test data, checked three quality gates, and registered versioned packages with manual approval.",
 "Đánh giá LR một lần trên test, kiểm tra ba quality gate và đăng ký package có version với phê duyệt thủ công.",
 "AUC 0.885515, F1 0.768903, recall 0.818594; versions 1 and 2 Approved; version 3 later PendingManualApproval.",
 "AUC 0,885515, F1 0,768903, recall 0,818594; version 1 và 2 Approved; version 3 sau đó PendingManualApproval.",
 "False negatives require explicit interpretation without clinical claims.", "Âm tính giả cần được giải thích rõ nhưng không đưa ra tuyên bố lâm sàng.",
 "Reported all 80 false negatives and retained manual approval.", "Báo cáo đủ 80 âm tính giả và giữ phê duyệt thủ công.",
 "W5-01, W5-02"),
("Endpoint and direct inference", "Endpoint và suy luận trực tiếp",
 "Deployed Model Package version 2 to `heart-risk-endpoint`, enabled 100% input/output Data Capture, and invoked the endpoint directly.",
 "Triển khai Model Package version 2 lên `heart-risk-endpoint`, bật 100% Data Capture input/output và gọi endpoint trực tiếp.",
 "The `ml.m5.large` endpoint reached `InService` and returned the prediction contract.", "Endpoint `ml.m5.large` đạt `InService` và trả đúng contract dự đoán.",
 "`ml.t3.medium` was unsupported by the package deployment configuration.", "`ml.t3.medium` không được cấu hình package hỗ trợ.",
 "Changed the allowed deployment instance to `ml.m5.large`.", "Đổi instance triển khai được phép sang `ml.m5.large`.",
 "W6-01a, W6-01b, W6-02, W6-03"),
("Lambda and API Gateway", "Lambda và API Gateway",
 "Created `heart-risk-api`, configured environment variables and least-privilege endpoint invocation, then exposed `GET /health` and `POST /predict`.",
 "Tạo `heart-risk-api`, cấu hình biến môi trường và quyền gọi endpoint tối thiểu, sau đó cung cấp `GET /health`, `POST /predict`.",
 "Verified HTTP 200 health/prediction, 400 missing fields, and controlled 502 downstream failure.", "Xác minh HTTP 200 health/prediction, 400 thiếu field và 502 có kiểm soát khi downstream lỗi.",
 "Public errors must not reveal internals or active API URLs.", "Lỗi public không được lộ nội bộ hoặc URL API đang hoạt động.",
 "Validated inputs and returned safe structured errors.", "Validate input và trả lỗi có cấu trúc an toàn.",
 "W6-04–W6-11"),
("Data Capture and monitoring baseline", "Data Capture và monitoring baseline",
 "Verified JSONL capture records containing endpoint input/output, metadata, and inference time; prepared baseline/current data and an hourly Model Monitor schedule.",
 "Xác minh JSONL chứa input/output endpoint, metadata, inference time; chuẩn bị baseline/current và lịch Model Monitor mỗi giờ.",
 "Real traffic was captured, but the expected official feature-level CloudWatch metric was not observed.", "Traffic thật đã được capture nhưng không quan sát thấy feature-level CloudWatch metric mong đợi.",
 "The missing official metric prevented evidence-based alerting.", "Thiếu metric chính thức làm cản trở cảnh báo có minh chứng.",
 "Documented the limitation and designed a custom fallback.", "Ghi rõ giới hạn và thiết kế custom fallback.",
 "W6-12, W6-13"),
("Custom drift fallback and CloudWatch", "Custom drift fallback và CloudWatch",
 "Ran a custom Processing Job over 20 features and published `DriftDetected` and `DataQualityViolationCount` to `Custom/HeartRisk`.",
 "Chạy custom Processing Job trên 20 feature và publish `DriftDetected`, `DataQualityViolationCount` vào `Custom/HeartRisk`.",
 "Six features drifted; values were 1 and 6; alarm reached `ALARM`.", "Sáu feature drift; metric bằng 1 và 6; alarm đạt `ALARM`.",
 "Sparse batch metrics caused missing periods to reset alarm behavior.", "Metric batch thưa làm period thiếu ảnh hưởng trạng thái alarm.",
 "Set `TreatMissingData=ignore` and published a fresh datapoint.", "Đặt `TreatMissingData=ignore` và publish datapoint mới.",
 "W7-01a–W7-05"),
("SageMaker Pipeline", "SageMaker Pipeline",
 "Built preprocessing, training, evaluation, condition, registration, and fail steps; ran pass and intentional-fail executions.",
 "Xây các bước preprocessing, training, evaluation, condition, registration, fail; chạy luồng pass và fail có chủ đích.",
 "Success registered version 3 as PendingManualApproval; AUC threshold 0.99 blocked registration by design.",
 "Luồng thành công đăng ký version 3 PendingManualApproval; ngưỡng AUC 0,99 chặn đăng ký theo thiết kế.",
 "The pipeline was absent before its first upsert.", "Pipeline chưa tồn tại trước lần upsert đầu.",
 "Ran the pipeline definition/upsert before listing or executing it.", "Chạy định nghĩa/upsert trước khi list hoặc execute.",
 "W8-01–W8-07"),
("Documentation, review, and cleanup", "Tài liệu, rà soát và cleanup",
 "Organized the bilingual Hugo report, workshop, proposal, evaluation, security/cost review, and cleanup runbook.",
 "Tổ chức báo cáo Hugo song ngữ, workshop, proposal, đánh giá, rà soát security/cost và runbook cleanup.",
 "The documentation is prepared; cleanup completion is not claimed.", "Tài liệu đã được chuẩn bị; chưa tuyên bố cleanup đã hoàn tất.",
 "Evidence must be retained before deleting resources.", "Cần giữ minh chứng trước khi xóa tài nguyên.",
 "Delete in dependency order only after evidence review.", "Chỉ xóa theo thứ tự phụ thuộc sau khi rà soát minh chứng.",
 "TODO: Add cleanup log, deleted-resource verification, and stopped Studio/JupyterLab evidence."),
]

for i, w in enumerate(weeks, 1):
    en_t, vi_t, work_en, work_vi, result_en, result_vi, problem_en, problem_vi, resolution_en, resolution_vi, evidence = w
    en = f"""# Week {i}: {en_t}

**Dates:** TODO: Enter verified week dates

## Objectives and work completed

{work_en}

## Technical activities

The work followed the project S3-first, managed-job, least-privilege, and reproducibility conventions. Commands and resource names are documented in the workshop.

## Problem and decision

- **Problem:** {problem_en}
- **Resolution/decision:** {resolution_en}

## Result

{result_en}

## Evidence

Referenced evidence catalog: `{evidence}`. The actual screenshot files were not present in this repository at implementation time; add sanitized originals under `static/images/evidence/` before publication.

## Reflection and next step

The next week builds on these versioned outputs rather than repeating manual notebook state."""
    vi = f"""# Tuần {i}: {vi_t}

**Thời gian:** TODO: Nhập ngày đã xác minh

## Mục tiêu và công việc hoàn thành

{work_vi}

## Hoạt động kỹ thuật

Công việc tuân theo các nguyên tắc S3-first, managed job, đặc quyền tối thiểu và khả năng tái lập. Lệnh và tên tài nguyên được trình bày trong workshop.

## Vấn đề và quyết định

- **Vấn đề:** {problem_vi}
- **Cách xử lý/quyết định:** {resolution_vi}

## Kết quả

{result_vi}

## Minh chứng

Danh mục minh chứng tham chiếu: `{evidence}`. Các file ảnh thật chưa có trong repository khi hiện thực; cần thêm bản đã che thông tin nhạy cảm vào `static/images/evidence/` trước khi public.

## Nhìn lại và bước tiếp theo

Tuần kế tiếp sử dụng các output có version thay vì phụ thuộc trạng thái notebook thủ công."""
    pair(CONTENT / "1-Worklog" / f"1.{i}-Week{i}", f"Week {i}: {en_t}", f"Tuần {i}: {vi_t}", i, f"1.{i}.", en, vi)


proposal_en = f"""# Project proposal

## 1. Executive summary

The proposal plans an educational MLOps proof of concept that turns a local heart-risk classification experiment into a reproducible AWS workflow. It is not intended for clinical use.

## 2. Background and problem statement

A notebook alone lacks reproducible managed processing, model version management, quality gates, real-time deployment, API access, monitoring/alerting, and an automated pass/fail workflow.

## 3. Target users

- Students and engineers learning AWS SageMaker MLOps
- ML teams evaluating a reproducible PoC workflow
- Application developers integrating a non-clinical prediction API

## 4. Objectives and scope

The scope covers versioned data, leakage-safe processing, LR/XGBoost training and HPO, final evaluation, Model Registry, one real-time endpoint, Lambda/API Gateway, Data Capture, custom drift monitoring, CloudWatch, Pipeline automation, documentation, and cleanup. Clinical validation, diagnosis, production authentication, CI/CD, IaC, fairness analysis, and automated retraining are out of scope.

## 5. Expected outputs

Versioned S3 data/manifest; train/validation/test data; preprocessing/model artifacts; HPO and evaluation reports; Registry versions; approved deployed model; endpoint and API; capture JSONL; drift report; metrics/alarm; Pipeline pass/fail executions; cleanup runbook and, after execution, evidence.

## 6. Success criteria

| Gate/check | Target |
|---|---:|
| Test ROC-AUC | ≥ 0.84 |
| Test F1 | ≥ 0.70 |
| Test recall | ≥ 0.65 |
| API tests | 200, 400, 502 handled |
| Monitoring | custom metrics and alarm |
| Pipeline | pass registers; fail blocks |

## 7. Solution architecture

![Heart-risk MLOps architecture](../images/architecture/heart-risk-architecture.svg)

The diagram separates offline data/training, online inference, monitoring, and the Pipeline quality gate. IAM roles form service boundaries; S3 remains private.

## 8. AWS services and rationale

| Service | Selection rationale |
|---|---|
| Amazon S3 | Durable storage for raw/processed data, capture, reports, artifacts |
| SageMaker Processing/Training/HPO | Reproducible jobs independent of a notebook |
| Model Registry | Versions, metadata, manual approval |
| SageMaker Endpoint | Managed real-time inference |
| Lambda and API Gateway | Validation wrapper and HTTP integration |
| CloudWatch | Logs, custom metrics, alarms |
| SageMaker Pipeline | Automated quality-gated workflow |
| AWS Budgets | Cost visibility and alerts |

## 9. Data and ML approach

The 7,000-row dataset has 22 original columns. `patient_id` is excluded, leaving 20 raw features and target `heart_attack_risk` (~42% positive). A stratified 70/15/15 split yields 4,900/1,050/1,050 rows. The preprocessor is fitted only on train: numeric median imputation and scaling, categorical most-frequent imputation and one-hot encoding, producing 36 features with zero missing values.

## 10. Twelve-week timeline

Weeks 1–3 establish AWS and data processing; 4–6 train, tune, evaluate, and register; 7–9 deploy, expose, and capture; 10–12 monitor, automate, document, and prepare cleanup.

## 11. Budget and controls

Budget alerts, tags, only three sequential HPO trials, one endpoint instance, job-based processing/training, and dependency-ordered cleanup constrain spend. **No exact final cost is claimed without Cost Explorer evidence.**

## 12. Risks and mitigation

| Risk | Mitigation |
|---|---|
| Data leakage | Split first; fit preprocessing on train only |
| Over-permissioned roles | Separate trust policies and scoped S3/endpoint access |
| Endpoint cost | One PoC instance; delete after evidence |
| Missing official drift metric | Custom managed drift job and explicit PoC thresholds |
| Unsafe interpretation | Disclaimer, limitations, no clinical users/claims |

## 13. Expected benefits

The project demonstrates reproducibility, traceability, operational monitoring, controlled promotion, and failure-safe automation across AWS services.

## 14. Ethical and medical limitations

The dataset is non-clinical; no fairness assessment or probability calibration is performed. Predictions must not guide care.

{disclaimer_en}
"""
proposal_vi = proposal_en.replace("# Project proposal", "# Đề xuất dự án").replace(
"The proposal plans an educational MLOps proof of concept that turns a local heart-risk classification experiment into a reproducible AWS workflow. It is not intended for clinical use.",
"Đề xuất lập kế hoạch cho một proof of concept MLOps phục vụ học tập, chuyển thử nghiệm phân loại heart-risk cục bộ thành quy trình AWS có thể tái lập; không dùng cho lâm sàng.")
# Replace with a fully reviewed Vietnamese version for the substantive sections.
proposal_vi = f"""# Đề xuất dự án

## 1. Tóm tắt điều hành

Dự án lập kế hoạch xây dựng proof of concept MLOps phục vụ học tập, chuyển thử nghiệm phân loại heart-risk trên notebook thành quy trình AWS có thể tái lập.

## 2. Bối cảnh và vấn đề

Notebook cục bộ thiếu tiền xử lý managed có thể tái lập, quản lý version mô hình, quality gate, real-time deployment, API, monitoring/cảnh báo và workflow pass/fail tự động.

## 3. Đối tượng sử dụng

- Sinh viên và kỹ sư học SageMaker MLOps
- Nhóm ML đánh giá một workflow PoC có thể tái lập
- Lập trình viên tích hợp API dự đoán phi lâm sàng

## 4. Mục tiêu và phạm vi

Phạm vi gồm dữ liệu có version, preprocessing chống leakage, LR/XGBoost và HPO, đánh giá cuối, Model Registry, một endpoint, Lambda/API Gateway, Data Capture, custom drift, CloudWatch, Pipeline, tài liệu và cleanup. Không gồm xác thực lâm sàng, chẩn đoán, production authentication, CI/CD, IaC, fairness hay automated retraining.

## 5. Đầu ra mong đợi

Dữ liệu/manifest S3 có version; bộ train/validation/test; artifact preprocessing/model; báo cáo HPO và đánh giá; Registry versions; model được duyệt và triển khai; endpoint/API; JSONL capture; drift report; metric/alarm; Pipeline pass/fail; runbook cleanup và minh chứng sau khi thực hiện.

## 6. Tiêu chí thành công

| Gate/check | Mục tiêu |
|---|---:|
| Test ROC-AUC | ≥ 0,84 |
| Test F1 | ≥ 0,70 |
| Test recall | ≥ 0,65 |
| API | xử lý 200, 400, 502 |
| Monitoring | custom metric và alarm |
| Pipeline | pass đăng ký; fail chặn |

## 7. Kiến trúc giải pháp

![Kiến trúc Heart-risk MLOps](../../images/architecture/heart-risk-architecture.svg)

Sơ đồ tách offline data/training, online inference, monitoring và Pipeline quality gate. IAM role tạo ranh giới dịch vụ; S3 giữ private.

## 8. Dịch vụ AWS và lý do lựa chọn

| Dịch vụ | Lý do |
|---|---|
| Amazon S3 | Lưu bền raw/processed data, capture, report, artifact |
| SageMaker Processing/Training/HPO | Job tái lập, độc lập notebook |
| Model Registry | Version, metadata, phê duyệt thủ công |
| SageMaker Endpoint | Suy luận thời gian thực managed |
| Lambda và API Gateway | Wrapper validate và tích hợp HTTP |
| CloudWatch | Log, custom metric, alarm |
| SageMaker Pipeline | Workflow tự động có quality gate |
| AWS Budgets | Theo dõi và cảnh báo chi phí |

## 9. Phương pháp dữ liệu và ML

Dataset có 7.000 dòng, 22 cột. Loại `patient_id` còn 20 raw feature và target `heart_attack_risk` (~42% positive). Split phân tầng 70/15/15 tạo 4.900/1.050/1.050 dòng. Preprocessor chỉ fit trên train: numeric median imputation và scaling; categorical most-frequent imputation và one-hot encoding; tạo 36 feature, không còn missing.

## 10. Timeline 12 tuần

Tuần 1–3 xây nền AWS và processing; 4–6 train, tune, evaluate, register; 7–9 deploy, API, capture; 10–12 monitor, automate, document và chuẩn bị cleanup.

## 11. Ngân sách và kiểm soát chi phí

Budget alert, tags, chỉ ba HPO trial tuần tự, một endpoint, tài nguyên dạng job và cleanup theo phụ thuộc giúp giới hạn chi phí. **Không tuyên bố tổng chi phí chính xác khi chưa có Cost Explorer.**

## 12. Rủi ro và giảm thiểu

| Rủi ro | Giảm thiểu |
|---|---|
| Data leakage | Split trước; fit preprocessing chỉ trên train |
| Role quá quyền | Trust policy riêng và quyền S3/endpoint có phạm vi |
| Chi phí endpoint | Một instance PoC; xóa sau khi lưu minh chứng |
| Thiếu official drift metric | Custom managed job và ngưỡng PoC rõ ràng |
| Diễn giải không an toàn | Disclaimer, limitation, không có claim/user lâm sàng |

## 13. Lợi ích mong đợi

Dự án minh họa khả năng tái lập, truy vết, monitoring vận hành, promotion có kiểm soát và automation an toàn khi thất bại.

## 14. Giới hạn đạo đức và y khoa

Dataset phi lâm sàng; chưa đánh giá fairness hay calibration xác suất. Không dùng dự đoán để hướng dẫn chăm sóc sức khỏe.

{disclaimer_vi}
"""
pair(CONTENT / "2-Proposal", "Proposal", "Đề xuất dự án", 2, "2.", proposal_en, proposal_vi)


pair(CONTENT / "3-BlogsPosted", "Blog drafts", "Bản nháp blog", 3, "3.",
"""# Blog drafts

Three project-specific bilingual drafts are prepared below. They are **not claimed as published**.

- TODO: Add verified AWS Study Group publication URLs
- TODO: Add publication dates and screenshots""",
"""# Bản nháp blog

Ba bản nháp song ngữ theo dự án được chuẩn bị bên dưới. Báo cáo **không tuyên bố đã xuất bản**.

- TODO: Thêm URL AWS Study Group đã xác minh
- TODO: Thêm ngày xuất bản và ảnh minh chứng""")

blogs = [
("Cost Optimization for a Personal SageMaker MLOps Project", "Tối ưu chi phí cho dự án MLOps cá nhân trên SageMaker",
 "Continuously running endpoints differ from processing and training jobs that stop when work ends. The PoC therefore used three sequential HPO trials, one endpoint instance, Budget alerts, tags, and a cleanup runbook.",
 "Endpoint chạy liên tục khác với Processing/Training Job kết thúc sau công việc. PoC vì vậy giới hạn ba HPO trial tuần tự, một endpoint, Budget alert, tags và runbook cleanup.",
 "List active endpoints before deletion:\n\n```bash\naws sagemaker list-endpoints --region \"$AWS_REGION\" --status-equals InService\n```\n\nRetain reports and sanitized evidence before deleting compute. Keep the S3 bucket private and never embed credentials.",
 "Liệt kê endpoint đang chạy trước khi xóa:\n\n```bash\naws sagemaker list-endpoints --region \"$AWS_REGION\" --status-equals InService\n```\n\nGiữ report và minh chứng đã che thông tin trước khi xóa compute. Giữ S3 private và không nhúng credential."),
("Model Registry and Quality Gates in SageMaker Pipelines", "Model Registry và Quality Gate trong SageMaker Pipeline",
 "Model versions separate trained artifacts from promotion decisions. Versions 1 and 2 were Approved; version 2 was deployed; the Pipeline created version 3 as PendingManualApproval.",
 "Model version tách artifact đã train khỏi quyết định promotion. Version 1 và 2 Approved; version 2 được deploy; Pipeline tạo version 3 PendingManualApproval.",
 "The `ConditionStep` checks AUC ≥ 0.84, F1 ≥ 0.70, and recall ≥ 0.65. The pass branch registers; the fail branch raises `MetricThresholdFailed`. An intentional AUC threshold of 0.99 verified that registration is blocked. Auto-deployment is excluded so a person reviews evidence and cost.",
 "`ConditionStep` kiểm tra AUC ≥ 0,84, F1 ≥ 0,70 và recall ≥ 0,65. Nhánh pass đăng ký; nhánh fail tạo `MetricThresholdFailed`. Ngưỡng AUC 0,99 có chủ đích xác minh việc chặn đăng ký. Không auto-deploy để người phụ trách rà soát minh chứng và chi phí."),
("Custom Data Drift Monitoring with SageMaker Processing and CloudWatch", "Giám sát Data Drift tùy chỉnh bằng SageMaker Processing và CloudWatch",
 "Data Capture provides current inference records, while the 4,900-row training baseline anchors comparison. The expected official feature metric was not observed, so the project implemented a transparent fallback.",
 "Data Capture cung cấp record suy luận hiện tại, còn baseline 4.900 dòng từ train làm mốc. Không quan sát thấy official feature metric nên dự án tạo fallback minh bạch.",
 "A custom Processing Job checked 20 features: numeric standardized mean shift > 0.5 and categorical total variation distance > 0.20. Six features drifted. It published `DriftDetected=1` and `DataQualityViolationCount=6`; `TreatMissingData=ignore` prevented sparse batch periods from overwriting the useful state. These are PoC rules, not universal or clinical thresholds.",
 "Custom Processing Job kiểm tra 20 feature: standardized mean shift numeric > 0,5 và total variation distance categorical > 0,20. Sáu feature drift. Job publish `DriftDetected=1`, `DataQualityViolationCount=6`; `TreatMissingData=ignore` tránh period batch thưa làm sai trạng thái hữu ích. Đây là quy tắc PoC, không phải ngưỡng phổ quát hay lâm sàng.")
]
for i, (et, vt, introe, introv, impl_e, impl_v) in enumerate(blogs, 1):
    common_end_en = """## Result and lessons

The implementation favors measurable evidence, explicit failure behavior, and cost-aware operation. IAM roles replace hard-coded keys; active URLs and sensitive ARNs must be masked.

## Publication status

- TODO: AWS Study Group publication URL
- TODO: Publication date
- TODO: Publication screenshot"""
    common_end_vi = """## Kết quả và bài học

Giải pháp ưu tiên minh chứng đo được, hành vi lỗi rõ ràng và vận hành có ý thức chi phí. IAM role thay access key hard-code; cần che URL đang active và ARN nhạy cảm.

## Trạng thái xuất bản

- TODO: URL bài AWS Study Group
- TODO: Ngày xuất bản
- TODO: Ảnh minh chứng xuất bản"""
    en = f"# {et}\n\n## Introduction and motivation\n\n{introe}\n\n## Flow and implementation\n\n{impl_e}\n\n{common_end_en}"
    vi = f"# {vt}\n\n## Giới thiệu và động lực\n\n{introv}\n\n## Luồng và hiện thực\n\n{impl_v}\n\n{common_end_vi}"
    pair(CONTENT / "3-BlogsPosted" / f"3.{i}-Blog{i}", et, vt, i, f"3.{i}.", en, vi)


pair(CONTENT / "4-EventParticipated", "Events Participated", "Sự kiện đã tham gia", 4, "4.",
"""# Events participated

No verified event information was supplied. The placeholder page below prevents the sample event from being presented as personal experience.""",
"""# Sự kiện đã tham gia

Chưa có thông tin sự kiện đã xác minh. Trang placeholder bên dưới bảo đảm sự kiện mẫu không bị trình bày như trải nghiệm cá nhân.""")
pair(CONTENT / "4-EventParticipated" / "4.1-Event1", "Verified event placeholder", "Thông tin sự kiện chờ xác minh", 1, "4.1.",
"""# To be completed with verified event information

| Field | Value |
|---|---|
| Event name | TODO |
| Date and time | TODO |
| Location/online platform | TODO |
| Role | TODO |
| Organizer | TODO |
| Main content | TODO |
| Personal contribution | TODO |
| Key learning | TODO |
| Evidence image/video/certificate | TODO |
| Public link | TODO |""",
"""# Sẽ hoàn thiện khi có thông tin sự kiện đã xác minh

| Trường | Giá trị |
|---|---|
| Tên sự kiện | TODO |
| Ngày và giờ | TODO |
| Địa điểm/nền tảng online | TODO |
| Vai trò | TODO |
| Đơn vị tổ chức | TODO |
| Nội dung chính | TODO |
| Đóng góp cá nhân | TODO |
| Bài học | TODO |
| Ảnh/video/chứng nhận | TODO |
| Link công khai | TODO |""")


workshop_root_en = f"""# Building and Deploying an End-to-End Heart Attack Risk Prediction System on AWS SageMaker

This workshop builds a reproducible end-to-end MLOps proof of concept for binary heart-attack risk classification: prepare data, compare models, enforce quality gates, register and approve, deploy a real-time endpoint, expose an API, capture traffic, detect drift, alert, and automate with SageMaker Pipelines.

**Audience:** learners familiar with Python, AWS fundamentals, and basic classification.  
**Duration:** approximately 8–12 guided hours, excluding job waiting time.  
**Services:** S3, SageMaker Processing/Training/HPO/Registry/Endpoint/Model Monitor/Pipelines, Lambda, API Gateway, CloudWatch, IAM, Budgets.

{notice("AWS resources can incur charges, especially a continuously running endpoint. Use Budget alerts and complete the cleanup runbook.")}

{disclaimer_en}

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
"""
workshop_root_vi = f"""# Xây dựng và triển khai hệ thống dự đoán nguy cơ đau tim end-to-end trên AWS SageMaker

Workshop xây dựng proof of concept MLOps có thể tái lập cho phân loại nguy cơ đau tim: chuẩn bị dữ liệu, so sánh model, quality gate, đăng ký/phê duyệt, endpoint, API, capture traffic, phát hiện drift, cảnh báo và SageMaker Pipelines.

**Đối tượng:** người học biết Python, AWS cơ bản và bài toán phân loại.  
**Thời lượng:** khoảng 8–12 giờ thực hành, không gồm thời gian chờ job.  
**Dịch vụ:** S3, SageMaker Processing/Training/HPO/Registry/Endpoint/Model Monitor/Pipelines, Lambda, API Gateway, CloudWatch, IAM, Budgets.

{notice("Tài nguyên AWS có thể phát sinh phí, đặc biệt endpoint chạy liên tục. Hãy dùng Budget alert và hoàn tất runbook cleanup.")}

{disclaimer_vi}

![Kiến trúc Heart-risk MLOps](../../images/architecture/heart-risk-architecture.svg)

## Mục tiêu học tập và điều hướng

1. [Tổng quan](5.1-Overview/)
2. [Điều kiện tiên quyết](5.2-Prerequisites/)
3. [Kiến trúc](5.3-Architecture/)
4. [Chuẩn bị dữ liệu](5.4-Data-Preparation/)
5. [Huấn luyện mô hình](5.5-Model-Training/)
6. [Đánh giá và Registry](5.6-Evaluation-Registry/)
7. [Triển khai và API](5.7-Deployment-API/)
8. [Monitoring](5.8-Monitoring/)
9. [Pipeline](5.9-Pipeline/)
10. [Bảo mật và chi phí](5.10-Security-Cost/)
11. [Cleanup](5.11-Cleanup/)
12. [Kết quả và giới hạn](5.12-Results-Limitations/)
"""
pair(CONTENT / "5-Workshop", "Heart Risk MLOps Workshop", "Workshop Heart Risk MLOps", 5, "5.", workshop_root_en, workshop_root_vi)


def workshop_pair(slug, weight, en_title, vi_title, en_body, vi_body):
    pair(CONTENT / "5-Workshop" / slug, en_title, vi_title, weight, f"5.{weight}.", en_body, vi_body)


overview_en = f"""# Workshop overview

## Objective and success criteria

Build a traceable flow from versioned raw data to monitored API and quality-gated Pipeline. The final LR model achieved test AUC 0.885515, F1 0.768903, and recall 0.818594, passing gates 0.84/0.70/0.65.

| Component | Verified result |
|---|---|
| Processing | 4,900/1,050/1,050; 36 features; no missing values |
| Registry/deployment | version 2 Approved and deployed |
| API | 200, 400, and controlled 502 |
| Drift | 6/20 violations; alarm `ALARM` |
| Pipeline | success registers v3 pending; intentional fail blocks |

![Architecture separating offline, online, monitoring and gate flows](../../images/architecture/heart-risk-architecture.svg)

The diagram establishes service boundaries and makes the S3-centered artifact flow explicit.

## Personal Contributions and Customizations

The project replaces the sample use case with a custom dataset; adds SHA-256 versioning/idempotent upload, train-only preprocessing, LR/XGBoost comparison, Bayesian HPO, three quality gates, Registry/manual approval, endpoint/Lambda/API tests (200/400/502), Data Capture, custom drift fallback and metrics, sparse-alarm resolution, Pipeline pass/fail paths, and cautious medical limitations.

## Prerequisite, errors, cost and next step

Use `us-east-1`, private S3, service roles, Budget alerts, and no credentials in code. A screenshot catalog exists in the specification, but the actual files must be supplied before evidence can render.

{disclaimer_en}

Next: [Prerequisites](../5.2-Prerequisites/)."""
overview_vi = f"""# Tổng quan workshop

## Mục tiêu và tiêu chí thành công

Xây luồng truy vết từ raw data có version đến API được monitor và Pipeline có quality gate. LR cuối đạt test AUC 0,885515, F1 0,768903, recall 0,818594, vượt gate 0,84/0,70/0,65.

| Thành phần | Kết quả đã xác minh |
|---|---|
| Processing | 4.900/1.050/1.050; 36 feature; không missing |
| Registry/deployment | version 2 Approved và deployed |
| API | 200, 400 và 502 có kiểm soát |
| Drift | 6/20 violation; alarm `ALARM` |
| Pipeline | success đăng ký v3 pending; fail chặn |

![Kiến trúc tách luồng offline, online, monitoring và gate](../../../images/architecture/heart-risk-architecture.svg)

Sơ đồ làm rõ ranh giới dịch vụ và luồng artifact lấy S3 làm trung tâm.

## Đóng góp và tùy biến cá nhân

Dự án thay use case mẫu bằng dataset riêng; thêm SHA-256/idempotent upload, train-only preprocessing, so sánh LR/XGBoost, Bayesian HPO, ba quality gate, Registry/manual approval, endpoint/Lambda/API test 200/400/502, Data Capture, custom drift/metric, xử lý sparse alarm, Pipeline pass/fail và ngôn ngữ y khoa thận trọng.

## Điều kiện, lỗi, chi phí và bước tiếp

Dùng `us-east-1`, S3 private, service role, Budget alert và không đặt credential trong code. Đặc tả có catalog ảnh nhưng cần cung cấp file thật trước khi render minh chứng.

{disclaimer_vi}

Tiếp theo: [Điều kiện tiên quyết](../5.2-Prerequisites/)."""
workshop_pair("5.1-Overview", 1, "Overview", "Tổng quan", overview_en, overview_vi)

prereq_en = """# Prerequisites

## Objective

Prepare a controlled environment before creating billed resources.

1. Use an AWS account and select `us-east-1`.
2. Install Git, Python 3, AWS CLI v2, and Hugo extended 0.134.3 or compatible.
3. Configure SageMaker Studio/JupyterLab without embedding access keys.
4. Create the private bucket and SageMaker/Lambda execution roles.
5. Configure AWS Budget alerts.

```bash
export AWS_REGION="us-east-1"
export PROJECT_BUCKET="heart-risk-mlops-<ACCOUNT_ID>-us-east-1-fcaj"
export PREFIX="heart-risk"
export ENDPOINT_NAME="heart-risk-endpoint"
export PIPELINE_NAME="heart-risk-pipeline"
aws sts get-caller-identity
aws s3api head-bucket --bucket "$PROJECT_BUCKET"
```

**Expected:** identity succeeds and the bucket is reachable by the authorized principal. An access-denied response means the role/bucket policy or Region must be checked; never “fix” it with public access.

Evidence expected: `AWS-01`, `AWS-02`, `AWS-08`, `AWS-12`. These would prove Region, budget, and role setup, but image files are currently TODO.

**Cost/security:** enable alerts before jobs; keep Block Public Access enabled; use roles and least privilege.

Next: [Architecture](../5.3-Architecture/)."""
prereq_vi = prereq_en.replace("# Prerequisites", "# Điều kiện tiên quyết").replace(
"## Objective\n\nPrepare a controlled environment before creating billed resources.",
"## Mục tiêu\n\nChuẩn bị môi trường có kiểm soát trước khi tạo tài nguyên tính phí.").replace(
"1. Use an AWS account and select `us-east-1`.\n2. Install Git, Python 3, AWS CLI v2, and Hugo extended 0.134.3 or compatible.\n3. Configure SageMaker Studio/JupyterLab without embedding access keys.\n4. Create the private bucket and SageMaker/Lambda execution roles.\n5. Configure AWS Budget alerts.",
"1. Dùng AWS account và chọn `us-east-1`.\n2. Cài Git, Python 3, AWS CLI v2, Hugo extended 0.134.3 hoặc tương thích.\n3. Cấu hình SageMaker Studio/JupyterLab không nhúng access key.\n4. Tạo bucket private và execution role SageMaker/Lambda.\n5. Cấu hình AWS Budget alert.").replace(
"**Expected:** identity succeeds and the bucket is reachable by the authorized principal. An access-denied response means the role/bucket policy or Region must be checked; never “fix” it with public access.",
"**Kỳ vọng:** nhận diện identity thành công và principal được phép truy cập bucket. Nếu access denied, kiểm tra role/bucket policy hoặc Region; không bật public để “sửa”.").replace(
"Evidence expected:", "Minh chứng cần có:").replace("These would prove Region, budget, and role setup, but image files are currently TODO.",
"Các ảnh sẽ chứng minh Region, budget và role nhưng file hiện vẫn là TODO.").replace(
"**Cost/security:** enable alerts before jobs; keep Block Public Access enabled; use roles and least privilege.",
"**Chi phí/bảo mật:** bật alert trước khi chạy job; giữ Block Public Access; dùng role và đặc quyền tối thiểu.").replace(
"Next: [Architecture]", "Tiếp theo: [Kiến trúc]")
workshop_pair("5.2-Prerequisites", 2, "Prerequisites", "Điều kiện tiên quyết", prereq_en, prereq_vi)

arch_en = f"""# Architecture

## Objective and flow

![Heart-risk AWS architecture](../../images/architecture/heart-risk-architecture.svg)

**Offline:** raw S3 → Processing → split/artifacts → Training/HPO → Evaluation → Registry.  
**Online:** API Gateway → Lambda validation → endpoint → response; Data Capture writes JSONL to S3.  
**Monitoring:** capture/baseline → custom Processing → report → custom metrics → alarm.  
**Pipeline:** condition checks AUC/F1/recall; pass registers, fail emits `MetricThresholdFailed`.

| Implemented in PoC | Recommended for production |
|---|---|
| One endpoint instance | Auto Scaling and multi-AZ operational design |
| Public HTTP integration without production auth | Cognito/API keys/WAF and throttling |
| Service IAM roles, private S3 | VPC-only networking and KMS key strategy |
| Manual scripts and Pipeline | IaC, CI/CD, automated retraining with approval |

The SVG is an original documentation diagram, not evidence of resource state. Validate actual state through console/CLI and sanitized screenshots.

**Troubleshooting:** if arrows do not match artifact paths, inspect S3 URIs and Pipeline properties rather than copying objects manually. Services incur Region-specific charges.

{disclaimer_en}

Next: [Data preparation](../5.4-Data-Preparation/)."""
arch_vi = f"""# Kiến trúc

## Mục tiêu và luồng

![Kiến trúc AWS Heart-risk](../../../images/architecture/heart-risk-architecture.svg)

**Offline:** raw S3 → Processing → split/artifact → Training/HPO → Evaluation → Registry.  
**Online:** API Gateway → Lambda validate → endpoint → response; Data Capture ghi JSONL vào S3.  
**Monitoring:** capture/baseline → custom Processing → report → custom metric → alarm.  
**Pipeline:** condition kiểm tra AUC/F1/recall; pass đăng ký, fail tạo `MetricThresholdFailed`.

| Đã hiện thực trong PoC | Khuyến nghị production |
|---|---|
| Một endpoint instance | Auto Scaling và thiết kế vận hành multi-AZ |
| HTTP integration chưa có production auth | Cognito/API key/WAF và throttling |
| Service IAM role, S3 private | VPC-only và chiến lược KMS key |
| Script thủ công và Pipeline | IaC, CI/CD, automated retraining có phê duyệt |

SVG là sơ đồ tài liệu gốc, không phải minh chứng trạng thái tài nguyên. Cần kiểm tra trạng thái thật bằng console/CLI và ảnh đã che thông tin.

**Xử lý lỗi:** nếu artifact path không khớp, kiểm tra S3 URI và Pipeline property thay vì copy thủ công. Dịch vụ phát sinh phí theo Region.

{disclaimer_vi}

Tiếp theo: [Chuẩn bị dữ liệu](../5.4-Data-Preparation/)."""
workshop_pair("5.3-Architecture", 3, "Architecture", "Kiến trúc", arch_en, arch_vi)


pair(CONTENT / "5-Workshop" / "5.4-Data-Preparation", "Data preparation", "Chuẩn bị dữ liệu", 4, "5.4.",
"""# Data preparation

The two labs establish immutable raw input and leakage-safe managed outputs.

1. [Version and upload raw data](5.4.1-S3-Upload/)
2. [Run SageMaker Processing](5.4.2-SageMaker-Processing/)""",
"""# Chuẩn bị dữ liệu

Hai bài thực hành tạo raw input bất biến và managed output chống leakage.

1. [Version và upload raw data](5.4.1-S3-Upload/)
2. [Chạy SageMaker Processing](5.4.2-SageMaker-Processing/)""")

s3_en = """# S3 upload and dataset versioning

## Objective and background

Upload the canonical 7,000-row CSV to `s3://$PROJECT_BUCKET/heart-risk/raw/heart_attack_dataset.csv`, calculate SHA-256, and store a manifest so repeated runs can detect the same content.

```bash
sha256sum heart_attack_dataset.csv
aws s3 cp heart_attack_dataset.csv \
  "s3://$PROJECT_BUCKET/$PREFIX/raw/heart_attack_dataset.csv" \
  --region "$AWS_REGION"
```

An idempotent uploader should compare the local digest with manifest/object metadata: skip identical content and require an explicit version/change path when different.

**Expected:** a private object and manifest under `heart-risk`; no public ACL. The source uploader is not present locally, so no fabricated attachment is linked.

**Errors:** `AccessDenied` means scoped IAM/bucket policy needs correction; a digest mismatch means do not silently overwrite. S3 storage/requests cost money, though usually less than always-on compute.

Next: [SageMaker Processing](../5.4.2-SageMaker-Processing/)."""
s3_vi = s3_en.replace("# S3 upload and dataset versioning", "# Upload S3 và version dữ liệu").replace(
"## Objective and background\n\nUpload the canonical 7,000-row CSV to", "## Mục tiêu và khái niệm\n\nUpload CSV 7.000 dòng chuẩn lên").replace(
"An idempotent uploader should compare the local digest with manifest/object metadata: skip identical content and require an explicit version/change path when different.",
"Uploader idempotent cần so digest local với manifest/object metadata: bỏ qua nội dung giống nhau và yêu cầu version/change path rõ ràng nếu khác.").replace(
"**Expected:** a private object and manifest under `heart-risk`; no public ACL. The source uploader is not present locally, so no fabricated attachment is linked.",
"**Kỳ vọng:** object private và manifest dưới `heart-risk`; không có public ACL. Source uploader không có trong workspace nên không tạo link attachment giả.").replace(
"**Errors:** `AccessDenied` means scoped IAM/bucket policy needs correction; a digest mismatch means do not silently overwrite. S3 storage/requests cost money, though usually less than always-on compute.",
"**Lỗi:** `AccessDenied` yêu cầu sửa IAM/bucket policy đúng phạm vi; digest mismatch không được overwrite âm thầm. S3 storage/request có phí nhưng thường thấp hơn compute chạy liên tục.").replace(
"Next: [SageMaker Processing]", "Tiếp theo: [SageMaker Processing]")
pair(CONTENT / "5-Workshop" / "5.4-Data-Preparation" / "5.4.1-S3-Upload", "S3 upload", "Upload S3", 1, "5.4.1.", s3_en, s3_vi)

proc_en = """# SageMaker Processing

## Objective

Create reproducible train/validation/test data without leakage.

```python
# Pseudocode: split before fitting transformations
train, temp = stratified_split(raw, train_size=0.70, target="heart_attack_risk")
validation, test = stratified_split(temp, train_size=0.50, target="heart_attack_risk")
preprocessor.fit(train[feature_columns])  # fit_scope = "train_only"
```

Numeric missing values use median imputation and scaling; categorical values use most-frequent imputation and one-hot encoding. `patient_id` is excluded.

| Check | Expected |
|---|---:|
| Split rows | 4,900 / 1,050 / 1,050 |
| Raw/processed features | 20 / 36 |
| Missing after processing | 0 |
| Fit scope | `train_only` |

Evidence `W2-01`, `W2-02`, and `W2-03` respectively proves managed completion, logged quality checks, and persisted S3 outputs. The supplied screenshots are displayed and interpreted below.

**Troubleshooting:** feature-count mismatch usually means category vocabulary or excluded columns changed. Never refit on validation/test. Stop failed jobs and inspect CloudWatch logs to control cost.

Next: [Model training](../../5.5-Model-Training/)."""
proc_vi = proc_en.replace("# SageMaker Processing", "# SageMaker Processing").replace(
"## Objective\n\nCreate reproducible train/validation/test data without leakage.",
"## Mục tiêu\n\nTạo train/validation/test có thể tái lập mà không leakage.").replace(
"Numeric missing values use median imputation and scaling; categorical values use most-frequent imputation and one-hot encoding. `patient_id` is excluded.",
"Numeric missing dùng median imputation và scaling; categorical dùng most-frequent imputation và one-hot encoding. Loại `patient_id`.").replace(
"| Check | Expected |", "| Kiểm tra | Kỳ vọng |").replace(
"| Split rows |", "| Số dòng split |").replace("| Raw/processed features |", "| Feature raw/processed |").replace(
"| Missing after processing |", "| Missing sau xử lý |").replace("| Fit scope |", "| Phạm vi fit |").replace(
"Evidence `W2-01`, `W2-02`, and `W2-03` respectively proves managed completion, logged quality checks, and persisted S3 outputs. The supplied screenshots are displayed and interpreted below.",
"Minh chứng `W2-01`, `W2-02` và `W2-03` lần lượt xác nhận managed job hoàn tất, quality check trong log và output S3. Các ảnh được cung cấp được hiển thị và diễn giải bên dưới.").replace(
"**Troubleshooting:** feature-count mismatch usually means category vocabulary or excluded columns changed. Never refit on validation/test. Stop failed jobs and inspect CloudWatch logs to control cost.",
"**Xử lý lỗi:** feature count lệch thường do category vocabulary hoặc cột loại trừ thay đổi. Không refit trên validation/test. Dừng job lỗi và đọc CloudWatch log để kiểm soát phí.").replace(
"Next: [Model training]", "Tiếp theo: [Huấn luyện mô hình]")
pair(CONTENT / "5-Workshop" / "5.4-Data-Preparation" / "5.4.2-SageMaker-Processing", "SageMaker Processing", "SageMaker Processing", 2, "5.4.2.", proc_en, proc_vi)


pair(CONTENT / "5-Workshop" / "5.5-Model-Training", "Model training", "Huấn luyện mô hình", 5, "5.5.",
"""# Model training

Train two algorithm families, tune XGBoost with a small controlled search, and select using validation—not test—results.

1. [Logistic Regression](5.5.1-Logistic-Regression/)
2. [XGBoost](5.5.2-XGBoost/)
3. [HPO](5.5.3-HPO/)""",
"""# Huấn luyện mô hình

Huấn luyện hai nhóm thuật toán, tune XGBoost bằng search nhỏ có kiểm soát và chọn theo validation, không theo test.

1. [Logistic Regression](5.5.1-Logistic-Regression/)
2. [XGBoost](5.5.2-XGBoost/)
3. [HPO](5.5.3-HPO/)""")

lr_en = """# Logistic Regression

## Objective and rationale

Train an interpretable linear baseline as a managed job, independent of the notebook session.

```text
validation ROC-AUC = 0.863949
F1 = 0.747583; recall = 0.789116; precision = 0.710204
decision threshold = 0.36
```

`W3-01` should prove job status/configuration and `W3-02` the validation metrics; actual images remain to be supplied. Threshold 0.36 is part of this evaluated artifact, not a medical cutoff.

**Expected:** model artifact in S3 and metrics recorded for comparison. If metric parsing is empty, verify log regex/channel names. Training jobs incur instance-time cost and the role should only reach required S3 prefixes.

Next: [XGBoost](../5.5.2-XGBoost/)."""
lr_vi = lr_en.replace("# Logistic Regression", "# Logistic Regression").replace(
"## Objective and rationale\n\nTrain an interpretable linear baseline as a managed job, independent of the notebook session.",
"## Mục tiêu và lý do\n\nTrain baseline tuyến tính dễ diễn giải bằng managed job, độc lập phiên notebook.").replace(
"should prove job status/configuration and", "cần chứng minh trạng thái/cấu hình job và").replace(
"the validation metrics; actual images remain to be supplied. Threshold 0.36 is part of this evaluated artifact, not a medical cutoff.",
"các validation metric; cần bổ sung file ảnh thật. Threshold 0,36 thuộc artifact được đánh giá, không phải ngưỡng y khoa.").replace(
"**Expected:** model artifact in S3 and metrics recorded for comparison. If metric parsing is empty, verify log regex/channel names. Training jobs incur instance-time cost and the role should only reach required S3 prefixes.",
"**Kỳ vọng:** model artifact trên S3 và metric được ghi để so sánh. Nếu không parse được metric, kiểm tra log regex/channel. Training job tính phí theo instance-time và role chỉ được truy cập prefix cần thiết.").replace(
"Next: [XGBoost]", "Tiếp theo: [XGBoost]")
pair(CONTENT / "5-Workshop" / "5.5-Model-Training" / "5.5.1-Logistic-Regression", "Logistic Regression", "Logistic Regression", 1, "5.5.1.", lr_en, lr_vi)

xgb_en = """# XGBoost

## Objective and comparison

Test a tree-based model that can learn nonlinear interactions.

| Model | AUC | F1 | Recall | Precision |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.863949 | 0.747583 | 0.789116 | 0.710204 |
| XGBoost default | 0.854283 | 0.749749 | 0.845805 | 0.673285 |

XGBoost improved recall but reduced precision and the primary selection metric, AUC. `W3-03` should prove the managed job and `W3-04` its metrics; images are not currently available.

**Expected:** an independently versioned artifact, not an overwrite of LR. If XGBoost input format fails, verify label position/content type. Limit job size and delete transient artifacts only after evidence is retained.

Next: [HPO](../5.5.3-HPO/)."""
xgb_vi = xgb_en.replace("## Objective and comparison", "## Mục tiêu và so sánh").replace(
"Test a tree-based model that can learn nonlinear interactions.", "Thử model dạng cây có thể học tương tác phi tuyến.").replace(
"XGBoost improved recall but reduced precision and the primary selection metric, AUC.", "XGBoost tăng recall nhưng giảm precision và primary selection metric AUC.").replace(
"should prove the managed job and", "cần chứng minh managed job và").replace(
"its metrics; images are not currently available.", "metric; hiện chưa có file ảnh.").replace(
"**Expected:** an independently versioned artifact, not an overwrite of LR. If XGBoost input format fails, verify label position/content type. Limit job size and delete transient artifacts only after evidence is retained.",
"**Kỳ vọng:** artifact có version độc lập, không overwrite LR. Nếu input XGBoost lỗi, kiểm tra vị trí label/content type. Giới hạn job và chỉ xóa artifact tạm sau khi giữ minh chứng.").replace(
"Next: [HPO]", "Tiếp theo: [HPO]")
pair(CONTENT / "5-Workshop" / "5.5-Model-Training" / "5.5.2-XGBoost", "XGBoost", "XGBoost", 2, "5.5.2.", xgb_en, xgb_vi)

hpo_en = """# Hyperparameter optimization

## Objective and configuration

Use a deliberately small managed Bayesian search to improve XGBoost without uncontrolled cost.

```python
objective_metric_name = "validation:auc"
strategy = "Bayesian"
max_jobs, max_parallel_jobs = 3, 1
tuned = ["eta", "max-depth", "min-child-weight"]
```

| Candidate | Validation AUC | F1 | Recall |
|---|---:|---:|---:|
| LR | **0.863949** | 0.747583 | 0.789116 |
| XGBoost default | 0.854283 | 0.749749 | 0.845805 |
| XGBoost HPO | 0.860982 | 0.749522 | **0.888889** |

LR remains selected by validation AUC. Test data was not used for model/trial selection. There is no HPO screenshot, so this page intentionally has no broken evidence image.

**Troubleshooting:** no best job usually means the objective metric regex/name was not emitted. Three sequential jobs constrain cost but also limit search quality.

Next: [Evaluation and Registry](../../5.6-Evaluation-Registry/)."""
hpo_vi = hpo_en.replace("# Hyperparameter optimization", "# Tối ưu siêu tham số").replace(
"## Objective and configuration", "## Mục tiêu và cấu hình").replace(
"Use a deliberately small managed Bayesian search to improve XGBoost without uncontrolled cost.",
"Dùng managed Bayesian search nhỏ có chủ đích để cải thiện XGBoost mà không mất kiểm soát chi phí.").replace(
"LR remains selected by validation AUC. Test data was not used for model/trial selection. There is no HPO screenshot, so this page intentionally has no broken evidence image.",
"LR vẫn được chọn theo validation AUC. Không dùng test để chọn model/trial. Không có ảnh HPO nên trang chủ động không chèn link ảnh hỏng.").replace(
"**Troubleshooting:** no best job usually means the objective metric regex/name was not emitted. Three sequential jobs constrain cost but also limit search quality.",
"**Xử lý lỗi:** không có best job thường do objective metric regex/name không được emit. Ba job tuần tự giới hạn phí nhưng cũng giới hạn chất lượng search.").replace(
"Next: [Evaluation and Registry]", "Tiếp theo: [Đánh giá và Registry]")
pair(CONTENT / "5-Workshop" / "5.5-Model-Training" / "5.5.3-HPO", "Hyperparameter optimization", "Tối ưu siêu tham số", 3, "5.5.3.", hpo_en, hpo_vi)


pair(CONTENT / "5-Workshop" / "5.6-Evaluation-Registry", "Evaluation and Registry", "Đánh giá và Registry", 6, "5.6.",
"""# Evaluation and Model Registry

Evaluate the selected candidate exactly once on test data, then register it with manual approval.

1. [Final evaluation](5.6.1-Evaluation/)
2. [Model Registry](5.6.2-Model-Registry/)""",
"""# Đánh giá và Model Registry

Đánh giá ứng viên đã chọn đúng một lần trên test, sau đó đăng ký với phê duyệt thủ công.

1. [Đánh giá cuối](5.6.1-Evaluation/)
2. [Model Registry](5.6.2-Model-Registry/)""")

eval_en = f"""# Final evaluation

| Metric | Value |
|---|---:|
| ROC-AUC | 0.885515 |
| Accuracy | 0.793333 |
| Precision | 0.724900 |
| Recall | 0.818594 |
| F1 | 0.768903 |
| False Negative Rate | 0.181406 |

| | Predicted negative | Predicted positive |
|---|---:|---:|
| Actual negative | TN 472 | FP 137 |
| Actual positive | FN 80 | TP 361 |

The model passes AUC ≥ 0.84, F1 ≥ 0.70, and recall ≥ 0.65. The 80 false negatives are positive labels missed by this evaluated model; this is a material limitation, not evidence of clinical safety. `W5-02` should substantiate the metrics/confusion matrix when supplied.

**Troubleshooting:** do not tune after viewing test results. A mismatch often means a different threshold or preprocessing artifact. Evaluation jobs have storage/compute cost; protect test data and reports.

{disclaimer_en}

Next: [Model Registry](../5.6.2-Model-Registry/)."""
eval_vi = f"""# Đánh giá cuối

| Metric | Giá trị |
|---|---:|
| ROC-AUC | 0,885515 |
| Accuracy | 0,793333 |
| Precision | 0,724900 |
| Recall | 0,818594 |
| F1 | 0,768903 |
| False Negative Rate | 0,181406 |

| | Dự đoán negative | Dự đoán positive |
|---|---:|---:|
| Thực tế negative | TN 472 | FP 137 |
| Thực tế positive | FN 80 | TP 361 |

Model vượt AUC ≥ 0,84, F1 ≥ 0,70, recall ≥ 0,65. 80 âm tính giả là positive label bị model bỏ sót; đây là giới hạn quan trọng, không phải bằng chứng an toàn lâm sàng. `W5-02` cần xác nhận metric/confusion matrix khi được cung cấp.

**Xử lý lỗi:** không tune sau khi xem test. Sai khác thường do threshold hoặc preprocessing artifact khác. Evaluation job có phí compute/storage; bảo vệ test data và report.

{disclaimer_vi}

Tiếp theo: [Model Registry](../5.6.2-Model-Registry/)."""
pair(CONTENT / "5-Workshop" / "5.6-Evaluation-Registry" / "5.6.1-Evaluation", "Final evaluation", "Đánh giá cuối", 1, "5.6.1.", eval_en, eval_vi)

reg_en = """# Model Registry

## Objective and states

Use `heart-attack-risk-models` for lineage and a human promotion decision.

| Version | State | Meaning |
|---:|---|---|
| 1 | Approved | retained approved version |
| 2 | Approved | deployment source for `heart-risk-endpoint` |
| 3 | PendingManualApproval | created by successful Pipeline |

```bash
aws sagemaker list-model-packages \
  --model-package-group-name heart-attack-risk-models \
  --region "$AWS_REGION"
```

`W5-01` should prove the states when supplied. Manual approval prevents an evaluated artifact from being deployed merely because training completed.

**Errors:** a package that rejects `ml.t3.medium` requires a supported deployment configuration; this project uses `ml.m5.large`. Avoid publishing full account-bearing ARNs.

Next: [Deployment and API](../../5.7-Deployment-API/)."""
reg_vi = reg_en.replace("## Objective and states", "## Mục tiêu và trạng thái").replace(
"Use `heart-attack-risk-models` for lineage and a human promotion decision.",
"Dùng `heart-attack-risk-models` để truy vết và có quyết định promotion của con người.").replace(
"| Version | State | Meaning |", "| Version | State | Ý nghĩa |").replace(
"retained approved version", "version được duyệt và giữ lại").replace(
"deployment source for", "nguồn triển khai cho").replace("created by successful Pipeline", "được Pipeline thành công tạo").replace(
"should prove the states when supplied. Manual approval prevents an evaluated artifact from being deployed merely because training completed.",
"cần chứng minh trạng thái khi được cung cấp. Phê duyệt thủ công ngăn artifact được deploy chỉ vì training hoàn tất.").replace(
"**Errors:** a package that rejects `ml.t3.medium` requires a supported deployment configuration; this project uses `ml.m5.large`. Avoid publishing full account-bearing ARNs.",
"**Lỗi:** package từ chối `ml.t3.medium` cần deployment config được hỗ trợ; dự án dùng `ml.m5.large`. Tránh public ARN chứa account đầy đủ.").replace(
"Next: [Deployment and API]", "Tiếp theo: [Triển khai và API]")
pair(CONTENT / "5-Workshop" / "5.6-Evaluation-Registry" / "5.6.2-Model-Registry", "Model Registry", "Model Registry", 2, "5.6.2.", reg_en, reg_vi)


pair(CONTENT / "5-Workshop" / "5.7-Deployment-API", "Deployment and API", "Triển khai và API", 7, "5.7.",
"""# Deployment and API

1. [SageMaker endpoint](5.7.1-SageMaker-Endpoint/)
2. [Lambda wrapper](5.7.2-Lambda/)
3. [API Gateway](5.7.3-API-Gateway/)
4. [Data Capture](5.7.4-Data-Capture/)""",
"""# Triển khai và API

1. [SageMaker endpoint](5.7.1-SageMaker-Endpoint/)
2. [Lambda wrapper](5.7.2-Lambda/)
3. [API Gateway](5.7.3-API-Gateway/)
4. [Data Capture](5.7.4-Data-Capture/)""")

endpoint_en = f"""# SageMaker real-time endpoint

Deploy Approved Model Package version 2 as `heart-risk-endpoint` on one `ml.m5.large` instance and wait for `InService`.

```bash
aws sagemaker describe-endpoint \
  --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION" \
  --query 'EndpointStatus'
```

Expected response fields are `prediction`, `risk_probability`, `threshold`, `model_type` or `model_version`, and `disclaimer`. `W6-01a/b` should prove live state/config; `W6-03` direct inference. `ml.t3.medium` previously failed package validation, resolved with supported `ml.m5.large`.

{disclaimer_en}

**Cost/security:** endpoint uptime is continuously billed; invoke through scoped IAM and do not expose it publicly. If status is `Failed`, inspect `FailureReason` and CloudWatch logs.

Next: [Lambda](../5.7.2-Lambda/)."""
endpoint_vi = endpoint_en.replace("# SageMaker real-time endpoint", "# SageMaker real-time endpoint").replace(
"Deploy Approved Model Package version 2 as", "Triển khai Approved Model Package version 2 thành").replace(
"on one `ml.m5.large` instance and wait for `InService`.", "trên một instance `ml.m5.large` và chờ `InService`.").replace(
"Expected response fields are", "Các field response kỳ vọng gồm").replace(
"should prove live state/config;", "cần chứng minh trạng thái/cấu hình;").replace(
"direct inference. `ml.t3.medium` previously failed package validation, resolved with supported `ml.m5.large`.",
"chứng minh inference trực tiếp. `ml.t3.medium` từng fail package validation và được xử lý bằng `ml.m5.large` được hỗ trợ.").replace(
"**Cost/security:** endpoint uptime is continuously billed; invoke through scoped IAM and do not expose it publicly. If status is `Failed`, inspect `FailureReason` and CloudWatch logs.",
"**Chi phí/bảo mật:** endpoint bị tính phí liên tục; gọi qua IAM có phạm vi và không public trực tiếp. Nếu `Failed`, đọc `FailureReason` và CloudWatch log.").replace(
"Next: [Lambda]", "Tiếp theo: [Lambda]")
pair(CONTENT / "5-Workshop" / "5.7-Deployment-API" / "5.7.1-SageMaker-Endpoint", "SageMaker endpoint", "SageMaker endpoint", 1, "5.7.1.", endpoint_en, endpoint_vi)

lambda_en = """# Lambda wrapper

`heart-risk-api` validates required fields, serializes the endpoint request, invokes only `heart-risk-endpoint`, and maps downstream errors to safe responses.

```python
endpoint = os.environ["ENDPOINT_NAME"]
response = runtime.invoke_endpoint(
    EndpointName=endpoint, ContentType="application/json", Body=json.dumps(payload)
)
```

Environment variables hold endpoint/model configuration, never credentials. `AWS-14` and `W6-06a/b` should prove least-privilege `sagemaker:InvokeEndpoint`; `W6-04/05` configuration. Files are pending.

**Expected:** valid events return structured results; missing fields return 400; unavailable prediction service returns 502 without an internal stack trace. Inspect Lambda/endpoint logs on timeout. Lambda and log retention incur usage/storage costs.

Next: [API Gateway](../5.7.3-API-Gateway/)."""
lambda_vi = lambda_en.replace("# Lambda wrapper", "# Lambda wrapper").replace(
"validates required fields, serializes the endpoint request, invokes only", "validate field bắt buộc, serialize request, chỉ gọi").replace(
"and maps downstream errors to safe responses.", "và ánh xạ lỗi downstream thành response an toàn.").replace(
"Environment variables hold endpoint/model configuration, never credentials.", "Biến môi trường giữ cấu hình endpoint/model, không giữ credential.").replace(
"should prove least-privilege", "cần chứng minh quyền đặc quyền tối thiểu").replace(
"configuration. Files are pending.", "chứng minh cấu hình. Các file ảnh đang chờ bổ sung.").replace(
"**Expected:** valid events return structured results; missing fields return 400; unavailable prediction service returns 502 without an internal stack trace. Inspect Lambda/endpoint logs on timeout. Lambda and log retention incur usage/storage costs.",
"**Kỳ vọng:** event hợp lệ trả result có cấu trúc; thiếu field trả 400; prediction service không sẵn sàng trả 502 không lộ stack trace. Khi timeout, đọc log Lambda/endpoint. Lambda và log retention phát sinh phí.").replace(
"Next: [API Gateway]", "Tiếp theo: [API Gateway]")
pair(CONTENT / "5-Workshop" / "5.7-Deployment-API" / "5.7.2-Lambda", "Lambda wrapper", "Lambda wrapper", 2, "5.7.2.", lambda_en, lambda_vi)

api_en = f"""# API Gateway

Create HTTP API `heart-risk-http-api` with:

```text
GET /health
POST /predict
```

Use a masked stage URL:

```bash
curl -i "$API_BASE_URL/health"
curl -i -X POST "$API_BASE_URL/predict" \
  -H 'content-type: application/json' --data @sample-request.json
```

| Test | Expected | Operational meaning |
|---|---:|---|
| Health | 200 | wrapper reachable |
| Valid prediction | 200 | API-to-endpoint integration works |
| Missing fields | 400 | client validation works |
| Service unavailable | 502 | downstream failure is controlled |

`W6-07` through `W6-11` should prove routes and each case when files are supplied. Never publish an active full URL; add throttling/authentication for production.

{disclaimer_en}

Next: [Data Capture](../5.7.4-Data-Capture/)."""
api_vi = api_en.replace("# API Gateway", "# API Gateway").replace(
"Create HTTP API", "Tạo HTTP API").replace("with:", "với:").replace(
"Use a masked stage URL:", "Dùng stage URL đã che:").replace(
"| Test | Expected | Operational meaning |", "| Test | Kỳ vọng | Ý nghĩa vận hành |").replace(
"| Health | 200 | wrapper reachable |", "| Health | 200 | wrapper truy cập được |").replace(
"| Valid prediction | 200 | API-to-endpoint integration works |", "| Prediction hợp lệ | 200 | tích hợp API-endpoint hoạt động |").replace(
"| Missing fields | 400 | client validation works |", "| Thiếu field | 400 | validate phía client hoạt động |").replace(
"| Service unavailable | 502 | downstream failure is controlled |", "| Service không sẵn sàng | 502 | lỗi downstream được kiểm soát |").replace(
"should prove routes and each case when files are supplied. Never publish an active full URL; add throttling/authentication for production.",
"cần chứng minh route và từng case khi có file. Không public URL active đầy đủ; thêm throttling/authentication cho production.").replace(
"Next: [Data Capture]", "Tiếp theo: [Data Capture]")
pair(CONTENT / "5-Workshop" / "5.7-Deployment-API" / "5.7.3-API-Gateway", "API Gateway", "API Gateway", 3, "5.7.3.", api_en, api_vi)

capture_en = """# Data Capture

Enable 100% input and output capture in JSONL to the private project S3 prefix.

```text
EnableCapture=true
InitialSamplingPercentage=100
CaptureOptions=[Input, Output]
```

An actual record contains `endpointInput`, `endpointOutput`, `eventMetadata`, and `inferenceTime`. `W6-02` should prove configuration, `W6-12` generated files, and `W6-13` record content. Supplying only configuration would not prove traffic was captured.

**Expected:** new invocations create timestamped JSONL objects. If none appear, verify capture destination, endpoint config, permissions, traffic, and delivery delay. Captured payloads can contain sensitive information: use synthetic/non-private data, private S3, retention, and restricted readers.

Next: [Monitoring](../../5.8-Monitoring/)."""
capture_vi = capture_en.replace("Enable 100% input and output capture in JSONL to the private project S3 prefix.",
"Bật capture 100% input/output dạng JSONL vào prefix S3 private của dự án.").replace(
"An actual record contains", "Record thật chứa").replace(
"should prove configuration,", "cần chứng minh cấu hình,").replace(
"generated files, and", "chứng minh file được tạo, và").replace(
"record content. Supplying only configuration would not prove traffic was captured.",
"chứng minh nội dung record. Chỉ có cấu hình chưa chứng minh traffic đã được capture.").replace(
"**Expected:** new invocations create timestamped JSONL objects. If none appear, verify capture destination, endpoint config, permissions, traffic, and delivery delay. Captured payloads can contain sensitive information: use synthetic/non-private data, private S3, retention, and restricted readers.",
"**Kỳ vọng:** invocation mới tạo object JSONL theo timestamp. Nếu không có, kiểm tra destination, endpoint config, permission, traffic và độ trễ. Payload capture có thể nhạy cảm: dùng dữ liệu synthetic/không riêng tư, S3 private, retention và giới hạn reader.").replace(
"Next: [Monitoring]", "Tiếp theo: [Monitoring]")
pair(CONTENT / "5-Workshop" / "5.7-Deployment-API" / "5.7.4-Data-Capture", "Data Capture", "Data Capture", 4, "5.7.4.", capture_en, capture_vi)


pair(CONTENT / "5-Workshop" / "5.8-Monitoring", "Monitoring", "Monitoring", 8, "5.8.",
"""# Drift monitoring

The official baseline and hourly schedule were created, but the expected feature-level CloudWatch metric did not appear. The documented alert therefore uses the custom fallback, not an unsupported official-metric claim.

1. [Custom drift Processing](5.8.1-Drift-Processing/)
2. [CloudWatch metrics and alarm](5.8.2-CloudWatch-Alarm/)""",
"""# Giám sát drift

Official baseline và lịch mỗi giờ đã được tạo nhưng feature-level CloudWatch metric mong đợi không xuất hiện. Cảnh báo được ghi nhận vì vậy dùng custom fallback, không tuyên bố thiếu căn cứ về official metric.

1. [Custom drift Processing](5.8.1-Drift-Processing/)
2. [CloudWatch metric và alarm](5.8.2-CloudWatch-Alarm/)""")

drift_en = f"""# Custom drift Processing

## Flow and PoC rules

Data Capture/S3 current data → custom SageMaker Processing → report → CloudWatch.

| Check | Value |
|---|---:|
| Baseline/current rows | 4,900 / 7,000 |
| Features/violations | 20 / 6 |
| Drifted | age, resting_bp, cholesterol, bmi, smoking_status, stress_level |

Numeric drift is standardized mean shift > 0.5; categorical drift is total variation distance > 0.20.

{notice("These thresholds are transparent proof-of-concept rules, not clinical or universal production standards.")}

`W7-01a/b` should prove managed execution/history; `W7-02` counts; `W7-03a/b` feature results. If the capture schema cannot be flattened, inspect JSONL input/output encoding before calculating drift. Processing compute is billed per run.

Next: [CloudWatch alarm](../5.8.2-CloudWatch-Alarm/)."""
drift_vi = f"""# Custom drift Processing

## Luồng và quy tắc PoC

Data Capture/S3 current data → custom SageMaker Processing → report → CloudWatch.

| Kiểm tra | Giá trị |
|---|---:|
| Baseline/current | 4.900 / 7.000 dòng |
| Feature/violation | 20 / 6 |
| Drift | age, resting_bp, cholesterol, bmi, smoking_status, stress_level |

Numeric drift khi standardized mean shift > 0,5; categorical drift khi total variation distance > 0,20.

{notice("Đây là quy tắc proof of concept minh bạch, không phải ngưỡng lâm sàng hay chuẩn production phổ quát.")}

`W7-01a/b` cần chứng minh managed execution/history; `W7-02` chứng minh số lượng; `W7-03a/b` chứng minh feature. Nếu không flatten được schema capture, kiểm tra encoding JSONL input/output trước khi tính drift. Processing compute tính phí theo lần chạy.

Tiếp theo: [CloudWatch alarm](../5.8.2-CloudWatch-Alarm/)."""
pair(CONTENT / "5-Workshop" / "5.8-Monitoring" / "5.8.1-Drift-Processing", "Custom drift Processing", "Custom drift Processing", 1, "5.8.1.", drift_en, drift_vi)

alarm_en = """# CloudWatch metrics and alarm

Publish batch results to namespace `Custom/HeartRisk`:

```text
DriftDetected = 1
DataQualityViolationCount = 6
```

Configure `heart-risk-custom-drift` to enter `ALARM` when `DriftDetected` breaches its threshold, with `TreatMissingData=ignore`.

```bash
aws cloudwatch describe-alarms \
  --alarm-names heart-risk-custom-drift --region "$AWS_REGION"
```

`W7-04` should prove both custom metrics; `W7-05` the `ALARM` state. Sparse batch metrics originally left/reset the state when empty periods were treated as non-breaching; ignoring missing periods and publishing a fresh datapoint resolved it.

**Errors/security/cost:** use `describe-alarms` if `DescribeAlarmHistory` is denied; grant history access only if needed. Keep dimensions stable and avoid sensitive data in dimensions. Metrics/alarms incur charges.

Next: [Pipeline](../../5.9-Pipeline/)."""
alarm_vi = alarm_en.replace("Publish batch results to namespace", "Publish kết quả batch vào namespace").replace(
"Configure", "Cấu hình").replace("to enter", "chuyển sang").replace("when", "khi").replace(
"breaches its threshold, with", "vượt ngưỡng, với").replace(
"should prove both custom metrics;", "cần chứng minh hai custom metric;").replace(
"the `ALARM` state. Sparse batch metrics originally left/reset the state when empty periods were treated as non-breaching; ignoring missing periods and publishing a fresh datapoint resolved it.",
"chứng minh trạng thái `ALARM`. Metric batch thưa từng làm trạng thái không đúng khi period trống bị coi là non-breaching; ignore missing period và publish datapoint mới đã xử lý vấn đề.").replace(
"**Errors/security/cost:** use", "**Lỗi/bảo mật/chi phí:** dùng").replace(
"if `DescribeAlarmHistory` is denied; grant history access only if needed. Keep dimensions stable and avoid sensitive data in dimensions. Metrics/alarms incur charges.",
"nếu bị từ chối `DescribeAlarmHistory`; chỉ cấp quyền history khi cần. Giữ dimension ổn định và không đưa dữ liệu nhạy cảm vào dimension. Metric/alarm có phí.").replace(
"Next: [Pipeline]", "Tiếp theo: [Pipeline]")
pair(CONTENT / "5-Workshop" / "5.8-Monitoring" / "5.8.2-CloudWatch-Alarm", "CloudWatch alarm", "CloudWatch alarm", 2, "5.8.2.", alarm_en, alarm_vi)


pair(CONTENT / "5-Workshop" / "5.9-Pipeline", "SageMaker Pipeline", "SageMaker Pipeline", 9, "5.9.",
"""# Quality-gated Pipeline

`PreprocessData → TrainModel → EvaluateModel → CheckModelQuality`; pass registers, fail runs `MetricThresholdFailed`.

1. [Successful execution](5.9.1-Success-Execution/)
2. [Intentional failure](5.9.2-Intentional-Failure/)""",
"""# Pipeline có quality gate

`PreprocessData → TrainModel → EvaluateModel → CheckModelQuality`; pass đăng ký, fail chạy `MetricThresholdFailed`.

1. [Execution thành công](5.9.1-Success-Execution/)
2. [Thất bại có chủ đích](5.9.2-Intentional-Failure/)""")

success_en = """# Successful Pipeline execution

The execution finished `Succeeded`: PreprocessData, TrainModel, EvaluateModel, CheckModelQuality, and RegisterModel all succeeded. The result was Model Package version 3 with `PendingManualApproval`.

```bash
aws sagemaker list-pipeline-executions \
  --pipeline-name "$PIPELINE_NAME" --region "$AWS_REGION"
```

`W8-01` should explain graph shape; `W8-02` overall success; `W8-03` each step; `W8-04` condition pass. The pipeline initially did not appear because it had not been upserted; run the pipeline definition/upsert before listing/executing.

**Expected:** registration occurs only after all three gates pass. Use a scoped Pipeline execution role and remember each step can incur job cost.

Next: [Intentional failure](../5.9.2-Intentional-Failure/)."""
success_vi = success_en.replace("The execution finished", "Execution kết thúc").replace(
"all succeeded. The result was", "đều thành công. Kết quả là").replace(
"with", "với").replace("should explain graph shape;", "cần giải thích graph;").replace(
"overall success;", "chứng minh trạng thái tổng;").replace("each step;", "từng step;").replace(
"condition pass. The pipeline initially did not appear because it had not been upserted; run the pipeline definition/upsert before listing/executing.",
"condition pass. Pipeline ban đầu chưa xuất hiện vì chưa upsert; chạy định nghĩa/upsert trước khi list/execute.").replace(
"**Expected:** registration occurs only after all three gates pass. Use a scoped Pipeline execution role and remember each step can incur job cost.",
"**Kỳ vọng:** chỉ đăng ký sau khi ba gate pass. Dùng Pipeline execution role có phạm vi; mỗi step có thể phát sinh phí job.").replace(
"Next: [Intentional failure]", "Tiếp theo: [Thất bại có chủ đích]")
pair(CONTENT / "5-Workshop" / "5.9-Pipeline" / "5.9.1-Success-Execution", "Successful execution", "Execution thành công", 1, "5.9.1.", success_en, success_vi)

fail_en = """# Intentional Pipeline failure

Override `AucThreshold=0.99`, above the evaluated 0.885515 result. The final execution is `Failed` **by design**, `MetricThresholdFailed` executes, and RegisterModel does not.

```bash
aws sagemaker start-pipeline-execution \
  --pipeline-name "$PIPELINE_NAME" \
  --pipeline-parameters Name=AucThreshold,Value=0.99 \
  --region "$AWS_REGION"
```

`W8-05` should prove failed execution, `W8-06` the 0.99 parameter, and `W8-07` the fail step. Together they prove a low-quality candidate cannot silently enter the registry.

**Troubleshooting:** do not “fix” this expected test by lowering the gate mid-execution. Distinguish condition failure from infrastructure failure in step metadata/logs.

Next: [Security and cost](../../5.10-Security-Cost/)."""
fail_vi = fail_en.replace("# Intentional Pipeline failure", "# Pipeline thất bại có chủ đích").replace(
"Override", "Ghi đè").replace("above the evaluated", "cao hơn kết quả").replace(
"The final execution is", "Execution cuối là").replace("**by design**", "**theo thiết kế**").replace(
"executes, and", "được chạy và").replace("does not.", "không chạy.").replace(
"should prove failed execution,", "cần chứng minh execution failed,").replace(
"the 0.99 parameter, and", "tham số 0,99 và").replace(
"the fail step. Together they prove a low-quality candidate cannot silently enter the registry.",
"fail step. Các minh chứng cho thấy ứng viên không đạt không thể âm thầm vào registry.").replace(
"**Troubleshooting:** do not “fix” this expected test by lowering the gate mid-execution. Distinguish condition failure from infrastructure failure in step metadata/logs.",
"**Xử lý lỗi:** không “sửa” test dự kiến này bằng cách hạ gate giữa execution. Phân biệt condition failure với infrastructure failure trong metadata/log.").replace(
"Next: [Security and cost]", "Tiếp theo: [Bảo mật và chi phí]")
pair(CONTENT / "5-Workshop" / "5.9-Pipeline" / "5.9.2-Intentional-Failure", "Intentional failure", "Thất bại có chủ đích", 2, "5.9.2.", fail_en, fail_vi)


security_en = """# Security and cost

## Controls implemented

- IAM roles instead of access keys; SageMaker/Lambda trust policies separated.
- SageMaker S3 access scoped to the project bucket/prefix; `iam:PassRole` limited to managed-job needs.
- Lambda restricted to `sagemaker:InvokeEndpoint` on the required endpoint.
- S3 private; no real patient/private data; public screenshots must mask account IDs, active URLs, and sensitive ARNs.
- Budget and alerts, project tags, three HPO trials, one endpoint, and job-based compute.

Expected evidence `AWS-02/03/07–14` proves budgets, tagging, role permissions/trust and scoped policies when supplied. Configuration screenshots do not prove an exact final cost, so none is claimed.

```bash
aws sagemaker list-endpoints --region "$AWS_REGION"
aws cloudwatch describe-alarms --region "$AWS_REGION"
```

The endpoint is the principal continuously billed resource; Processing/Training/HPO jobs charge while running, and S3/logs/metrics also have usage costs. Retain evidence before cleanup, then remove compute.

**Troubleshooting:** AccessDenied should be fixed by identifying the exact denied action/resource—not by adding administrator access.

Next: [Cleanup](../5.11-Cleanup/)."""
security_vi = security_en.replace("# Security and cost", "# Bảo mật và chi phí").replace(
"## Controls implemented", "## Kiểm soát đã hiện thực").replace(
"IAM roles instead of access keys; SageMaker/Lambda trust policies separated.",
"Dùng IAM role thay access key; tách trust policy SageMaker/Lambda.").replace(
"SageMaker S3 access scoped to the project bucket/prefix;", "Quyền S3 của SageMaker giới hạn ở bucket/prefix dự án;").replace(
"limited to managed-job needs.", "giới hạn theo nhu cầu managed job.").replace(
"Lambda restricted to", "Lambda giới hạn").replace("on the required endpoint.", "trên endpoint cần thiết.").replace(
"S3 private; no real patient/private data; public screenshots must mask account IDs, active URLs, and sensitive ARNs.",
"S3 private; không dùng dữ liệu bệnh nhân/private; ảnh public phải che account ID, URL active và ARN nhạy cảm.").replace(
"Budget and alerts, project tags, three HPO trials, one endpoint, and job-based compute.",
"Budget/alert, project tags, ba HPO trial, một endpoint và compute dạng job.").replace(
"Expected evidence", "Minh chứng cần có").replace(
"proves budgets, tagging, role permissions/trust and scoped policies when supplied. Configuration screenshots do not prove an exact final cost, so none is claimed.",
"chứng minh budget, tag, role permission/trust và policy có phạm vi khi được bổ sung. Ảnh cấu hình không chứng minh tổng chi phí nên không tuyên bố con số.").replace(
"The endpoint is the principal continuously billed resource; Processing/Training/HPO jobs charge while running, and S3/logs/metrics also have usage costs. Retain evidence before cleanup, then remove compute.",
"Endpoint là tài nguyên chính tính phí liên tục; Processing/Training/HPO tính phí khi chạy, S3/log/metric cũng có phí. Giữ minh chứng trước cleanup rồi xóa compute.").replace(
"**Troubleshooting:** AccessDenied should be fixed by identifying the exact denied action/resource—not by adding administrator access.",
"**Xử lý lỗi:** sửa AccessDenied bằng cách xác định đúng action/resource bị từ chối, không thêm administrator access.").replace(
"Next: [Cleanup]", "Tiếp theo: [Cleanup]")
workshop_pair("5.10-Security-Cost", 10, "Security and cost", "Bảo mật và chi phí", security_en, security_vi)

cleanup_en = """# Cleanup runbook

**Status: TODO — these commands are planned and cleanup completion is not claimed. Add deletion and stopped-application evidence after execution.**

Preserve sanitized evidence, Registry/Pipeline history, and reports until the report is finalized. Then delete in dependency order:

```bash
# 1. Monitoring and alarm
aws sagemaker delete-monitoring-schedule --monitoring-schedule-name heart-risk-monitor --region "$AWS_REGION"
aws cloudwatch delete-alarms --alarm-names heart-risk-custom-drift heart-risk-age-drift --region "$AWS_REGION"

# 2. Endpoint; deletion is asynchronous
aws sagemaker delete-endpoint --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"
aws sagemaker wait endpoint-deleted --endpoint-name "$ENDPOINT_NAME" --region "$AWS_REGION"

# 3. Discover exact dependent names before deleting configs/models
aws sagemaker list-endpoint-configs --name-contains heart-risk --region "$AWS_REGION"
aws sagemaker list-models --name-contains heart-risk --region "$AWS_REGION"

# 4. API and Lambda (resolve API_ID first; do not paste an active URL)
aws apigatewayv2 get-apis --region "$AWS_REGION"
aws lambda delete-function --function-name heart-risk-api --region "$AWS_REGION"
```

Delete the resolved endpoint config/model with their explicit names. Stop/delete running Studio/JupyterLab applications from **SageMaker AI → Domains → User profiles → Applications**. Pipeline deletion is optional only after history/evidence is no longer required. Keep or archive the private S3 evidence/report prefix according to retention needs.

**Errors:** endpoint config deletion fails while endpoint deletion is pending; wait and describe state. Never use broad recursive deletion or delete the bucket before verifying the exact target.

Next: [Results and limitations](../5.12-Results-Limitations/)."""
cleanup_vi = cleanup_en.replace("# Cleanup runbook", "# Runbook cleanup").replace(
"**Status: TODO — these commands are planned and cleanup completion is not claimed. Add deletion and stopped-application evidence after execution.**",
"**Trạng thái: TODO — đây là lệnh dự kiến và chưa tuyên bố cleanup hoàn tất. Thêm minh chứng xóa tài nguyên và dừng ứng dụng sau khi chạy.**").replace(
"Preserve sanitized evidence, Registry/Pipeline history, and reports until the report is finalized. Then delete in dependency order:",
"Giữ minh chứng đã che thông tin, history Registry/Pipeline và report đến khi báo cáo hoàn tất. Sau đó xóa theo thứ tự phụ thuộc:").replace(
"Delete the resolved endpoint config/model with their explicit names. Stop/delete running Studio/JupyterLab applications from",
"Xóa endpoint config/model đã resolve bằng tên cụ thể. Dừng/xóa Studio/JupyterLab application đang chạy tại").replace(
"Pipeline deletion is optional only after history/evidence is no longer required. Keep or archive the private S3 evidence/report prefix according to retention needs.",
"Chỉ tùy chọn xóa Pipeline sau khi không cần history/minh chứng. Giữ hoặc archive prefix S3 private theo yêu cầu retention.").replace(
"**Errors:** endpoint config deletion fails while endpoint deletion is pending; wait and describe state. Never use broad recursive deletion or delete the bucket before verifying the exact target.",
"**Lỗi:** xóa endpoint config thất bại khi endpoint còn đang xóa; hãy chờ và kiểm tra trạng thái. Không xóa recursive phạm vi rộng hoặc xóa bucket trước khi xác minh target.").replace(
"Next: [Results and limitations]", "Tiếp theo: [Kết quả và giới hạn]")
workshop_pair("5.11-Cleanup", 11, "Cleanup", "Cleanup", cleanup_en, cleanup_vi)

results_en = f"""# Results, limitations, and future work

## Results

| Area | Result |
|---|---|
| Data | 7,000 rows; 20 raw/36 processed features; train-only fit |
| Model | LR selected; test AUC 0.885515, F1 0.768903 |
| API | health/predict plus 200/400/502 behavior |
| Drift | six features; custom metrics 1 and 6; alarm ALARM |
| Pipeline | pass registers v3 pending; 0.99 test blocks registry |

## Problems encountered and resolutions

| Problem | Root cause | Resolution |
|---|---|---|
| Leakage risk | preprocessing before proper split | split first; fit train only |
| `ml.t3.medium` rejected | unsupported package instance | use `ml.m5.large` |
| Official drift metric absent | expected metric not published in test | custom Processing and metrics |
| Alarm returned/stayed OK | sparse periods treated non-breaching | `TreatMissingData=ignore`; fresh point |
| Pipeline absent initially | not upserted | run definition/upsert first |
| SDK v2 warnings | SageMaker SDK v2 | document migration to v3 |
| Alarm history denied | missing permission | use `describe-alarms`; optionally scope history permission |

## Personal contributions

Custom dataset and SHA-256/idempotent upload design; leakage-safe preprocessing; LR/XGBoost/HPO comparison; three gates and manual promotion; API error contract; Data Capture; custom drift/CloudWatch fallback; sparse metric fix; pass/fail Pipeline; bilingual reproducible documentation and disclaimer.

## Limitations

Non-clinical data; no fairness assessment or probability calibration; only three HPO trials; one endpoint; no production authentication; PoC drift rules; expected official feature metric not observed; SDK v2 debt; no automated retraining, CI/CD, or IaC.

## Future work

Evaluate fairness/calibration with appropriate governance; add authentication, throttling, private networking, encryption strategy, Auto Scaling, IaC/CI/CD, SDK v3 migration, automated-but-approved retraining, and cost evidence.

{disclaimer_en}
"""
results_vi = f"""# Kết quả, giới hạn và hướng phát triển

## Kết quả

| Nhóm | Kết quả |
|---|---|
| Dữ liệu | 7.000 dòng; 20 raw/36 processed feature; fit train-only |
| Model | chọn LR; test AUC 0,885515, F1 0,768903 |
| API | health/predict và hành vi 200/400/502 |
| Drift | sáu feature; custom metric 1 và 6; alarm ALARM |
| Pipeline | pass đăng ký v3 pending; test 0,99 chặn registry |

## Vấn đề và cách xử lý

| Vấn đề | Nguyên nhân | Cách xử lý |
|---|---|---|
| Nguy cơ leakage | preprocessing trước split đúng | split trước; fit train-only |
| `ml.t3.medium` bị từ chối | instance không được package hỗ trợ | dùng `ml.m5.large` |
| Thiếu official drift metric | metric mong đợi không publish khi test | custom Processing và metric |
| Alarm OK không đúng | period thưa bị coi non-breaching | `TreatMissingData=ignore`; datapoint mới |
| Ban đầu thiếu Pipeline | chưa upsert | chạy định nghĩa/upsert trước |
| Cảnh báo SDK v2 | SageMaker SDK v2 | lên kế hoạch chuyển v3 |
| Không có alarm history | thiếu permission | dùng `describe-alarms`; tùy chọn quyền history có phạm vi |

## Đóng góp cá nhân

Dataset tùy biến và thiết kế SHA-256/idempotent upload; preprocessing chống leakage; so sánh LR/XGBoost/HPO; ba gate và promotion thủ công; API error contract; Data Capture; custom drift/CloudWatch fallback; sửa sparse metric; Pipeline pass/fail; tài liệu song ngữ có thể tái lập và disclaimer.

## Giới hạn

Dữ liệu phi lâm sàng; chưa fairness/calibration; chỉ ba HPO trial; một endpoint; chưa production authentication; drift rule PoC; không quan sát official feature metric; nợ SDK v2; chưa automated retraining, CI/CD, IaC.

## Hướng phát triển

Đánh giá fairness/calibration với governance phù hợp; thêm authentication, throttling, private networking, encryption strategy, Auto Scaling, IaC/CI/CD, SDK v3, retraining tự động có phê duyệt và minh chứng chi phí.

{disclaimer_vi}
"""
workshop_pair("5.12-Results-Limitations", 12, "Results and limitations", "Kết quả và giới hạn", results_en, results_vi)


self_en = """# Self-evaluation

Ratings are intentionally left for the student to select; examples are factual and improvement actions are concrete.

| Criterion | Rating | Project example | Improvement action |
|---|---|---|---|
| Knowledge | TODO: Good/Fair/Average | implemented a multi-service SageMaker MLOps flow | deepen networking, governance, SDK v3 |
| Ability to learn | TODO | learned managed Processing, Registry, monitoring, Pipeline | reproduce with IaC |
| Proactiveness | TODO | validated preprocessing locally before managed jobs | define acceptance tests earlier |
| Discipline | TODO | maintained versioned outputs and quality gates | improve schedule/evidence capture |
| Communication | TODO | produced bilingual technical documentation | request verified mentor feedback |
| Teamwork | TODO | TODO: add a verified collaboration example | record decisions and owners |
| Problem solving | TODO | custom drift fallback when expected metric was absent | compare official monitor configurations |
| Contribution | TODO | integrated API, capture, alarm, pass/fail Pipeline | package reusable automation |

No mentor or team claim is inferred where evidence was not supplied."""
self_vi = """# Tự đánh giá

Điểm đánh giá được để sinh viên tự chọn; ví dụ bám theo dự án và hành động cải thiện cụ thể.

| Tiêu chí | Mức | Ví dụ dự án | Hành động cải thiện |
|---|---|---|---|
| Kiến thức | TODO: Good/Fair/Average | hiện thực quy trình SageMaker MLOps đa dịch vụ | đào sâu networking, governance, SDK v3 |
| Khả năng học | TODO | học Processing, Registry, monitoring, Pipeline managed | tái lập bằng IaC |
| Chủ động | TODO | validate preprocessing local trước managed job | định nghĩa acceptance test sớm hơn |
| Kỷ luật | TODO | giữ output có version và quality gate | cải thiện lịch và capture minh chứng |
| Giao tiếp | TODO | viết tài liệu kỹ thuật song ngữ | xin feedback mentor đã xác minh |
| Làm việc nhóm | TODO | TODO: thêm ví dụ cộng tác đã xác minh | ghi lại quyết định và owner |
| Giải quyết vấn đề | TODO | tạo custom drift khi thiếu metric mong đợi | so sánh cấu hình official monitor |
| Đóng góp | TODO | tích hợp API, capture, alarm, Pipeline pass/fail | đóng gói automation tái sử dụng |

Không suy diễn thông tin mentor hay teamwork khi chưa có minh chứng."""
pair(CONTENT / "6-Self-evaluation", "Self-evaluation", "Tự đánh giá", 6, "6.", self_en, self_vi)

feedback_en = """# Sharing and feedback

## Overall experience and satisfaction

TODO: Add a personal, verified reflection and satisfaction level.

## Most valuable learning

The documented technical learning is the transition from a notebook experiment to traceable managed jobs, manual promotion, operational error handling, drift visibility, and pass/fail automation.

## Mentor/admin support

TODO: Add verified feedback without inventing names, meetings, or benefits.

## Technical and soft-skill growth

The project demonstrates growth in AWS service integration, leakage-aware ML evaluation, IAM/cost hygiene, troubleshooting, and bilingual documentation. TODO: add verified communication/teamwork examples.

## Difficulties

Instance compatibility, missing expected official drift metrics, sparse alarm periods, Pipeline upsert order, and SDK v2 warnings required explicit diagnosis.

## Suggestions for FCAJ

Earlier quota/IAM checklists, a mandatory cost-cleanup checklist, an architecture review before deployment, and a complete bilingual sample could reduce avoidable setup and reporting ambiguity.

## Recommendation and career direction

TODO: State whether you would recommend the program and why.  
TODO: Add your verified future career direction."""
feedback_vi = """# Chia sẻ và phản hồi

## Trải nghiệm tổng thể và mức độ hài lòng

TODO: Thêm cảm nhận cá nhân đã xác minh và mức độ hài lòng.

## Bài học giá trị nhất

Bài học kỹ thuật đã ghi nhận là chuyển từ thử nghiệm notebook sang managed job có truy vết, promotion thủ công, xử lý lỗi vận hành, quan sát drift và automation pass/fail.

## Hỗ trợ từ mentor/admin

TODO: Thêm phản hồi đã xác minh, không tự tạo tên, cuộc họp hay phúc lợi.

## Phát triển kỹ thuật và kỹ năng mềm

Dự án thể hiện tiến bộ về tích hợp dịch vụ AWS, đánh giá ML chú ý leakage, IAM/chi phí, troubleshooting và tài liệu song ngữ. TODO: thêm ví dụ giao tiếp/teamwork đã xác minh.

## Khó khăn

Tính tương thích instance, thiếu official drift metric mong đợi, period alarm thưa, thứ tự upsert Pipeline và cảnh báo SDK v2 cần được chẩn đoán rõ.

## Đề xuất cho FCAJ

Checklist quota/IAM sớm, checklist cleanup bắt buộc, review kiến trúc trước deployment và mẫu song ngữ đầy đủ có thể giảm lỗi setup và mơ hồ khi viết báo cáo.

## Khuyến nghị và định hướng nghề nghiệp

TODO: Nêu có giới thiệu chương trình cho bạn bè hay không và lý do.  
TODO: Thêm định hướng nghề nghiệp đã xác minh."""
pair(CONTENT / "7-Feedback", "Sharing and Feedback", "Chia sẻ và phản hồi", 7, "7.", feedback_en, feedback_vi)


# Original, accessible SVG architecture.
arch_dir = ROOT / "static" / "images" / "architecture"
arch_dir.mkdir(parents=True, exist_ok=True)
(arch_dir / "heart-risk-architecture.svg").write_text("""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760" role="img" aria-labelledby="title desc">
<title id="title">Heart Risk MLOps architecture on AWS</title>
<desc id="desc">Offline training, online inference, monitoring, and quality-gated pipeline flows inside an AWS Cloud boundary.</desc>
<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2878b5"/></marker><marker id="i" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#d86613"/></marker><marker id="m" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#5b3f91"/></marker><style>.box{fill:#fff;stroke:#4b5563;stroke-width:2;rx:8}.h{font:700 17px Arial;fill:#111827}.t{font:14px Arial;fill:#1f2937}.lane{fill:#f8fafc;stroke:#cbd5e1;stroke-width:1}.data{stroke:#2878b5;stroke-width:3;fill:none;marker-end:url(#a)}.infer{stroke:#d86613;stroke-width:3;fill:none;marker-end:url(#i)}.mon{stroke:#5b3f91;stroke-width:3;fill:none;marker-end:url(#m)}</style></defs>
<rect x="18" y="18" width="1164" height="724" rx="18" fill="#fff8ee" stroke="#ff9900" stroke-width="3"/><text x="45" y="52" class="h">AWS Cloud · us-east-1</text>
<rect class="lane" x="45" y="72" width="1110" height="185" rx="10"/><text x="65" y="100" class="h">Offline data and ML flow</text>
<g><rect class="box" x="65" y="125" width="150" height="72"/><text x="140" y="153" text-anchor="middle" class="h">Amazon S3</text><text x="140" y="177" text-anchor="middle" class="t">raw + manifest</text><rect class="box" x="270" y="125" width="165" height="72"/><text x="352" y="153" text-anchor="middle" class="h">Processing</text><text x="352" y="177" text-anchor="middle" class="t">train-only fit</text><rect class="box" x="490" y="125" width="165" height="72"/><text x="572" y="153" text-anchor="middle" class="h">Training / HPO</text><text x="572" y="177" text-anchor="middle" class="t">LR + XGBoost</text><rect class="box" x="710" y="125" width="165" height="72"/><text x="792" y="153" text-anchor="middle" class="h">Evaluation</text><text x="792" y="177" text-anchor="middle" class="t">AUC · F1 · recall</text><rect class="box" x="930" y="125" width="185" height="72"/><text x="1022" y="153" text-anchor="middle" class="h">Model Registry</text><text x="1022" y="177" text-anchor="middle" class="t">manual approval</text><path class="data" d="M215 161H265"/><path class="data" d="M435 161H485"/><path class="data" d="M655 161H705"/><path class="data" d="M875 161H925"/></g>
<rect class="lane" x="45" y="275" width="1110" height="150" rx="10"/><text x="65" y="303" class="h">Online inference flow</text>
<g><rect class="box" x="65" y="330" width="170" height="62"/><text x="150" y="356" text-anchor="middle" class="h">API Gateway</text><text x="150" y="378" text-anchor="middle" class="t">/health · /predict</text><rect class="box" x="330" y="330" width="170" height="62"/><text x="415" y="356" text-anchor="middle" class="h">AWS Lambda</text><text x="415" y="378" text-anchor="middle" class="t">validate + invoke</text><rect class="box" x="595" y="330" width="210" height="62"/><text x="700" y="356" text-anchor="middle" class="h">SageMaker Endpoint</text><text x="700" y="378" text-anchor="middle" class="t">heart-risk-endpoint</text><rect class="box" x="900" y="330" width="180" height="62"/><text x="990" y="356" text-anchor="middle" class="h">JSON response</text><text x="990" y="378" text-anchor="middle" class="t">prediction + disclaimer</text><path class="infer" d="M235 361H325"/><path class="infer" d="M500 361H590"/><path class="infer" d="M805 361H895"/></g>
<rect class="lane" x="45" y="443" width="1110" height="135" rx="10"/><text x="65" y="471" class="h">Monitoring flow</text>
<g><rect class="box" x="65" y="493" width="190" height="58"/><text x="160" y="518" text-anchor="middle" class="h">Data Capture / S3</text><text x="160" y="539" text-anchor="middle" class="t">JSONL current data</text><rect class="box" x="340" y="493" width="190" height="58"/><text x="435" y="518" text-anchor="middle" class="h">Custom Processing</text><text x="435" y="539" text-anchor="middle" class="t">drift report</text><rect class="box" x="615" y="493" width="190" height="58"/><text x="710" y="518" text-anchor="middle" class="h">CloudWatch</text><text x="710" y="539" text-anchor="middle" class="t">custom metrics</text><rect class="box" x="890" y="493" width="190" height="58"/><text x="980" y="518" text-anchor="middle" class="h">Alarm</text><text x="980" y="539" text-anchor="middle" class="t">ALARM · missing ignore</text><path class="mon" d="M255 522H335"/><path class="mon" d="M530 522H610"/><path class="mon" d="M805 522H885"/></g>
<rect class="lane" x="45" y="596" width="1110" height="98" rx="10"/><text x="65" y="624" class="h">Pipeline quality gate</text><text x="65" y="653" class="t">Preprocess → Train → Evaluate → Check AUC/F1/Recall</text><path class="data" d="M440 650H595"/><text x="620" y="642" class="t">pass → RegisterModel</text><text x="620" y="670" class="t">fail → MetricThresholdFailed</text>
<g><line x1="760" y1="716" x2="805" y2="716" class="data"/><text x="815" y="721" class="t">data</text><line x1="880" y1="716" x2="925" y2="716" class="infer"/><text x="935" y="721" class="t">inference</text><line x1="1030" y1="716" x2="1075" y2="716" class="mon"/><text x="1085" y="721" class="t">monitoring</text></g></svg>""", encoding="utf-8")


# Remove obsolete sample assets and create safe attachment placeholders only.
sample_images = ROOT / "static" / "images" / "5-Workshop"
if sample_images.exists():
    shutil.rmtree(sample_images)
sample_proposal = ROOT / "static" / "images" / "2-Proposal"
if sample_proposal.exists():
    shutil.rmtree(sample_proposal)
(ROOT / "static" / "images" / "evidence").mkdir(parents=True, exist_ok=True)
attach = ROOT / "static" / "attachments" / "heart-risk"
attach.mkdir(parents=True, exist_ok=True)
(attach / "README.txt").write_text(
    "Heart-risk workshop attachments\n\n"
    "The supplied evidence screenshots are stored separately under static/images/evidence and linked from the bilingual workshop.\n"
    "No project source files were present when the report was generated.\n"
    "Add only reviewed, non-sensitive source files here. Never add credentials, active API URLs, private data, or unmasked account identifiers.\n",
    encoding="utf-8",
)
(attach / "sample-request.json").write_text(
    '{\n  "TODO": "Replace with the verified 20-feature request schema before use"\n}\n',
    encoding="utf-8",
)


# Project-facing README; preserve the original implementation brief separately.
readme = """# FCAJ Internship Report — Heart Risk MLOps

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

Open <http://localhost:1313/>.

Build the production site:

```bash
hugo --minify --baseURL http://localhost:8080/
```

Serve the generated site with:

```bash
python3 -m http.server 8080 --directory public
```

Then open <http://localhost:8080/>.

## Deployment

`.github/workflows/hugo.yml` builds with Hugo Extended 0.134.3 on pushes to
`main`, overrides `baseURL` with
`https://duochip.github.io/fcj-heart-risk-report/`, and publishes `public/` to
the `gh-pages` branch.

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
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("Generated bilingual report content.")
