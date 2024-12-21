
def xem_hoc_sinh_diem_kem(ds_hoc_sinh):
    ds_hoc_sinh_diem_kem=[]
    for hoc_sinh_kem in ds_hoc_sinh:
        if hoc_sinh_kem['diem trung binh']<=4:
            ds_hoc_sinh_diem_kem.append(hoc_sinh_kem)
    return ds_hoc_sinh_diem_kem
    
         
        

        