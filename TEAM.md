# Team

## Thông tin nhóm

- Tên nhóm: Logitech
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Logitech-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:
    - URL: https://github.com/phuthaitran/K5-L3B-DAY13-Logitech-LaunchEconomics
    - Commit chốt: `4f163bc`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trần Phú Thái | 2A202604001 | | phuthaitran | TV1 - Người viết Code |
|   2 | Vũ Trọng Thắng | 2A202604022 | | Thangvipsv4 | TV2 - người kiểm số |
|   3 | Trần Trung Kiên | 2A202604014 | | ttkien0710 | TV3 - Người gắn nhãn 1 |
|   4 | Đặng Thùy Dung | 2A202604116 | | dtdung14 | TV4 - Người gắn nhãn 2, kiêm giữ hồ sơ |


Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

## TranPhuThai-2A202604001

### Phần việc phụ trách

- **CP1 · Nhiệm vụ A:** viết `src/lab13.py` phần A1–A4 (ba hàm kinh tế chạy lại, `mo_hinh()`, tách theo loại, chi phí cố định) và điền phần A của `report/team/bang_chi_phi.md`.
- **CP5 · Nhiệm vụ E:** viết phần E1 trong `src/lab13.py` (tính thử ba chỉ số), hoàn thiện `report/team/chi_so.md`, điền mục 4 và dòng đề xuất của `report/team/ho_so_launch_v0.md`, viết `report/team/group_report.md`.

### Đóng góp cụ thể

- **A1:** ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** `mo_hinh()` tính token và tool trên mọi lần chạy kể cả lần lỗi, chia giá token cho 1.000 token, cộng phút xem lại và làm lại (simulated), mẫu số chỉ đếm `ket_qua == 'thanh_cong'`; có sẵn tham số giá, hệ số và `max_lan_chay` để CP2 gọi lại. Kết quả: 4.472 đ mỗi việc thành công [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu (274,7 đ).
- **A3, A4:** bảng theo bốn loại (`quoc_te` 1,88×, chạy lại không giúp: ok lần 1 là 30%, lần 3 là 2,2%); chi phí cố định 1.185 đ/việc ở 45.000 yêu cầu/tháng, 2.370 đ/việc nếu khối lượng còn một nửa [simulated].
- **E1:** code ba chỉ số cho toàn mẫu và phạm vi pilot: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); trong phạm vi `noi_dia` + `hang_nang`: 92,26% · 21,09% · 3,97%.
- **`chi_so.md`:** hai chỉ số tự đề xuất (tỉ lệ nhân viên mở gợi ý; tỉ lệ hoàn sai qua kiểm tra mẫu hằng tuần), 13 event có `trace_id` khớp tên event dùng trong `bang_loi.md`, kiểm tra chéo từng chỉ số với event dùng để tính.
- **Hồ sơ launch v0:** mục 4 và đề xuất **Go có điều kiện**, nêu cả con số bất lợi (xem lại 100% lên 0,98× – 1,03× [simulated]; power 0,64 nếu tác động thật chỉ 5 điểm) và bốn điều kiện có người phụ trách, ngày kiểm tra.

### Bằng chứng

- Commit `627aa5e` "CP1: mo hinh chi phi moi viec thanh cong (A1-A4)": `src/lab13.py`, `report/team/bang_chi_phi.md` (A1–A4).
- Commit CP5 (do tôi commit sau khi viết báo cáo này): phần E1 cuối `src/lab13.py`, `report/team/chi_so.md` (E1 và danh sách event), `report/team/ho_so_launch_v0.md` (mục 4, đề xuất), `report/team/group_report.md`.
- Chạy `cd src && python lab13.py` in đủ bảng A1–A4, B, D1, E1.

## VuTrongThang-2A202604022

### Phần việc phụ trách

- **Checkpoint 1 (A):** Kiểm tra và đối chiếu các số liệu trong mô hình chi phí.
- **Checkpoint 2 (B):** Phụ trách phân tích độ nhạy của mô hình chi phí, đánh giá ảnh hưởng của các yếu tố đầu vào và so sánh các kịch bản vận hành.
- **Checkpoint 3 (C):** Tham gia gắn nhãn độc lập 20 trường hợp lỗi.
- **Checkpoint 4 (D):** Phụ trách tính toán cỡ mẫu thử nghiệm, phân tích các yếu tố ảnh hưởng đến thiết kế pilot và cập nhật kế hoạch pilot.
- **Checkpoint 5 (E):** Hỗ trợ cung cấp số liệu chi phí và cỡ mẫu cho báo cáo nhóm.

### Đóng góp cụ thể

#### Checkpoint 2 – Sensitivity Analysis

- Xây dựng và phân tích 9 kịch bản độ nhạy.
- Đánh giá tác động khi giá token và chi phí kiểm duyệt cùng tăng gấp đôi.
- So sánh chi phí hệ thống khi giới hạn số lần thử lại là 1, 2 và 3.
- Phân tích kịch bản kiểm duyệt 100% đối với nhóm `noi_dia + hang_nang`.
- Xác định thứ tự ảnh hưởng của các yếu tố đến chi phí: rework, review và staff wage.

#### Checkpoint 4 – Pilot Design

