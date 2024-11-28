print("Pham Viet Quan mssv 235752021610022")
def append_and_display(file_path, text_to_append):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text_to_append + '\n')
        print("Đã ghi thêm văn bản vào tệp.")
        with open(file_path, 'r', encoding='utf-8') as file:
            print("Nội dung hiện tại của tệp:")
            print(file.read())
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra đường dẫn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_path = 'example.txt'
text_to_append = "Đây là văn bản mới được thêm vào."
append_and_display(file_path, text_to_append)
