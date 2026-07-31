---
title: "Chia sẻ và phản hồi"
weight: 7
chapter: false
pre: " <b>7.</b> "
---

## Trải nghiệm tổng thể và mức độ hài lòng

Tôi đánh giá trải nghiệm thực tập FCAJ ở mức **8/10**. Chương trình tạo điều kiện để tôi kết nối Data Engineering, Machine Learning và các dịch vụ AWS trong một dự án end-to-end thay vì học từng dịch vụ rời rạc. Quá trình xây dựng Heart Risk MLOps PoC giúp tôi hiểu một hệ thống ML hữu ích không chỉ có model đã huấn luyện; data preparation có thể tái lập, evaluation gate, model governance, triển khai, monitoring, kiểm soát chi phí, bảo mật và tài liệu rõ ràng đều quan trọng như nhau.

Kết quả khiến tôi hài lòng nhất là chuyển quy trình notebook ban đầu thành một hệ thống có thể giải thích và demo từ dữ liệu thô đến API prediction và drift alarm. Dự án vẫn là PoC phục vụ học tập, không phải hệ thống y tế production, nhưng giúp tôi hình dung cụ thể các tiêu chuẩn kỹ thuật cần có sau giai đoạn thử nghiệm.

## Bài học giá trị nhất

Bài học giá trị nhất là quá trình chuyển từ thử nghiệm notebook sang managed workflow có khả năng truy vết. Tôi đã học cách:

- chia dữ liệu trước khi fit preprocessing để tránh data leakage;
- dùng SageMaker Processing và Training Job thay vì phụ thuộc notebook chạy liên tục;
- so sánh model bằng ROC-AUC, F1 và recall thay vì chọn theo một metric;
- đăng ký model với manual approval và áp dụng quality gate pass/fail trong SageMaker Pipelines;
- cung cấp inference qua Lambda và API Gateway với input validation và error response an toàn;
- chuyển inference data đã capture thành custom drift metric và CloudWatch alarm;
- xem IAM scope, vòng đời tài nguyên, budget alert và cleanup là quyết định kiến trúc.

## Hỗ trợ và môi trường học tập

Cấu trúc FCAJ khuyến khích tự nghiên cứu và hiện thực thay vì chỉ làm theo một lab cố định. Yêu cầu về báo cáo và workshop cũng buộc tôi lưu minh chứng, giải thích quyết định thiết kế và trình bày kết quả bằng cả tiếng Việt lẫn tiếng Anh.

Cộng đồng AWS Study Group tạo môi trường hữu ích để chia sẻ kiến thức kỹ thuật. Hai bài về AWS Lambda và Amazon SageMaker đã được đăng, trong khi bài thứ ba về chi phí SageMaker MLOps đang chờ duyệt. Việc tham dự buổi chia sẻ giải pháp Agentic AI và Hackathon ngày 25/07 cũng giúp tôi so sánh cách các nhóm khác xác định vấn đề, trình bày kiến trúc và demo MVP.

Tôi không gán phản hồi cụ thể cho một mentor cá nhân vì báo cáo hiện không có hồ sơ phản hồi mentor chính thức.

## Phát triển kỹ thuật và kỹ năng mềm

Về kỹ thuật, tôi tiến bộ trong xử lý dữ liệu bằng Python, đánh giá ML có chú ý leakage, SageMaker managed job, triển khai model, CloudWatch monitoring, IAM và vận hành AWS có ý thức chi phí. Tôi cũng làm việc có hệ thống hơn khi đọc log, cô lập nguyên nhân, kiểm tra component nhỏ ở local và lưu lại minh chứng cuối cùng.

Về kỹ năng mềm, việc viết workshop song ngữ cải thiện khả năng giao tiếp kỹ thuật và tổ chức một quy trình dài thành các bước có thể tái lập. Chuẩn bị bài viết cộng đồng giúp tôi chuyển chi tiết kỹ thuật thành bài học thực tế. Sự kiện ngày 25/07 cho tôi thấy giá trị của storyline vấn đề–giải pháp–tác động. Minh chứng teamwork hiện ít hơn minh chứng kỹ thuật, vì vậy dự án tiếp theo cần duy trì task ownership, decision log và review record rõ ràng ngay từ đầu.

## Khó khăn

Khó khăn chính không nằm ở việc train model mà ở tích hợp và hành vi vận hành:

- `ml.t3.medium` không được hỗ trợ cho một managed job nên phải đổi sang `ml.m5.large`;
- official feature-level drift metric mong đợi không xuất hiện nên tôi hiện thực custom Processing fallback minh bạch;
- custom metric thưa có thể làm sai hành vi alarm trước khi cấu hình `TreatMissingData=ignore`;
- quá trình tạo và cập nhật Pipeline cần trình tự upsert có tính idempotent;
- cảnh báo deprecation của SageMaker SDK v2 tạo ra công việc migration trong tương lai;
- endpoint, log, artifact và experiment đòi hỏi kỷ luật kiểm soát chi phí và cleanup.

Các vấn đề này giúp tôi học cách kiểm tra constraint của dịch vụ sớm, định nghĩa hành vi lỗi có thể quan sát và duy trì fallback có thể đo lường, giải thích được.

## Đề xuất cho FCAJ

Tôi đề xuất bổ sung một số checkpoint cho các khóa FCAJ tiếp theo:

1. kiểm tra mức độ sẵn sàng của môi trường ngay đầu kỳ, gồm Region, IAM, quota, instance được hỗ trợ và budget alert;
2. review kiến trúc ngắn trước khi học viên tạo tài nguyên tính phí;
3. checklist ước tính chi phí và cleanup bắt buộc cho từng milestone;
4. checklist minh chứng chỉ rõ screenshot, log, metric và public link cần thu thập;
5. một báo cáo song ngữ mẫu nhỏ với quy tắc rõ ràng cho những claim cần xác minh;
6. peer review định kỳ để học viên luyện giải thích quyết định và ghi nhận feedback trước tuần cuối.

## Khuyến nghị và định hướng nghề nghiệp

Tôi sẽ giới thiệu FCAJ cho các sinh viên đã có kiến thức lập trình cơ bản và muốn trải nghiệm thực tế việc kết nối nhiều dịch vụ AWS thành một giải pháp hoàn chỉnh. Chương trình mang lại nhiều giá trị nhất khi học viên chủ động thử nghiệm, đọc tài liệu dịch vụ, kiểm soát ngân sách và ghi lại vấn đề thay vì chỉ tái hiện các lệnh chạy thành công.

Định hướng nghề nghiệp của tôi là **Data Engineering, phát triển dần sang MLOps và cloud data platform**. Sau kỳ thực tập, các ưu tiên tiếp theo là thiết kế data pipeline vững hơn, Infrastructure as Code, automated testing và CI/CD, containerization, observability và bảo mật production. Tôi cũng muốn đào sâu SageMaker cùng các dịch vụ dữ liệu AWS để xây dựng hệ thống trong đó data preparation, model delivery và vận hành có thể tái lập, bảo trì lâu dài.
