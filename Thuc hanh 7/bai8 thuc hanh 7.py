print("Pham Viet Quan mssv 235752021610022")
data_list = ["Dòng 1: Xin chào!", "Dòng 2: Đây là ví dụ.", "Dòng 3: Kết thúc."]
file_name = "output.txt"
try:
    with open(file_name, "w", encoding="utf-8") as file:
        for item in data_list:
            file.write(item + "\n")  # Thêm ký tự xuống dòng sau mỗi mục
    print(f"Nội dung đã được ghi vào tệp '{file_name}' thành công.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
