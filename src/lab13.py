"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    # = (1 - (1-p)^k) / p; khi k → ∞ còn 1/p.
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # Thất bại chỉ khi cả k lần đều sai.
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tử số: mọi lần chạy (kể cả lần sai); mẫu số: chỉ yêu cầu thành công.
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ lần chạy thuộc các yêu cầu đang xét (để A3, B4 gọi lại với reqs đã lọc).
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi. Giá token tính cho 1.000 token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai

    # Mẫu số: chỉ yêu cầu thành công.
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
YEU_CAU_THANG = 1500 * 30      # 45.000 yêu cầu / tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ---------- A2 ----------
    print('\n== A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated) ==')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    print(f"cps / hoá đơn mỗi yêu cầu = {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong']:6.1%}")
    khong_tc = int((reqs['ket_qua'] != 'thanh_cong').sum())
    ca_he_thong = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca không thành công × 12.000 đ): '
          f'{ca_he_thong:,.0f} đ = {ca_he_thong / BASELINE:.2f}× [simulated]')

    # ---------- A3 ----------
    print('\n== A3 · Theo loại yêu cầu (cps: simulated) ==')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'chay/yc':>8s} {'cps':>9s} {'so_12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r):9.1%} {so_chay / len(r):8.2f} "
              f"{kq['cps']:9,.0f} {kq['cps'] / BASELINE:6.2f}×")
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử, theo loại.
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: d['status'] == 'ok')
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('\nTỉ lệ ok theo lần thử:')
    print(ok_theo_lan.map(lambda x: f'{x:.1%}'))

    # ---------- A4 ----------
    print('\n== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang (simulated) ==')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    kq_pv = mo_hinh(runs, pv)
    print(f"Phạm vi: {len(pv)} yêu cầu, {kq_pv['thanh_cong']} thành công, cps = {kq_pv['cps']:,.0f} đ")
    for nhan, he_so in [('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YEU_CAU_THANG * he_so * kq_pv['thanh_cong'] / len(reqs)
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        tong_viec = kq_pv['cps'] + co_dinh
        print(f'{nhan:22s} tc/tháng={tc_thang:9,.0f}  cố định/việc={co_dinh:6,.0f} đ  '
              f'cps+cố định={tong_viec:6,.0f} đ = {tong_viec / BASELINE:.2f}×')

    # ---------- B1 · Độ nhạy từng yếu tố ----------
    print('\n== B1 · Độ nhạy từng yếu tố (cps: simulated) ==')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    ket_qua_b1 = {}
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        thay_doi = (cps / goc - 1) * 100
        ket_qua_b1[ten] = {'cps': cps, 'thay_doi': thay_doi}
        print(f'{ten:32s} cps={cps:10,.0f} đ  thay đổi={thay_doi:+6.1f}% [simulated]')

    # ---------- B2 · Tác động một cặp và xếp hạng ----------
    print('\n== B2 · Cặp token + xem lại và xếp hạng yếu tố ==')
    cap = mo_hinh(
        runs, reqs,
        gia_vao=52,
        gia_ra=260,
        he_so_xem_lai=2.0,
    )
    thay_doi_cap = (cap['cps'] / goc - 1) * 100
    print(f"Token gấp đôi + xem lại gấp đôi: cps={cap['cps']:,.0f} đ "
          f"thay đổi={thay_doi_cap:+.1f}% [simulated]")
    tac_dong = {
        'Số ca làm lại': abs(ket_qua_b1['Số ca làm lại gấp đôi']['thay_doi']),
        'Tỉ lệ xem lại': abs(ket_qua_b1['Tỉ lệ xem lại gấp đôi']['thay_doi']),
        'Lương nhân viên': abs(ket_qua_b1['Lương nhân viên tăng 25%']['thay_doi']),
    }
    for hang, (ten, muc) in enumerate(sorted(tac_dong.items(), key=lambda p: p[1], reverse=True), 1):
        print(f'Xếp hạng {hang}: {ten} ({muc:.1f}% khi gấp đôi) [simulated]')

    # ---------- B3 · Giới hạn số lần chạy ----------
    print('\n== B3 · Giới hạn 1, 2, 3 lần (cps và cả hệ thống: simulated) ==')
    ket_qua_b3 = {}
    for gioi_han in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        chi_phi_he_thong = kq['tong'] + khong_thanh_cong * BASELINE
        ket_qua_b3[gioi_han] = {
            'tong': kq['tong'],
            'khong_thanh_cong': khong_thanh_cong,
            'chi_phi_he_thong': chi_phi_he_thong,
            'cps': kq['cps'],
        }
        print(f"Gioi hạn {gioi_han}: tổng trợ lý={kq['tong']:,.0f} đ "
              f"không thành công={khong_thanh_cong} "
              f"cả hệ thống={chi_phi_he_thong:,.0f} đ "
              f"cps={kq['cps']:,.0f} đ [simulated]")
    re_nhat_cong_ty = min(ket_qua_b3, key=lambda k: ket_qua_b3[k]['chi_phi_he_thong'])
    re_nhat_cps = min(ket_qua_b3, key=lambda k: ket_qua_b3[k]['cps'])
    print(f'Rẻ nhất cho công ty: giới hạn {re_nhat_cong_ty} lần')
    print(f'Rẻ nhất theo cps: giới hạn {re_nhat_cps} lần')

    # ---------- B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang ----------
    print('\n== B4 · Xem lại 100% noi_dia + hang_nang (simulated) ==')
    pv = reqs[reqs['loai'].isin(PHAM_VI)].copy()
    pv_runs = runs[runs['request_id'].isin(pv['request_id'])]
    co_lan_ok = set(pv_runs.loc[pv_runs['status'] == 'ok', 'request_id'])
    pv['phut_xem_lai_simulated'] = pv['request_id'].map(
        lambda request_id: 5 if request_id in co_lan_ok else 0
    )
    pv['phut_lam_lai_simulated'] = pv['ket_qua'].map(
        lambda ket_qua: 9 if ket_qua == 'lam_lai' else 0
    )
    kq_b4 = mo_hinh(runs, pv)
    print(f"Phạm vi: {len(pv)} yêu cầu, {len(co_lan_ok)} yêu cầu có ít nhất một lần ok, "
          f"{kq_b4['thanh_cong']} thành công")
    print(f"CPS xem lại 100%: {kq_b4['cps']:,.0f} đ "
          f"= {kq_b4['cps'] / BASELINE:.2f}× nhân viên tự làm [simulated]")
    so_ca_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    tien_token_tool_b4 = kq_b4['token'] + kq_b4['tool']
    tong_b4_15_phut = tien_token_tool_b4 + len(co_lan_ok) * 5 * LUONG_PHUT + so_ca_lam_lai * 15.3 * LUONG_PHUT
    cps_b4_15_phut = tong_b4_15_phut / kq_b4['thanh_cong']
    print(f"Độ nhạy phút làm lại = 15,3 phút/ca: "
          f"cps={cps_b4_15_phut:,.0f} đ "
          f"= {cps_b4_15_phut / BASELINE:.2f}× nhân viên tự làm [simulated]")

    # ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
    print('\n== D1 · Cỡ mẫu (baseline=0.70, mde=0.05, alpha=0.05, power=0.8, ICC=0.02) ==')
    from statistics import NormalDist

    def tinh_co_mau(p1, p2, alpha=0.05, power=0.8):
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    n_yc = tinh_co_mau(0.70, 0.75)
    print(f"a) Chia theo yêu cầu: {n_yc} yêu cầu mỗi nhóm")

    de_nv_75 = 1 + (75 - 1) * 0.02
    n_nv_75 = math.ceil(n_yc * de_nv_75)
    nv_moi_nhom_75 = math.ceil(n_nv_75 / 75)
    print(f"b) Theo nhân viên m=75: DE={de_nv_75:.2f}, n={n_nv_75} mỗi nhóm -> {nv_moi_nhom_75} nhân viên/nhóm (tổng {nv_moi_nhom_75*2} > 40: KHÔNG ĐỦ NGƯỜI)")

    tran_20_nv = 20 / 0.02
    print(f"c) 20 nhân viên mỗi nhóm: trần cỡ mẫu hiệu dụng c/ICC = {tran_20_nv:.0f} < {n_yc} (KHÔNG ĐẠT mức chênh 5 điểm)")

    tran_6_depot = 6 / 0.02
    print(f"d) 6 depot mỗi nhóm: trần cỡ mẫu hiệu dụng c/ICC = {tran_6_depot:.0f} < {n_yc} (KHÔNG ĐẠT)")

    n_yc_6pt = tinh_co_mau(0.70, 0.76)
    m_can = math.ceil((0.98 * n_yc_6pt) / (20 - 0.02 * n_yc_6pt))
    de_6pt = 1 + (m_can - 1) * 0.02
    print(f"e) Mức chênh 6 điểm: {n_yc_6pt} mỗi nhóm -> cần m >= {m_can} yêu cầu/nhân viên (DE={de_6pt:.2f})")

    tl_mo_lai = reqs['mo_lai_trong_7_ngay'].mean()
    tl_mo_lai_pv = pv['mo_lai_trong_7_ngay'].mean()
    print(f"Tỉ lệ mo_lai_trong_7_ngay: toàn bộ={tl_mo_lai:.2%}, phạm vi noi_dia+hang_nang={tl_mo_lai_pv:.2%}")
