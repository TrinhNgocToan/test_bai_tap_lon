def lap_danh_sach():
    ds_sinh_vien = []
    n = int(input("Nhap so sinh vien n = "))
    for sinh_vien in range(n):
        print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
        ma_sinh_vien=float(input("Nhap ma sinh vien: "))
        ho_dem= input(" Nhâp họ và tên đệm: ")
        ten = input("Nhap ten sinh vien: ")
        diem_toan = float(input("Nhap diem toan sinh vien: "))
        diem_ly= float(input("Nhap diem ly sinh vien: "))
        diem_hoa= float(input("Nhap diem hoa sinh vien: "))
        diem_trung_binh=(diem_toan+diem_hoa+diem_ly)/3
        thong_tin_sinh_vien = {"ma sinh vien":ma_sinh_vien,"ho dem":ho_dem,"ten": ten, "diem toan":diem_toan, "diem ly":diem_ly,"diem hoa":diem_hoa,"diem trung binh":diem_trung_binh}
        ds_sinh_vien.append(thong_tin_sinh_vien)
    print("Mã sinh viên    Họ đệmn    Tên    Điểm toánn    Điểm hoá    Điểm lý    Điểm trung bình")
    for student in ds_sinh_vien:
        print(f"{student['ma sinh vien']} {student['ho dem']} {student['ten']}     {student['diem toan']:.1f}     {student['diem hoa']:.1f}     {student['diem ly']:.1f}     {student['diem trung binh']:.1f}")