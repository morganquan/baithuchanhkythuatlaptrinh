print("Pham Viet Quan Mssv 235752021610022")
import numpy as np
dtype = [('Tên', 'U50'), ('Chiều cao', 'f4'), ('Lớp', 'U10')]
students = np.array([
    ('Nguyen Van Tung', 1.70, '64K1'),
    ('Tran Thi Hanh', 1.60, '64k3'),
    ('Le Van Quan', 1.75, '64K5'),
    ('Pham Thi Quynh Trang', 1.65, '64K2'),
    ('Hoang Van Phuc', 1.72, '65k1'),
    ('Vu Thi Nhu Yen', 1.58, '64K1')
], dtype=dtype)
print("Danh sách sinh viên ban đầu:")
print(students)
sorted_students = np.sort(students, order=['Lớp', 'Chiều cao'])
print("\nDanh sách sinh viên sau khi sắp xếp:")
print(sorted_students)
