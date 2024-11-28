print("Pham Viet Quan Mssv 235752021610022")
class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    def check_balance(self):
        print(f"Số dư hiện tại: {self.balance:.2f} VNĐ")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Nạp thành công {amount:.2f} VNĐ. Số dư mới: {self.balance:.2f} VNĐ")
        else:
            print("Số tiền nạp phải lớn hơn 0.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Số dư không đủ để rút số tiền này.")
        elif amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        else:
            self.balance -= amount
            print(f"Rút thành công {amount:.2f} VNĐ. Số dư còn lại: {self.balance:.2f} VNĐ")
    def run(self):
        while True:
            print("\n--- ATM ---")
            print("1. Kiểm tra số dư")
            print("2. Nạp tiền")
            print("3. Rút tiền")
            print("4. Thoát")
            choice = input("Chọn chức năng (1-4): ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                amount = float(input("Nhập số tiền muốn nạp: "))
                self.deposit(amount)
            elif choice == "3":
                amount = float(input("Nhập số tiền muốn rút: "))
                self.withdraw(amount)
            elif choice == "4":
                print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
atm = ATM(1000000)
atm.run()

