import tkinter as tk

# Hàm xử lý sự kiện khi nút được bấm
def on_button_click():
    label.config(text="Bạn đã bấm nút!", fg="green")  # Cập nhật nhãn sau khi bấm nút

# Tạo cửa sổ chính (window form)
window = tk.Tk()
window.title("Cửa sổ đồ họa với Tkinter")
window.geometry("400x200")  # Kích thước cửa sổ (rộng x cao)
window.resizable(False, False)  # Không cho phép thay đổi kích thước

# Thêm một nhãn (label) vào cửa sổ
label = tk.Label(window, text="Chào mừng bạn đến với Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Thêm khoảng cách bên trên và dưới

# Thêm một nút (button) vào cửa sổ
button = tk.Button(
    window,
    text="Bấm vào đây",
    bg="blue",      # Màu nền của nút
    fg="white",     # Màu chữ của nút
    font=("Arial", 12),
    command=on_button_click  # Gắn sự kiện bấm nút
)
button.pack(pady=10)  # Thêm khoảng cách bên trên và dưới

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
