import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi bấm nút "Click Me"
def show_selected_option():
    selected_value = var.get()  # Lấy giá trị của radio button đã chọn
    messagebox.showinfo("Thông tin đã chọn", f"Bạn đã chọn số: {selected_value}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Thông tin cá nhân và Chọn số")
window.geometry("400x400")

# Phần hiển thị thông tin cá nhân
info_frame = tk.Frame(window)
info_frame.pack(pady=20)

name_label = tk.Label(info_frame, text="Họ và Tên: Pham Viet Quan", font=("Arial", 12))
name_label.grid(row=0, column=0, sticky="w")

dob_label = tk.Label(info_frame, text="Ngày Sinh: 24/10/2005", font=("Arial", 12))
dob_label.grid(row=1, column=0, sticky="w")

mssv_label = tk.Label(info_frame, text="MSSV: 235752021610022", font=("Arial", 12))
mssv_label.grid(row=2, column=0, sticky="w")

major_label = tk.Label(info_frame, text="Ngành Học: Ky Thuat Dieu Khien va TDH", font=("Arial", 12))
major_label.grid(row=3, column=0, sticky="w")

# Phần chọn số với Radio Button
selection_frame = tk.Frame(window)
selection_frame.pack(pady=20)

var = tk.IntVar()

radio1 = tk.Radiobutton(selection_frame, text="1", value=1, variable=var, font=("Arial", 12))
radio1.grid(row=0, column=0, padx=10)

radio2 = tk.Radiobutton(selection_frame, text="2", value=2, variable=var, font=("Arial", 12))
radio2.grid(row=0, column=1, padx=10)

radio3 = tk.Radiobutton(selection_frame, text="3", value=3, variable=var, font=("Arial", 12))
radio3.grid(row=0, column=2, padx=10)

# Nút "Click Me" để hiển thị lựa chọn
click_button = tk.Button(window, text="Click Me", font=("Arial", 14), command=show_selected_option)
click_button.pack(pady=20)

# Chạy vòng lặp chính
window.mainloop()
