so_gio_lam = float(input("Nhập số giời làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giời làm tiêu chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_tinh = gio_tieu_chuan * luong_gio + gio_vuot_chuan*luong_gio*1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_tinh}")