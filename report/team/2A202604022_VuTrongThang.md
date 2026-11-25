# 202604022_VuTrongThang.md

## 1. Thông tin thành viên

- **Họ tên:** Vũ Trọng Thắng
- **MSSV:** 2A202604022
- **Email:** [Bổ sung email]
- **Vai trong nhóm:** TV2 – Người kiểm số

## 2. Phần việc phụ trách

- **Checkpoint 1 (A):** Kiểm tra và đối chiếu các số liệu trong mô hình chi phí.
- **Checkpoint 2 (B):** Phụ trách phân tích độ nhạy của mô hình chi phí, đánh giá ảnh hưởng của các yếu tố đầu vào và so sánh các kịch bản vận hành.
- **Checkpoint 3 (C):** Tham gia gắn nhãn độc lập 20 trường hợp lỗi.
- **Checkpoint 4 (D):** Phụ trách tính toán cỡ mẫu thử nghiệm, phân tích các yếu tố ảnh hưởng đến thiết kế pilot và cập nhật kế hoạch pilot.
- **Checkpoint 5 (E):** Hỗ trợ cung cấp số liệu chi phí và cỡ mẫu cho báo cáo nhóm.

## 3. Đóng góp cụ thể

### Checkpoint 2 – Sensitivity Analysis

- Xây dựng và phân tích 9 kịch bản độ nhạy.
- Đánh giá tác động khi giá token và chi phí kiểm duyệt cùng tăng gấp đôi.
- So sánh chi phí hệ thống khi giới hạn số lần thử lại là 1, 2 và 3.
- Phân tích kịch bản kiểm duyệt 100% đối với nhóm `noi_dia + hang_nang`.
- Xác định thứ tự ảnh hưởng của các yếu tố đến chi phí: rework, review và staff wage.

### Checkpoint 4 – Pilot Design

- Tính toán cỡ mẫu cần thiết cho thử nghiệm ở cấp request.
- Phân tích Design Effect khi phân cụm theo nhân viên và depot.
- Đánh giá giới hạn cỡ mẫu thực tế và mức độ ảnh hưởng đến statistical power.
- Chuẩn bị câu trả lời cho 5 câu hỏi thiết kế thử nghiệm nhân quả.
- Tính reopen rate 7 ngày: 51/1.200 trường hợp, tương đương khoảng 4,25% trên toàn bộ dữ liệu.
- Cập nhật các kết quả tính toán và thông tin liên quan vào kế hoạch pilot.

## 4. Bằng chứng

Các file đã chỉnh sửa:

- `src/lab13.py`: Bổ sung các phép tính và kết quả phân tích độ nhạy, cỡ mẫu, statistical power và reopen rate.
- `report/team/bang_chi_phi.md`: Bổ sung kết quả phân tích chi phí tại Checkpoint 2.
- `report/team/pilot_plan.yaml`: Cập nhật thông tin và kế hoạch liên quan đến Checkpoint 4.

Một số kết quả cụ thể:

- Chi phí CPS trong kịch bản tăng đồng thời giá token và chi phí review: khoảng 6.543 VND.
- Kịch bản giới hạn 2 lần thử lại có tổng chi phí hệ thống thấp nhất trong ba kịch bản đã phân tích: khoảng 6.901.220 VND.
- Cỡ mẫu request-level: 1.251 request mỗi nhóm.
- Reopen rate 7 ngày trên toàn bộ dữ liệu: 4,25%.

**Commit:** [Bổ sung commit hash sau khi hoàn tất commit và push]

## 5. Công cụ AI đã dùng

- **Codex:** Hỗ trợ đọc và phân tích cấu trúc code, triển khai các phép tính, cập nhật file báo cáo và kế hoạch pilot.
- **ChatGPT:** Hỗ trợ phân tích yêu cầu Lab, kiểm tra logic, giải thích kết quả và rà soát các điểm chưa nhất quán.

Tôi chủ động kiểm tra kết quả bằng cách đọc lại phần code và file đầu ra, chạy chương trình, kiểm tra cú pháp Python, chạy các bài kiểm thử liên quan và xem lại Git diff để xác định chính xác những file đã thay đổi.

## 6. Tự đánh giá

Tôi đã hoàn thành phần lớn nhiệm vụ được giao với vai trò người kiểm số, tập trung vào việc phân tích độ nhạy chi phí và thiết kế thử nghiệm pilot.

Qua Lab 13, tôi hiểu rõ hơn cách đánh giá ảnh hưởng của các biến đầu vào đến chi phí hệ thống, cách tính cỡ mẫu và những hạn chế khi triển khai thử nghiệm trong điều kiện nguồn lực thực tế.

Tôi nhận thấy mình vẫn cần cải thiện khả năng kiểm tra tính nhất quán giữa các kết quả phân tích, code và tài liệu báo cáo. Trong các công việc tiếp theo, tôi sẽ chú trọng hơn đến việc xác minh số liệu và ghi lại bằng chứng cụ thể cho từng phần việc.
