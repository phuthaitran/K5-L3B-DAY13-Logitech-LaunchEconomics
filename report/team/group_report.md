# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Logitech
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có cho chạy pilot hay không, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Cách tiếp cận: mọi con số tính bằng `src/lab13.py` trên mẫu 1.200 yêu cầu (1.624 lần chạy), có người thứ hai tính tay để đối chiếu; nhiệm vụ sau dùng lại số của nhiệm vụ trước; số từ cột `_simulated` luôn ghi nhãn simulated. Nhóm chia bốn vai (viết code, kiểm số, gắn nhãn 1, gắn nhãn 2 kiêm giữ hồ sơ) và đổi người viết code sau giờ giải lao.

## 3. Giải pháp

- **A · Mô hình chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): ba hàm A1 qua ba phép thử (1,20 · 1,25 · 1,25); `mo_hinh()` cộng token và tool của mọi lần chạy kể cả lần lỗi, cộng phút xem lại và làm lại, chia cho số việc thành công; tách theo loại (A3) và cộng chi phí cố định 40 triệu/tháng (A4).
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh()` cho 9 kịch bản, một cặp, giới hạn 1/2/3 lần chạy tính cả phần nhân viên làm thay, và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo năm loại Google PAIR, so nhãn, viết quy tắc cho ca lệch, bảng khắc phục 5 ca đủ năm loại.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính năm câu D1 trước, rồi mới chọn chia theo nhân viên 20 + 20; năm câu D2; ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ đặt sau khi tính tỉ lệ mở lại hiện tại.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): tính thử ba chỉ số, đề xuất thêm hai chỉ số, 13 event có `trace_id` kèm kiểm tra chéo chỉ số ↔ event, ba dòng rủi ro kinh tế lấy từ bảng độ nhạy, hồ sơ bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token và tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5% tổng chi phí. Tính cả 222 ca nhân viên làm thay: 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- Theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` 1,88× [simulated]; chạy lại không cứu `quoc_te` (ok lần 1 là 30%, lần 3 là 2,2%).
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ cả hệ thống [simulated]). Xem lại 100% đẩy chi phí lên 0,98× – 1,03× [simulated].
- Bảng lỗi: đồng thuận 16/20 = 80%, đủ năm loại có cách phát hiện đo được.
- Pilot: chia theo nhân viên 20 + 20, mức chênh 6 điểm, 859 yêu cầu/nhóm, m ≥ 299, DE 6,96; power còn 0,64 nếu tác động thật chỉ 5 điểm.
- Chỉ số trong đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25%.
- **Đề xuất cuối: Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang`, kèm bốn điều kiện có người phụ trách và ngày kiểm tra (xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: ... (điền sau buổi duyệt chéo: điểm C6, C7, C8, quyết định và câu hỏi của hội đồng)

## 5. Khó khăn và cách xử lý

- **Lỗi in tiếng Việt trên Windows:** khi chuyển output qua pipe trong Git Bash, `print` báo `UnicodeEncodeError: 'charmap' codec can't encode character`. Xử lý: chạy với `PYTHONIOENCODING=utf-8`; code không phải sửa.
- **Đồng thuận gắn nhãn vừa chạm ngưỡng 80%:** bốn ca lệch: ba ca (1, 9, 14) lẫn "Do người dùng" với "Hệ thống" vì gắn theo chỗ cần sửa thay vì nguyên nhân gốc; ca 10 lẫn "Ngữ cảnh" với "Giới hạn hệ thống". Xử lý: thống nhất nhãn và ghi một câu quy tắc phân biệt cho từng ca trong `bang_loi.md`.
- **Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm với 40 nhân viên:** nhóm chấp nhận mức chênh 6 điểm và ghi rõ power 0,64 trong hồ sơ thay vì chọn chia theo depot.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; mọi kết luận chi phí phải tính lại bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên ba chỉ số chỉ là mức hiện tại, chưa nói được trợ lý tạo ra khác biệt.
- Pilot chỉ đủ mẫu cho mức chênh 6 điểm; nếu tác động thật nhỏ hơn, cần kéo dài pilot để mỗi nhân viên đạt nhiều yêu cầu hơn, hoặc mở rộng số nhân viên.
- Phút làm lại trung bình trong dữ liệu là 15,3 phút/ca, cao hơn mức 9 phút của đề; nếu đúng, xem lại 100% đắt hơn nhân viên tự làm (1,03×).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `statsmodels.stats.power.NormalIndPower`.
- Tài liệu lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
