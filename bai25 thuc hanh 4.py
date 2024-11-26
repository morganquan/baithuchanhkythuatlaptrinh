print("Pham Viet Quan Mssv 235752021610022")
def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers
input_numbers = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(num) for num in input_numbers.split(',')]
odd_numbers = filter_odd_numbers(numbers)
print("Các số lẻ là:", odd_numbers)
