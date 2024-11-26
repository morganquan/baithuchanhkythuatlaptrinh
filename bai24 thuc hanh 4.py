print("Pham Viet Quan Mssv 235752021610022")
def count_upper_lower(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(f"Số chữ hoa là: {upper_count}")
    print(f"Số chữ thường là: {lower_count}")
input_text = input("Nhập câu: ")
count_upper_lower(input_text)
