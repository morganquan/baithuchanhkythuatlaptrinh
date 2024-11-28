import tkinter as tk
import random

# Các biến toàn cục
time_left = 120  # Thời gian chơi (giây)
score = 0  # Điểm hiện tại
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Brown", "Pink", "White", "Black"]


# Hàm bắt đầu game
def start_game(event=None):
    global time_left, score
    if time_left == 120:  # Chỉ bắt đầu lại khi hết thời gian
        score = 0
        time_left = 120
        score_label.config(text=f"Điểm: {score}")
        time_label.config(text=f"Thời gian: {time_left}s")
        countdown()  # Bắt đầu đếm ngược
        next_color()  # Hiển thị màu mới


# Hàm hiển thị màu mới
def next_color():
    if time_left > 0:
        # Đặt tiêu điểm vào hộp nhập liệu
        color_entry.focus_set()

        # Tạo màu ngẫu nhiên
        random.shuffle(colors)
        color_label.config(fg=colors[1].lower(), text=colors[0])  # Văn bản và màu chữ


# Hàm đếm ngược thời gian
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"Thời gian: {time_left}s")
        window.after(1000, countdown)  # Lặp lại sau 1 giây
    else:
        # Hiển thị thông báo hết giờ
        color_label.config(text="Hết giờ!", fg="black")
        color_entry.config(state=tk.DISABLED)  # Vô hiệu hóa hộp nhập liệu


# Hàm kiểm tra câu trả lời
def check_answer(event=None):
    global score
    if time_left > 0:
        # Nếu nhập đúng màu
        if color_entry.get().strip().lower() == colors[1].lower():
            score += 2  # Thêm 2 điểm
        else:
            score -= 1  # Trừ 1 điểm
        score_label.config(text=f"Điểm: {score}")  # Cập nhật điểm
        color_entry.delete(0, tk.END)  # Xóa nội dung đã nhập
        next_color()  # Hiển thị màu tiếp theo


# Tạo cửa sổ chính
window = tk.Tk()
window.title("Game học màu sắc tiếng Anh")
window.geometry("400x300")

# Tạo nhãn tiêu đề
instructions = tk.Label(window, text="Nhập tên màu hiển thị, không phải màu chữ!", font=("Arial", 12))
instructions.pack(pady=10)

# Tạo nhãn thời gian
time_label = tk.Label(window, text=f"Thời gian: {time_left}s", font=("Arial", 14), fg="red")
time_label.pack()

# Tạo nhãn điểm
score_label = tk.Label(window, text=f"Điểm: {score}", font=("Arial", 14), fg="blue")
score_label.pack()

# Tạo nhãn hiển thị màu
color_label = tk.Label(window, font=("Arial", 40))
color_label.pack(pady=20)

# Tạo hộp nhập liệu
color_entry = tk.Entry(window, font=("Arial", 14))
color_entry.pack()
color_entry.bind("<Return>", check_answer)  # Xử lý sự kiện khi nhấn Enter

# Tạo nút bắt đầu
start_button = tk.Button(window, text="Bắt đầu", font=("Arial", 14), command=start_game)
start_button.pack(pady=10)

# Chạy vòng lặp chính
window.mainloop()
