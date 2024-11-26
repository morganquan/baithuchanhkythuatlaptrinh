print("Pham Viet Quan Mssv 235752021610022")
n = int(input("Nhập số nguyên dương n: "))
def tong_uoc_so(x):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    return tong
for x in range(1, n):
    if tong_uoc_so(x) > x:
        print(x)
