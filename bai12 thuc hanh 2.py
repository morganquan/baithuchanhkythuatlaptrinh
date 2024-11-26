print("Pham Viet Quan mssv 236762021610022")

import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[$#@]', password):
        return False
    return True

def check_passwords(passwords_str):
    passwords = [pwd.strip() for pwd in passwords_str.split(',')]
    valid_passwords = [pwd for pwd in passwords if is_valid_password(pwd)]
    print(','.join(valid_passwords))

if __name__ == "__main__":
    input_passwords = input("Nhập các mật khẩu, phân tách bằng dấu phẩy: ")
    check_passwords(input_passwords)
