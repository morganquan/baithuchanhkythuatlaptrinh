print("Pham Viet Quan mssv 235752021610022")
source_file = "output.txt"
destination_file = "copied_output.txt"
try:
    with open(source_file, "r", encoding="utf-8") as src_file:
        content = src_file.read()
    with open(destination_file, "w", encoding="utf-8") as dest_file:
        dest_file.write(content)
    print(f"Nội dung đã được sao chép từ '{source_file}' sang '{destination_file}' thành công.")
except FileNotFoundError:
    print(f"Tệp '{source_file}' không tồn tại. Vui lòng kiểm tra lại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
