# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Logitech · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] (gấp 16,3× hoá đơn token+tool chia số yêu cầu; 4.599 đ nếu gồm chi phí cố định ở 45k yc/tháng) | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | noi_dia 0,22× (2.696 đ), hang_nang 0,69× (8.221 đ); cả hệ thống 0,49× (5.865 đ) [simulated] | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử là: chính 82,8% (994/1.200), dùng · bỏ qua gợi ý 27,1% (48/177), an toàn · mở lại 7 ngày 4,25% (51/1.200); phạm vi noi_dia + hang_nang: 92,3% và 3,97%; 8 event có trace_id (`chi_so.md`) | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca: Hệ thống 5, Do người dùng 4, Ngữ cảnh 4, Giới hạn 4, Ngầm 3; đồng thuận 80% (16/20); có cơ chế phát hiện & khắc phục đủ 5 loại | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo 20+20 nhân viên, 859 yc/nhóm (m >= 299, DE = 6,96), MDE 6 điểm; có 3 luật dừng chuẩn cú pháp; ngày quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% kéo dài chi phí lên 11.743 đ – 12.414 đ (0,98× – 1,03×); Làm lại tăng gấp đôi chi phí lên 6.787 đ (+51,8%) [simulated] | Giả lập | Giám đốc vận hành |

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang. Lý do: chi phí mỗi việc thành công trong phạm vi là 3.414 đ = 0,28× nhân viên tự làm (4.599 đ = 0,38× nếu gồm chi phí cố định) [simulated]; loại quoc_te (1,88×) đứng ngoài pilot. Điều kiện:

1. **Phạm vi chỉ noi_dia + hang_nang**, quoc_te và doi_tac chuyển nhân viên kèm tóm tắt. Người phụ trách: PM trợ lý hoàn phí · kiểm tra 2026-12-04, trước ngày bắt đầu pilot.
2. **Khoá chống trùng và đối soát sổ cái chạy trước pilot** (ca 7, 20): 0 ca hoàn trùng, 0 tin "đã hoàn" thiếu bản ghi sổ cái trong 3 ngày chạy thử nội bộ. Người phụ trách: Kỹ sư trưởng agent · kiểm tra 2026-12-04.
3. **Tỉ lệ mở lại 7 ngày của nhóm trợ lý ≤ 6%** và không cao hơn nhóm đối chứng quá 2 điểm (đợt chạy thử: 3,97% trong phạm vi). Vượt thì bấm cờ ngắt theo luật dừng an toàn. Người phụ trách: Giám đốc vận hành · kiểm tra hằng tuần, lần đầu 2026-12-14.
4. **Tỉ lệ làm lại ≤ 7% và chi phí mỗi việc thành công ≤ 8.000 đ** [simulated] (yếu tố nhạy nhất: làm lại gấp đôi → +51,8%). Vượt 2 tuần liền thì thu hẹp về riêng noi_dia, tối đa 2 lần chạy. Người phụ trách: PM trợ lý hoàn phí · kiểm tra 2026-12-21.
5. **Xem lại 100% không kéo quá bước rollout 25%**: ở mức đó chi phí lên 11.743 đ = 0,98× [simulated], gần như không còn lợi. Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%. Người phụ trách: Trưởng nhóm CSKH · kiểm tra 2026-12-21.
6. **Đủ mẫu trước ngày quyết định**: 20 nhân viên mỗi nhóm, mỗi người ≥ 299 yêu cầu trong phạm vi; thiếu thì lùi ngày quyết định chứ không đọc kết quả sớm. Người phụ trách: Giám đốc vận hành · quyết định 2027-01-05.
