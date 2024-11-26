print("Pham Viet Quan Mssv 235752021610022")
def calculate_balance():
    balance = 0    
    print("Nhập nhật ký giao dịch. Nhập 'x' để kết thúc.")    
    while True:
        transaction = input()
        if transaction.lower() == 'x':
            break
        action, amount = transaction.split()
        amount = int(amount)
        if action == 'D':
            balance += amount
        elif action == 'W':
            balance -= amount
        else:
            print("Giao dịch không hợp lệ. Vui lòng nhập lại.")    
    return balance
final_balance = calculate_balance()
print(f"Số tiền thực của tài khoản là: {final_balance}")
