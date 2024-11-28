print("Pham Viet Quan mssv 235752021610022")
def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        num_characters = len(content)
        words = content.split()
        num_words = len(words)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        num_lines = len(lines)
        print(f"Số ký tự: {num_characters}")
        print(f"Số từ: {num_words}")
        print(f"Số dòng: {num_lines}")
    except FileNotFoundError:
        print("File không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_path = 'example.txt'
analyze_file(file_path)
