print("Pham Viet Quan Mssv 235752021610022")
"""Chương trình tạo một máy tính đơn giản có thể cộng, trừ, nhân và
chia bằng cách sử dụng chức năng """
# This function adds two numbers
def add(x, y):
 return x + y
# This function subtracts two numbers
def subtract(x, y):
 return x - y
# This function multiplies two numbers
def multiply(x, y):
 return x * y# This function divides two numbers
def divide(x, y):
 return x / y
print("Chọn thao tác.")
print("1.Cộng")
print("2.Trừ")
print("3.nhân")
print("4.Chia")
# Take input from the user
choice = input("Nhập lựa chọn (1/2/3/4:")
num1 = int(input("Nhập số đầu tiên: "))
num2 = int(input("Nhập số thứ hai: "))
if choice == '1':
 print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
 print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
 print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
 print(num1,"/",num2,"=", divide(num1,num2))
else:
 print("Invalid input")
