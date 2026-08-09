---
title: "Tuần 8: SageMaker Pipeline và hoàn thiện báo cáo"
weight: 8
chapter: false
pre: " <b>1.8.</b> "
---

**Thời gian:** 03/08/2026 – 15/08/2026

## Mục tiêu và công việc hoàn thành

- Tích hợp preprocessing, training, evaluation, condition, registration và fail step vào SageMaker Pipeline.
- Chạy luồng pass và intentional-fail để kiểm tra quality gate.
- Rà soát dữ liệu, IAM, chi phí và vòng đời tài nguyên; tổ chức website Hugo song ngữ, workshop, báo cáo và runbook cleanup.

## Vấn đề và quyết định

- Pipeline chưa tồn tại trước lần tạo đầu tiên nên định nghĩa/upsert được chạy trước bước list hoặc execute.
- Minh chứng phải được lưu trước cleanup; không tuyên bố đã xóa tài nguyên nếu chưa có log xác nhận.

## Kết quả

Luồng thành công đăng ký Model Package version 3 ở trạng thái `PendingManualApproval`. Ngưỡng AUC 0,99 đi vào fail step và chặn đăng ký đúng thiết kế. Từ 10–15/08, kết quả được rà soát, tài liệu hóa và bàn giao để kết thúc kỳ thực tập.

## Minh chứng

Danh mục: `W8-01–W8-07`, gồm Pipeline graph, execution thành công, condition pass và intentional failure.

## Tổng kết

Tám tuần tạo thành quy trình liên tục từ môi trường, dữ liệu, huấn luyện đến triển khai, monitoring, automation và báo cáo; output có version được tái sử dụng thay vì phụ thuộc notebook thủ công.