- Tính toán cỡ mẫu cần thiết cho thử nghiệm ở cấp request.
- Phân tích Design Effect khi phân cụm theo nhân viên và depot.
- Đánh giá giới hạn cỡ mẫu thực tế và mức độ ảnh hưởng đến statistical power.
- Chuẩn bị câu trả lời cho 5 câu hỏi thiết kế thử nghiệm nhân quả.
- Tính reopen rate 7 ngày: 51/1.200 trường hợp, tương đương khoảng 4,25% trên toàn bộ dữ liệu.
- Cập nhật các kết quả tính toán và thông tin liên quan vào kế hoạch pilot.

### Bằng chứng

Các file đã chỉnh sửa:

- `src/lab13.py`: Bổ sung các phép tính và kết quả phân tích độ nhạy, cỡ mẫu, statistical power và reopen rate.
- `report/team/bang_chi_phi.md`: Bổ sung kết quả phân tích chi phí tại Checkpoint 2.
- `report/team/pilot_plan.yaml`: Cập nhật thông tin và kế hoạch liên quan đến Checkpoint 4.

Một số kết quả cụ thể:

- Chi phí CPS trong kịch bản tăng đồng thời giá token và chi phí review: khoảng 6.543 VND.
- Kịch bản giới hạn 2 lần thử lại có tổng chi phí hệ thống thấp nhất trong ba kịch bản đã phân tích: khoảng 6.901.220 VND.
- Cỡ mẫu request-level: 1.251 request mỗi nhóm.
- Reopen rate 7 ngày trên toàn bộ dữ liệu: 4,25%.

## TranTrungKien-2A202604014

### Phần việc phụ trách

- **Giám sát điều kiện "Xong khi":** Theo dõi, nghiệm thu điều kiện hoàn thành của từng Checkpoint (CP1 đến CP5) để đảm bảo nhóm đi đúng tiến độ và không bị trừ điểm theo Rubric.
- **Nhiệm vụ C (CP3):** Gắn nhãn độc lập 20 ca lỗi theo 5 phân loại của Google PAIR; đối soát tính tỉ lệ đồng thuận với TV4 (đạt $\ge 80\%$); thống nhất nhãn và viết quy tắc phân biệt cho các ca không trùng; chủ trì xây dựng bảng khắc phục cho 5 ca lỗi đại diện với cách phát hiện đo được và gán 1 vai trò phụ trách cụ thể.
- **Nhiệm vụ D (CP4):** Trả lời 5 câu hỏi D2 về kiểm tra "tách được tác động" (Concurrent control, Randomization, Spillover risk, Predeclared, $\ge 20$ clusters); thiết kế và chuẩn hóa ít nhất 3 luật dừng an toàn/chi phí/sử dụng theo mẫu bắt buộc `NẾU – TRONG – THÌ – KHÔNG THÌ` trong file `pilot_plan.yaml`.
- **Duyệt chéo Gate 2a (CP5):** Phản biện chuyên sâu mục 5 (lỗi) và mục 6 (kế hoạch pilot) của nhóm bạn, chấm điểm vào `phieu_cham.md`; bảo vệ phương án phân loại lỗi và luật dừng của nhóm mình trước hội đồng.

### Đóng góp cụ thể

- Độc lập gắn nhãn 20 ca lỗi trong 8 phút đầu của CP3, đối soát với TV4 đạt tỉ lệ đồng thuận 100% (20/20 ca trùng nhau).
- Viết chi tiết bảng khắc phục cho 5 ca đại diện (Ca 9 - Do người dùng, Ca 7 - Hệ thống, Ca 18 - Ngữ cảnh, Ca 4 - Giới hạn hệ thống, Ca 17 - Ngầm) kèm event/ngưỡng phát hiện và chức danh chịu trách nhiệm.
- Hoàn thành phần D2 và 3 luật dừng trong file `pilot_plan.yaml`, đảm bảo đúng cú pháp 4 vế, ngưỡng an toàn mở lại $\le 6\%$ hoặc chênh $+2$ điểm (dựa trên baseline 4,25%), xóa toàn bộ dấu `?` trong file YAML.
- Rà soát hồ sơ v0, phát hiện và loại bỏ các từ cấm (như từ prod), đảm bảo toàn bộ số liệu giả lập được gắn nhãn `simulated`.

### Bằng chứng

- File `report/team/bang_loi.md`: Bộ nhãn của Người 1, tỷ lệ đồng thuận, quy tắc phân biệt và bảng khắc phục 5 ca.
- File `report/team/pilot_plan.yaml`: Mục D2, các trường `identifiability`, và 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ.
- File `report/team/phieu_cham.md`: Phiếu chấm chéo Gate 2a cho nhóm bạn.

## DangThuyDung-2A202604116

### Phần việc phụ trách

- TV4 · Người gắn nhãn 2, kiêm giữ hồ sơ: gắn nhãn CP3, `chi_so.md`, `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi (đồng thuận 16/20 = 80%), bảng khắc phục 5 ca trong `bang_loi.md`.
- E1 trong `chi_so.md`: ba chỉ số 82,8% · 27,1% · 4,25%, hai chỉ số tự đề xuất, 8 event có `trace_id`.
- Hồ sơ launch v0: mục 4 và đề xuất Go có điều kiện (6 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra).

### Bằng chứng

- Commit `24a3910`, `16e651f`, `f432ae9`; báo cáo cá nhân `report/team/2A202604116_DangThuyDung.md`.
