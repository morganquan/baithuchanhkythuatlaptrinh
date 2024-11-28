print("Pham Viet Quan mssv 235752021610022")
def read_and_reverse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(content[::-1])
    except FileNotFoundError:
        print("Tệp không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_path = 'Nhom_2_Lop_09'
read_and_reverse_file(file_path)
