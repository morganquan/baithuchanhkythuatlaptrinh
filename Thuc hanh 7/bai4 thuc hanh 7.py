print("Pham Viet Quan mssv 235752021610022")
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("Nội dung của tệp:")
        print(content)
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra đường dẫn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_path = 'example.txt'
read_file(file_path)
