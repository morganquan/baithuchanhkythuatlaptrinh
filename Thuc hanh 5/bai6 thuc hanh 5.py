
print("Pham Viet Quan Mssv 235752021610022")
import mymodule # Import module mymath

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử của danh sách
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))

    lst.append(value)

# Sử dụng module mymodule để sắp xếp danh sách và tìm phần tử lớn nhất, nhỏ nhất
sorted_lst = mymodule.sort_list(lst)
max_value = mymodule.find_max(lst)
min_value = sorted_lst[0]

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất
max_position = lst.index(max_value)
min_position = lst.index(min_value)

# In kết quả
print("Danh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất trong danh sách:", max_value, "tại vị trí:", max_position)
print("Phần tử nhỏ nhất trong danh sách:", min_value, "tại vị trí:", min_position)
