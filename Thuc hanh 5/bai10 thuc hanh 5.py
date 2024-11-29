print("Pham Viet Quan Mssv 235752021610022")
from bubble_sort import bubbleSort

# Nhập danh sách số từ bàn phím
n = int(input("Nhập số lượng phần tử trong danh sách: "))
nlist = []
for _ in range(n):
    num = int(input("Nhập một số: "))
    nlist.append(num)

print(f"Danh sách trước khi sắp xếp: {nlist}")
sorted_list = bubbleSort(nlist)
print(f"Danh sách sau khi sắp xếp: {sorted_list}")
