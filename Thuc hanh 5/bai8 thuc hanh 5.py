# main.py
print("Pham Viet Quan Mssv 235752021610022")
import search_module  # Import module search_module

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các phần tử vào danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Sử dụng hàm Sequential_Search từ module search_module
found, index = search_module.Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy tại vị trí {index}.")
else:
    print(f"Phần tử {item} không có trong danh sách.")
