---
title: "Tự đánh giá"
weight: 6
chapter: false
pre: " <b>6.</b> "
---

## Phương pháp đánh giá

Phần tự đánh giá sử dụng tám tiêu chí có trọng số bằng nhau. Mỗi tiêu chí được chấm theo thang 10 điểm và gắn với minh chứng đã tạo trong dự án Heart Risk MLOps. Mục tiêu tổng thể là **8,0/10**.

| Tiêu chí | Điểm | Mức | Minh chứng từ dự án | Hướng cải thiện |
|---|---:|---|---|---|
| Kiến thức | 8,5/10 | Tốt | Xây dựng quy trình đa dịch vụ với Amazon S3, SageMaker Processing, Training, HPO, Model Registry, Endpoint và Pipeline, kết hợp Lambda, API Gateway và CloudWatch. | Đào sâu private networking, governance và SageMaker Python SDK v3. |
| Khả năng học hỏi | 8,5/10 | Tốt | Chuyển từ thử nghiệm notebook cục bộ sang processing managed, đăng ký model, monitoring và thực thi pipeline. | Tái lập môi trường bằng Infrastructure as Code và CI/CD. |
| Tính chủ động | 8,0/10 | Tốt | Kiểm tra preprocessing cục bộ trước khi chạy managed job, thiết lập quality gate và thu thập minh chứng vận hành. | Xác định acceptance test và yêu cầu minh chứng ngay từ đầu mỗi mốc công việc. |
| Tính kỷ luật | 7,5/10 | Khá | Quản lý output có phiên bản trên S3, tách biệt xử lý train/test và sử dụng quality gate pass/fail. | Duy trì lịch công việc chặt chẽ hơn và ghi nhận đầy đủ minh chứng dọn dẹp tài nguyên. |
| Giao tiếp | 7,5/10 | Khá | Hoàn thiện báo cáo kỹ thuật song ngữ và chia sẻ hai bài viết kỹ thuật với cộng đồng AWS Study Group. | Trình bày kỹ thuật cô đọng hơn và ghi nhận phản hồi người review theo cấu trúc. |
| Làm việc nhóm | 7,0/10 | Khá | Phối hợp chia sẻ kiến thức dự án qua các bài viết cộng đồng và ghi nhận tài liệu tham khảo chung; tuy nhiên chưa lưu đầy đủ phân công công việc xuyên suốt dự án. | Duy trì decision log có người phụ trách, thời hạn và kết quả review. |
| Giải quyết vấn đề | 9,0/10 | Tốt | Thay metric drift chính thức bị thiếu bằng custom Processing job, sửa cách xử lý alarm khi metric thưa, đổi instance không được hỗ trợ và giúp quá trình tạo Pipeline có tính idempotent. | So sánh giải pháp monitoring tùy chỉnh với Model Monitor chính thức được cấu hình đầy đủ baseline. |
| Mức độ đóng góp | 8,0/10 | Tốt | Hoàn thiện PoC end-to-end gồm huấn luyện, triển khai, API inference, data capture, drift alarm và hai kịch bản Pipeline pass/fail. | Đóng gói các bước lặp lại thành module tái sử dụng, tự động hóa triển khai và dọn dẹp. |

## Kết quả tổng hợp

| Chỉ số | Kết quả |
|---|---:|
| Tổng điểm | **64,0/80** |
| Điểm trung bình | **8,0/10** |
| Mức tổng thể | **Tốt** |
| Mục tiêu | **Đạt** |

## Tự nhìn nhận

Kết quả nổi bật nhất là khả năng chẩn đoán lỗi tích hợp giữa quy trình ML và các dịch vụ AWS mà vẫn duy trì chất lượng dữ liệu và khả năng truy vết. Các khoảng trống chính không nằm ở kết quả PoC mà ở mức độ sẵn sàng production: Infrastructure as Code, kiểm thử và triển khai tự động, tăng cường bảo mật, cùng hồ sơ teamwork có hệ thống hơn. Đây là các ưu tiên cho vòng phát triển tiếp theo.
