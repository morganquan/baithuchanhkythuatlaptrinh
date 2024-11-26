print("Pham Viet Quan Mssv 235752021610022")
n = int(input("Nhập số dòng n của Tam giác Pascal: "))
def pascal_triangle(n):
    row = [1]
    for i in range(n):
        print(" ".join(map(str, row)))
        next_row = [1]
        for j in range(1, len(row)):
            next_row.append(row[j-1] + row[j])
        next_row.append(1)
        row = next_row
pascal_triangle(n)
