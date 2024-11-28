# main.py
print("Pham Viet Quan Mssv 235752021610022")
import search_module1  # Import module search_module

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các phần tử vào danh sách
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    lst.append(value)

# Sắp xếp danh sách (yêu cầu danh sách phải đã được sắp xếp cho tìm kiếm nhị phân)
lst.sort()

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Sử dụng hàm binary_search từ module search_module
found = search_module1.binary_search(lst, value)

# In kết quả
if found:
    print(f"Phần tử {value} có trong danh sách.")
else:
    print(f"Phần tử {value} không có trong danh sách.")
