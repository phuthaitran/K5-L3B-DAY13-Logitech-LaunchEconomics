# Team

## Thông tin nhóm

- Tên nhóm: Logitech
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Logitech-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:
    - URL: https://github.com/phuthaitran/K5-L3B-DAY13-Logitech-LaunchEconomics/commit/754cfb634c501baecd996ed2a8e0ce18d162cf1e

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

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

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

### 4. Bằng chứng

- Commit `627aa5e` "CP1: mo hinh chi phi moi viec thanh cong (A1-A4)": `src/lab13.py`, `report/team/bang_chi_phi.md` (A1–A4).
- Commit CP5 (do tôi commit sau khi viết báo cáo này): phần E1 cuối `src/lab13.py`, `report/team/chi_so.md` (E1 và danh sách event), `report/team/ho_so_launch_v0.md` (mục 4, đề xuất), `report/team/group_report.md`.
- Chạy `cd src && python lab13.py` in đủ bảng A1–A4, B, D1, E1.

## DangThuyDung-2A202604116

### Phần việc phụ trách

- TV4 · Người gắn nhãn 2, kiêm giữ hồ sơ: gắn nhãn CP3, `chi_so.md`, `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi (đồng thuận 16/20 = 80%), bảng khắc phục 5 ca trong `bang_loi.md`.
- E1 trong `chi_so.md`: ba chỉ số 82,8% · 27,1% · 4,25%, hai chỉ số tự đề xuất, 8 event có `trace_id`.
- Hồ sơ launch v0: mục 4 và đề xuất Go có điều kiện (6 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra).

### Bằng chứng

- Commit `24a3910`, `16e651f`, `f432ae9`; báo cáo cá nhân `report/team/2A202604116_DangThuyDung.md`.
