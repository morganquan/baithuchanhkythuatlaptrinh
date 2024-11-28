# script.py

import mymath  # Import module mymath

# Danh sách giá trị
values = [2, 4, 6, 8, 10]

# Tính bình phương của mỗi phần tử trong danh sách
print('Squares:')
for v in values:
    print(mymath.square(v))

# Tính lập phương của mỗi phần tử trong danh sách
print('Cubes:')
for v in values:
    print(mymath.cube(v))

# Tính trung bình cộng của các phần tử trong danh sách
print('Average: ' + str(mymath.average(values)))
