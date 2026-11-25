# Phiếu gắn nhãn CP3 · dùng riêng cho từng người gắn nhãn

**Cách dùng:** mỗi người gắn nhãn tự copy phiếu này, ngồi tách nhau, gắn độc lập cả 20 ca trong 8 phút, không trao đổi. Đừng mở `bang_loi.md` trước khi gắn xong. Gắn xong thì gửi cột "Nhãn" cho người giữ hồ sơ để chép vào `bang_loi.md`. Không sửa nhãn sau khi đã so.

Gắn nhãn theo **nguyên nhân gốc**, không theo chỗ cần sửa.

| Loại | Nghĩa là | Câu hỏi để nhận ra |
| --- | --- | --- |
| Do người dùng | Người dùng nhập sai hoặc chọn sai | Đầu vào của khách có sai không? |
| Hệ thống | Trợ lý làm sai so với thiết kế hoặc chính sách | Có vi phạm thiết kế/chính sách, và có người thấy? |
| Ngữ cảnh | Làm đúng thiết kế nhưng khách thấy sai | Kết quả đúng, chỉ giả định không khớp hoàn cảnh? |
| Giới hạn hệ thống | Không thể trả lời: thiếu dữ liệu, ngoài phạm vi, đầu vào không xử lý được | Có làm được không, dù có cố gắng? |
| Ngầm | Có sai nhưng cả khách lẫn hệ thống đều không nhận ra | Chỉ phát hiện qua kiểm tra mẫu? |

Người gắn nhãn: ...

| Ca | Mô tả | Nhãn |
| --: | --- | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. | Hệ thống|
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. | Hệ thống |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn". | Ngữ cảnh |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. |Giới hạn hệ thống |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. | ngầm |
| 6 | Khách chọn mục "Hoàn phí giao trễ" nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | do người dùng |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công". | hệ thống |
| 8 | Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. |hệ thống |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý gì. | hệ thống |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ". | giới hạn hệ thống |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ". | giới hạn hệ thống |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. | ngầm |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. | Giới hạn hệ thống |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Yêu cầu bị đóng. | Hệ thống |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. | Hệ thống |
| 16 | Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. | Ngữ cảnh |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. | ngầm |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi "Đã hoàn 15.000 đ", không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. | Ngữ cảnh |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. |Giới hạn hệ thống |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. | Hệ thống |

Nguồn: mục "Hai mươi ca lỗi" trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`.
