print("Pham Viet Quan Mssv 235752021610022")
import numpy as np

student_ids = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
heights = np.array([40., 42., 45., 41., 38., 40., 42.0])
sorted_indices = np.lexsort((student_ids, heights))
print("Các chỉ số sắp xếp:")
print(sorted_indices)
sorted_ids = student_ids[sorted_indices]
sorted_heights = heights[sorted_indices]
print("\nDữ liệu sau khi sắp xếp theo chiều cao:")
for i in range(len(sorted_ids)):
    print(f"ID: {sorted_ids[i]}, Chiều cao: {sorted_heights[i]}")
