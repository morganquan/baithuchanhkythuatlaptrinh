print("Pham Viet Quan mssv 235752021610022")
def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]

            print(f"Nội dung {n} dòng cuối cùng của tệp:")
            for line in last_n_lines:
                print(line.strip())
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra đường dẫn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_path = 'example.txt'
n = 5
read_last_n_lines(file_path, n)
