print("Pham Viet Quan Mssv 235752021610022")
import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu của sinh viên (tên, lớp, chiều cao)
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

# In mảng gốc
print("Original array:")
print(students)

# Sắp xếp mảng theo chiều cao
print("Sort by height:")
sorted_students = np.sort(students, order='height')
print(sorted_students)
