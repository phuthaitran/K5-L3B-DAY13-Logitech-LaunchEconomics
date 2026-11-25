# Báo cáo cá nhân — TranPhuThai-2A202604001

## 1. Thông tin thành viên

- Họ tên: Trần Phú Thái
- MSSV: 2A202604001
- Email: 26ai.thaitp@vinuni.edu.vn
- Vai trong nhóm: Người viết code (TV1)

## 2. Phần việc phụ trách

- **CP1 · Nhiệm vụ A:** viết `src/lab13.py` phần A1–A4 (ba hàm kinh tế chạy lại, `mo_hinh()`, tách theo loại, chi phí cố định) và điền phần A của `report/team/bang_chi_phi.md`.
- **CP5 · Nhiệm vụ E:** viết phần E1 trong `src/lab13.py` (tính thử ba chỉ số), hoàn thiện `report/team/chi_so.md`, điền mục 4 và dòng đề xuất của `report/team/ho_so_launch_v0.md`, viết `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- **A1:** ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** `mo_hinh()` tính token và tool trên mọi lần chạy kể cả lần lỗi, chia giá token cho 1.000 token, cộng phút xem lại và làm lại (simulated), mẫu số chỉ đếm `ket_qua == 'thanh_cong'`; có sẵn tham số giá, hệ số và `max_lan_chay` để CP2 gọi lại. Kết quả: 4.472 đ mỗi việc thành công [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu (274,7 đ).
- **A3, A4:** bảng theo bốn loại (`quoc_te` 1,88×, chạy lại không giúp: ok lần 1 là 30%, lần 3 là 2,2%); chi phí cố định 1.185 đ/việc ở 45.000 yêu cầu/tháng, 2.370 đ/việc nếu khối lượng còn một nửa [simulated].
- **E1:** code ba chỉ số cho toàn mẫu và phạm vi pilot: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); trong phạm vi `noi_dia` + `hang_nang`: 92,26% · 21,09% · 3,97%.
- **`chi_so.md`:** hai chỉ số tự đề xuất (tỉ lệ nhân viên mở gợi ý; tỉ lệ hoàn sai qua kiểm tra mẫu hằng tuần), 13 event có `trace_id` khớp tên event dùng trong `bang_loi.md`, kiểm tra chéo từng chỉ số với event dùng để tính.
- **Hồ sơ launch v0:** mục 4 và đề xuất **Go có điều kiện**, nêu cả con số bất lợi (xem lại 100% lên 0,98× – 1,03× [simulated]; power 0,64 nếu tác động thật chỉ 5 điểm) và bốn điều kiện có người phụ trách, ngày kiểm tra.

## 4. Bằng chứng

- Commit `627aa5e` "CP1: mo hinh chi phi moi viec thanh cong (A1-A4)": `src/lab13.py`, `report/team/bang_chi_phi.md` (A1–A4).
- Commit CP5 (do tôi commit sau khi viết báo cáo này): phần E1 cuối `src/lab13.py`, `report/team/chi_so.md` (E1 và danh sách event), `report/team/ho_so_launch_v0.md` (mục 4, đề xuất), `report/team/group_report.md`.
- Chạy `cd src && python lab13.py` in đủ bảng A1–A4, B, D1, E1.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus 5.5):** đọc đề và gợi ý phân vai; viết code A1–A4 và E1 trong `lab13.py`; soạn nháp nội dung `chi_so.md`, đề xuất trong hồ sơ, `group_report.md` và báo cáo này.
- **Cách tự kiểm tra:** chạy `python lab13.py` và xác nhận ba phép thử ĐẠT; đối chiếu từng số A2, A3, A4, E1 với số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (đều lệch dưới 2%); kiểm A2 bằng cách tính lại nhẩm 4.373.585 / 978 = 4.472 đ; chạy lệnh `grep` tìm từ cấm theo quy tắc 5 của lab trên `report/team`, không ra kết quả; rà nhãn simulated ở mọi số lấy từ cột `_simulated`. Tôi tự giải thích được vì sao tử số tính mọi lần chạy (lần lỗi vẫn tốn tiền) còn mẫu số chỉ đếm việc thành công (đó là kết quả công ty thực sự nhận).

## 6. Tự đánh giá

- Hoàn thành phần code CP1 đúng mốc, giúp các nhiệm vụ B và D chỉ cần gọi lại `mo_hinh()`.
- Hoàn thiện CP5 dựa trên số của cả nhóm, giữ đề xuất khớp với các con số bất lợi.

