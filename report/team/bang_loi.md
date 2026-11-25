# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Event `confirm_received` rồi `request_reopened` cùng `trace_id` trong 7 ngày; cảnh báo khi quá 1% số yêu cầu đã đóng/ngày | Hộp xác nhận hiện số tiền và tài khoản nhận, bấm lần hai mới đóng; cho khách hoàn tác trong 24 giờ | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: số lệnh hoàn ghi sổ cái trên cùng `ma_van_don`; ngưỡng 0 ca trùng | Gắn khoá chống trùng (idempotency key = mã vận đơn + loại hoàn) cho mọi lệnh ghi sổ cái; khoá trùng thì trả trạng thái lệnh cũ | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Event `notification_sent` có giờ gửi trong khung 22:00–07:00 và số phản ánh "làm phiền", theo tuần; ngưỡng 0,5% số thông báo | Hoàn tiền vẫn chạy ngay; thông báo ngoài khung 07:00–22:00 được xếp hàng, gửi lúc 07:00 | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `input_unsupported` với `reason = audio`, đếm theo ngày; ngưỡng 2% số yêu cầu | Nói rõ chưa nghe được tin thoại, kèm nút gõ nhanh 3 trường (mã vận đơn, lý do, số tiền) hoặc chuyển nhân viên kèm tóm tắt | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn có mã giảm giá mỗi tuần, so số tiền hoàn với giá sau giảm; ngưỡng 1% đơn lệch | Tool tra giá trả giá sau giảm; ghi `gia_truoc_giam`, `gia_sau_giam` vào trace; đơn có mã giảm giá được xem lại cho tới khi 2 tuần liền đạt ngưỡng | Kế toán trưởng |
