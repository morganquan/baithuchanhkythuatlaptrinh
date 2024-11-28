print("Pham Viet Quan Mssv 235752021610022")
class Hinhchunhat:
    def __init__(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
hinh_chunhat = Hinhchunhat()
print("Diện tích hình chữ nhật là:", hinh_chunhat.tinh_dien_tich())
