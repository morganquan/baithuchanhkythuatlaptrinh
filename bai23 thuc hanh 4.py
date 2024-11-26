print("Pham Viet Quan Mssv 235752021610022")
def count_letters_and_digits(text):
    letter_count = 0
    digit_count = 0
    for char in text:
        if char.isalpha():  
            letter_count += 1
        elif char.isdigit():  
            digit_count += 1
    print(f"Số chữ cái là: {letter_count}")
    print(f"Số chữ số là: {digit_count}")
input_text = input("Nhập câu: ")
count_letters_and_digits(input_text)
