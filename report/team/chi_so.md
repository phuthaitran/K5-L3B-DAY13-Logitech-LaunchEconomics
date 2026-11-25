# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994 / 1.200 = **82,8%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | (41 `sua` + 7 `bo`) / 177 = **27,1%** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51 / 1.200 = **4,25%** |
| Dùng | Nhóm tự đề xuất: tỉ lệ nhân viên gửi gợi ý của trợ lý trong 2 phút | Số `staff_review_decision` có `decision = giu` và thời gian từ `agent_suggestion_shown` < 2 phút, chia số `agent_suggestion_shown` | Không cần tính |
| An toàn | Nhóm tự đề xuất: tỉ lệ hoàn sai số tiền qua kiểm tra mẫu (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `lech_tien = 1`, chia tổng số đơn được kiểm tra mẫu (100 đơn/tuần) | Không cần tính |

Chỉ số trong đợt chạy thử là 82,8% (chính), 27,1% (dùng), 4,25% (an toàn); riêng phạm vi `noi_dia` + `hang_nang` (982 yêu cầu) là 92,3% và 3,97%. Đợt chạy thử không có nhóm đối chứng nên chưa nói được trợ lý làm thay đổi các chỉ số này. Cách tính: `pd.read_csv('logix_requests.csv', keep_default_na=False)`, đếm theo công thức ở cột 3; không dùng cột `_simulated`.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_created` | Hệ thống tiếp nhận | request_id, loai, depot, staff_id, so_tien_vnd, nhom_pilot (tro_ly/doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok/loi), trace_id | Cuối mỗi lần chạy |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, trace_id | Khi nhân viên mở gợi ý |
| `staff_review_decision` | Nhân viên CSKH | request_id, staff_id, decision (giu/sua/bo), phut_xem_lai, trace_id | Khi nhân viên chốt xem lại |
| `refund_ledger_written` | API sổ cái | request_id, so_tien_hoan, idempotency_key, status, trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `request_closed` | Hệ thống tiếp nhận | request_id, closed_by (tro_ly/nhan_vien/khach), gio_tu_luc_tao, trace_id | Khi yêu cầu đóng |
| `request_reopened` | Khách / nhân viên | request_id, ly_do, so_ngay_tu_luc_dong, trace_id | Khi yêu cầu mở lại |
| `audit_sample_checked` | Kế toán | request_id, so_tien_dung, so_tien_da_hoan, lech_tien (0/1), trace_id | Kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `request_closed` (gio_tu_luc_tao ≤ 24) và không có `request_reopened` (so_ngay_tu_luc_dong ≤ 7), chia số `request_created`. Đo được.
- **Dùng · bỏ qua gợi ý:** `staff_review_decision` có decision = sua hoặc bo, chia tổng số `staff_review_decision`. Đo được.
- **An toàn · lỗi lọt đến khách:** số `request_reopened` trong 7 ngày, chia số `request_created`. Đo được.
- **Dùng · gửi gợi ý trong 2 phút:** hiệu thời điểm `staff_review_decision` − `agent_suggestion_shown` cùng trace_id. Đo được.
- **An toàn · hoàn sai qua kiểm tra mẫu:** `audit_sample_checked` có lech_tien = 1, chia số đơn kiểm tra. Đo được.
- Event `refund_ledger_written` không vào chỉ số nào ở trên nhưng cần cho luật dừng "≥ 1 ca hoàn trùng" trong `pilot_plan.yaml` (đếm idempotency_key trùng) và ca 7, 20 trong `bang_loi.md`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp phạm vi về riêng `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.414 đ = 1,03× nếu thời gian làm lại thực tế 15,3 phút/ca) [simulated] | Tỉ lệ yêu cầu được xem lại vẫn > 50% ở cuối bước rollout 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở quy mô 45.000 yc/tháng, +2.370 đ/việc nếu khối lượng giảm một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch pilot | Không mở rộng pilot, xem lại điều khoản chi phí cố định | Giám đốc vận hành |
