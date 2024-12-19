import sys

# Hàm menu chính
def menu():
    while True:
        print("\n===== QUẢN LÝ HỌC SINH =====")
        print("1. Quản lý lớp học")
        print("2. Quản lý học sinh")
        print("3. Xử lý điểm")
        print("4. Thoát chương trình")

        try:
            choice = int(input("Chọn chức năng (1-4): "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 4.")
            continue

        if choice == 1:
            menu_quan_ly_lop_hoc()
        elif choice == 2:
            menu_quan_ly_hoc_sinh()
        elif choice == 3:
            menu_xu_ly_diem()
        elif choice == 4:
            print("Kết thúc chương trình!")
            sys.exit()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Menu quản lý lớp học
def menu_quan_ly_lop_hoc():
    while True:
        print("\n--- Quản lý lớp học ---")
        print("1. Xem lớp học")
        print("2. Thêm lớp học")
        print("3. Xóa lớp học")
        print("4. Chỉnh sửa lớp học")
        print("5. Tìm kiếm lớp học")
        print("6. Quay lại menu chính")

        try:
            choice = int(input("Chọn chức năng (1-6): "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 6.")
            continue

        if choice == 1:
            xem_lop_hoc()
        elif choice == 2:
            them_lop_hoc()
        elif choice == 3:
            xoa_lop_hoc()
        elif choice == 4:
            chinh_sua_lop_hoc()
        elif choice == 5:
            tim_kiem_lop_hoc()
        elif choice == 6:
            print("Quay lại menu chính.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Menu quản lý học sinh
def menu_quan_ly_hoc_sinh():
    while True:
        print("\n--- Quản lý học sinh ---")
        print("1. Xem học sinh")
        print("2. Thêm học sinh")
        print("3. Xóa học sinh")
        print("4. Chỉnh sửa học sinh")
        print("5. Tìm kiếm học sinh")
        print("6. Quay lại menu chính")

        try:
            choice = int(input("Chọn chức năng (1-6): "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 6.")
            continue

        if choice == 1:
            xem_hoc_sinh()
        elif choice == 2:
            them_hoc_sinh()
        elif choice == 3:
            xoa_hoc_sinh()
        elif choice == 4:
            chinh_sua_hoc_sinh()
        elif choice == 5:
            tim_kiem_hoc_sinh()
        elif choice == 6:
            print("Quay lại menu chính.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Menu xử lý điểm
def menu_xu_ly_diem():
    while True:
        print("\n--- Xử lý điểm học sinh ---")
        print("1. Xem học sinh kèm điểm")
        print("2. Chỉnh sửa điểm")
        print("3. Xóa điểm")
        print("4. Tìm kiếm điểm")
        print("5. Quay lại menu chính")

        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")
            continue

        if choice == 1:
            xem_hoc_sinh_diem()
        elif choice == 2:
            chinh_sua_diem()
        elif choice == 3:
            xoa_diem()
        elif choice == 4:
            tim_kiem_diem()
        elif choice == 5:
            print("Quay lại menu chính.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def xem_lop_hoc():
    print("Xem danh sách lớp học.")

def them_lop_hoc():
    print("Thêm lớp học mới.")

def xoa_lop_hoc():
    print("Xóa lớp học.")

def chinh_sua_lop_hoc():
    print("Chỉnh sửa thông tin lớp học.")

def tim_kiem_lop_hoc():
    print("Tìm kiếm lớp học.")

def xem_hoc_sinh():
    print("Xem danh sách học sinh.")

def them_hoc_sinh():
    print("Thêm học sinh mới.")

def xoa_hoc_sinh():
    print("Xóa học sinh.")

def chinh_sua_hoc_sinh():
    print("Chỉnh sửa thông tin học sinh.")

def tim_kiem_hoc_sinh():
    print("Tìm kiếm học sinh.")

def xem_hoc_sinh_diem():
    print("Xem danh sách học sinh kèm điểm.")

def chinh_sua_diem():
    print("Chỉnh sửa điểm của học sinh.")

def xoa_diem():
    print("Xóa điểm của học sinh.")

def tim_kiem_diem():
    print("Tìm kiếm điểm của học sinh.")

# Chạy chương trình
menu()
