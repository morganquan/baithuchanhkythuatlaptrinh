print("Pham Viet Quan Mssv 235752021610022")
chuoi = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
ds_nhi_phan = chuoi.split(',')
so_chia_het_5 = []
for bin_num in ds_nhi_phan:
    if int(bin_num, 2) % 5 == 0:
        so_chia_het_5.append(bin_num)
print(",".join(so_chia_het_5))
