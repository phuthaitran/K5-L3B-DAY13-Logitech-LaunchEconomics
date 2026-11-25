# Báo cáo cá nhân — DangThuyDung-2A202604116

## 1. Thông tin thành viên

- Họ tên: Đặng Thùy Dung
- MSSV: 2A202604116
- Email: (không công khai)
- Vai trong nhóm: TV4 · Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Cài môi trường chạy lab (Python 3.13, `src/.venv`, đủ thư viện trong `requirements.txt`).
- CP3: gắn nhãn độc lập 20 ca lỗi với vai người gắn nhãn 2; chuẩn bị phiếu gắn nhãn và bảng khắc phục 5 ca.
- CP5: viết `report/team/chi_so.md` (E1, danh sách event) và điền `report/team/ho_so_launch_v0.md`, chốt đề xuất.

## 3. Đóng góp cụ thể

- **Gắn nhãn CP3:** gắn độc lập cả 20 ca trong `report/team/phieu_gan_nhan_CP3.md`. Lệch với người gắn nhãn 1 ở 4 ca (1, 9, 10, 14), đồng thuận 16/20 = 80%. Cả 4 ca lệch cùng một kiểu: tôi gắn "Hệ thống" khi khách nhập/bấm sai nhưng trợ lý không chặn, tức là gắn theo chỗ cần sửa thay vì nguyên nhân gốc. Nhóm dùng chính điểm này làm quy tắc phân biệt trong `bang_loi.md`.
- **Bảng khắc phục 5 ca** (ca 14, 20, 16, 11, 5, mỗi loại một ca), mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách.
- **E1 trong `chi_so.md`:** ba chỉ số trong đợt chạy thử là 82,8% (chính, 994/1.200), 27,1% (bỏ qua gợi ý, 48/177), 4,25% (mở lại 7 ngày, 51/1.200); hai chỉ số tự đề xuất; 8 event có `trace_id`; kiểm tra chéo để mọi chỉ số đều tính được từ event.
- **Hồ sơ launch v0:** điền mục 4 và đề xuất **Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang` (3.414 đ/việc thành công = 0,28× nhân viên tự làm [simulated]), sáu điều kiện có người phụ trách và ngày kiểm tra.

## 4. Bằng chứng

- Commit `24a3910`: phiếu gắn nhãn CP3 và bảng khắc phục 5 ca (thông điệp commit ghi nhầm "người 1", đúng ra là người gắn nhãn 2).
- Commit `16e651f`: `chi_so.md` và `ho_so_launch_v0.md`.
- File: `report/team/phieu_gan_nhan_CP3.md`, `report/team/bang_loi.md` (cột "Nhãn người 2" và bảng khắc phục), `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude)**, dùng để: cài môi trường, trích 20 ca lỗi từ file docx thành phiếu gắn nhãn, viết nháp bảng khắc phục, tính ba chỉ số E1 bằng pandas, soạn nháp danh sách event và các điều kiện Go có điều kiện.
- **Nhãn lỗi tôi tự gắn, AI không gắn thay.** Sau khi gắn, tôi nhờ AI so với nhãn tham khảo và đã lỡ sửa ca 1, 9, 10, 14 theo nhận xét; sau đó tôi trả cả bốn ca về nhãn gốc để giữ đúng bộ nhãn độc lập (RULES.md: không sửa bộ nhãn độc lập sau khi đã so).
- **Cách tự kiểm tra:**
  - Ba chỉ số E1: đếm lại theo đúng công thức trong `docs/du_lieu_va_cong_thuc.md`, đọc file bằng `keep_default_na=False`; mẫu số chỉ số dùng là 177 = số yêu cầu có `duoc_xem_lai = 1`.
  - Số trong hồ sơ: đối chiếu với output `python lab13.py` (A2, A3, A4, B1, B4) và `pilot_plan.yaml` (859 yêu cầu/nhóm, 20 cụm, ngày quyết định 2027-01-05).
  - Chạy `grep -rni production report/team`, không in gì.

## 6. Tự đánh giá

- Làm tốt: giữ hồ sơ liền mạch với số của CP1, CP2, CP4; mọi số giả lập có nhãn `simulated`; đề xuất có điều kiện, người phụ trách và ngày kiểm tra.
- Cần cải thiện: khi gắn nhãn, tôi hay gắn theo chỗ cần sửa thay vì nguyên nhân gốc (4/20 ca); lần sau hỏi "đầu vào của khách có sai không?" trước khi gắn. Tôi cũng không nên sửa phiếu độc lập sau khi xem nhận xét.
