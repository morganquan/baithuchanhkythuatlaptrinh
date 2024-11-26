print("Pham Viet Quan Mssv 235752021610022")
input_str = input("Nhập chuỗi: ")
new_str = ''.join([char for char in input_str if not char.isdigit()])
print("Chuỗi sau khi loại bỏ các chữ số:", new_str)
