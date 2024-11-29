# script_with_alias.py
print("Pham Viet Quan Mssv 235752021610022")
import mymath as mt  # Sử dụng alias "mt" cho module mymath

# Danh sách giá trị
values = [2, 4, 6, 8, 10]

# Tính bình phương của mỗi phần tử trong danh sách
print('Squares:')
for v in values:
    print(mt.square(v))

# Tính lập phương của mỗi phần tử trong danh sách
print('Cubes:')
for v in values:
    print(mt.cube(v))

# Tính trung bình cộng của các phần tử trong danh sách
print('Average: ' + str(mt.average(values)))
