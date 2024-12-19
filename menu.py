import sys

def menu():
        print("\n===== QUẢN LÝ HỌC SINH =====")
        print("1. Quản lý lớp học")
        print("2. Quản lý học sinh")
        print("3. Xử lý điểm")
        print("4. Thoát chương trình")

        choice = float(input("Chọn chức năng (1-4): "))

        if choice == 1:
            menu_quan_ly_lop_hoc()
            return
        elif choice == 2:
            menu_quan_ly_hoc_sinh()
            return
        elif choice == 3:
            menu_xu_ly_diem()
            return
        elif choice == 4:
            print("Kết thúc chương trình!")
            sys.exit()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def menu_quan_ly_lop_hoc():
    print("\n--- Quản lý lớp học ---")
    print("1. Xem lớp học")
    print("2. Thêm lớp học")
    print("3. Xóa lớp học")
    print("4. Chỉnh sửa lớp học")
    print("5. Tìm kiếm lớp học")
    print("6. Quay lại menu chính")
    choice = float(input("Chọn chức năng (1-4): "))
    if choice ==1 :
        xem_lop_hoc()
        return

def menu_quan_ly_hoc_sinh():
    print("\n--- Quản lý học sinh ---")
    print("1. Xem học sinh")
    print("2. Thêm học sinh")
    print("3. Xóa học sinh")
    print("4. Chỉnh sửa học sinh")
    print("5. Tìm kiếm học sinh")
    print("6. Quay lại menu chính")

def menu_xu_ly_diem():
    print("\n--- Xử lý điểm học sinh ---")
    print("1. Xem học sinh kèm điểm")
    print("2. Chỉnh sửa điểm")
    print("3. Xóa điểm")
    print("4. Tìm kiếm điểm")
    print("5. Quay lại menu chính")


 
    
    
def xem_lop_hoc():# nằm trong hàm quản lí lớp học
        with open(file="package_quan_ly_lop_hoc/file_ds_lop_hoc.csv", mode="r") as file:
            file.close()
            
            
            
            
            
menu()