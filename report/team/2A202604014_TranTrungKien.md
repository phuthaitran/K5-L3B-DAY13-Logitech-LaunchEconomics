# Báo cáo cá nhân — TranTrungKien-2A202604014

## 1. Thông tin thành viên

- Họ tên: Trần Trung Kiên
- MSSV: 2A202604014
- Email:
- Vai trong nhóm: TV3 - Người gắn nhãn 1 (Labeler 1 & Gatekeeper điều kiện "Xong khi")

## 2. Phần việc phụ trách

- **Giám sát điều kiện "Xong khi":** Theo dõi, nghiệm thu điều kiện hoàn thành của từng Checkpoint (CP1 đến CP5) để đảm bảo nhóm đi đúng tiến độ và không bị trừ điểm theo Rubric.
- **Nhiệm vụ C (CP3):** Gắn nhãn độc lập 20 ca lỗi theo 5 phân loại của Google PAIR; đối soát tính tỉ lệ đồng thuận với TV4 (đạt $\ge 80\%$); thống nhất nhãn và viết quy tắc phân biệt cho các ca không trùng; chủ trì xây dựng bảng khắc phục cho 5 ca lỗi đại diện với cách phát hiện đo được và gán 1 vai trò phụ trách cụ thể.
- **Nhiệm vụ D (CP4):** Trả lời 5 câu hỏi D2 về kiểm tra "tách được tác động" (Concurrent control, Randomization, Spillover risk, Predeclared, $\ge 20$ clusters); thiết kế và chuẩn hóa ít nhất 3 luật dừng an toàn/chi phí/sử dụng theo mẫu bắt buộc `NẾU – TRONG – THÌ – KHÔNG THÌ` trong file `pilot_plan.yaml`.
- **Duyệt chéo Gate 2a (CP5):** Phản biện chuyên sâu mục 5 (lỗi) và mục 6 (kế hoạch pilot) của nhóm bạn, chấm điểm vào `phieu_cham.md`; bảo vệ phương án phân loại lỗi và luật dừng của nhóm mình trước hội đồng.

## 3. Đóng góp cụ thể

- Độc lập gắn nhãn 20 ca lỗi trong 8 phút đầu của CP3, đối soát với TV4 đạt tỉ lệ đồng thuận 100% (20/20 ca trùng nhau).
- Viết chi tiết bảng khắc phục cho 5 ca đại diện (Ca 9 - Do người dùng, Ca 7 - Hệ thống, Ca 18 - Ngữ cảnh, Ca 4 - Giới hạn hệ thống, Ca 17 - Ngầm) kèm event/ngưỡng phát hiện và chức danh chịu trách nhiệm.
- Hoàn thành phần D2 và 3 luật dừng trong file `pilot_plan.yaml`, đảm bảo đúng cú pháp 4 vế, ngưỡng an toàn mở lại $\le 6\%$ hoặc chênh $+2$ điểm (dựa trên baseline 4,25%), xóa toàn bộ dấu `?` trong file YAML.
- Rà soát hồ sơ v0, phát hiện và loại bỏ các từ cấm (như từ prod), đảm bảo toàn bộ số liệu giả lập được gắn nhãn `simulated`.

## 4. Bằng chứng

- File [report/team/bang_loi.md](file:///c:/Users/Admin/OneDrive%20-%20National%20Economics%20University/AITC/Lab/K5-L3B-DAY13-Logitech-LaunchEconomics/report/team/bang_loi.md): Bộ nhãn của Người 1, tỷ lệ đồng thuận, quy tắc phân biệt và bảng khắc phục 5 ca.
- File [report/team/pilot_plan.yaml](file:///c:/Users/Admin/OneDrive%20-%20National%20Economics%20University/AITC/Lab/K5-L3B-DAY13-Logitech-LaunchEconomics/report/team/pilot_plan.yaml): Mục D2, các trường `identifiability`, và 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ.
- File [report/team/phieu_cham.md](file:///c:/Users/Admin/OneDrive%20-%20National%20Economics%20University/AITC/Lab/K5-L3B-DAY13-Logitech-LaunchEconomics/report/team/phieu_cham.md): Phiếu chấm chéo Gate 2a cho nhóm bạn.

## 5. Công cụ AI đã dùng

- **Antigravity (Gemini 3.8 Flash):** Sử dụng để rà soát đề bài, kiểm tra chéo các công thức tính cỡ mẫu, gợi ý cấu trúc cú pháp luật dừng YAML và kiểm tra tính hợp lệ cú pháp `yaml.safe_load`.
- **Cách tự kiểm tra kết quả:** Tự đối soát 20 ca lỗi theo nguyên tắc gốc của Google PAIR; chạy lệnh `yaml.safe_load` để xác nhận file cấu hình pilot không lỗi cú pháp; đối chiếu từng mục trong hồ sơ với rubric chấm thi.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, đúng hạn 100% các phần việc được giao theo vai TV3.
- Phối hợp nhịp nhàng với TV4 trong việc gắn nhãn và chuyển giao số liệu vào hồ sơ launch v0.
- Điểm tự đánh giá đóng góp: 10/10.
