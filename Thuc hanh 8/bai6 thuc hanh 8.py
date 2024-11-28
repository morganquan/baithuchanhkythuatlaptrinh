import tkinter as tk
from tkinter import messagebox  # Dùng để hiển thị thông báo
def menu_action(action):
    messagebox.showinfo("Thông báo", f"Bạn đã chọn: {action}")
window = tk.Tk()
window.title("Menu với Tkinter")
window.geometry("400x300")
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 để ẩn đường kẻ đầu tiên
file_menu.add_command(label="Mở tệp", command=lambda: menu_action("Mở tệp"))
file_menu.add_command(label="Lưu tệp", command=lambda: menu_action("Lưu tệp"))
file_menu.add_separator()  # Đường kẻ phân cách
file_menu.add_command(label="Thoát", command=window.quit)
menu_bar.add_cascade(label="Tệp", menu=file_menu)
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Sao chép", command=lambda: menu_action("Sao chép"))
edit_menu.add_command(label="Dán", command=lambda: menu_action("Dán"))
edit_menu.add_command(label="Xóa", command=lambda: menu_action("Xóa"))
menu_bar.add_cascade(label="Chỉnh sửa", menu=edit_menu)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Hướng dẫn", command=lambda: menu_action("Hướng dẫn"))
help_menu.add_command(label="Giới thiệu", command=lambda: menu_action("Giới thiệu"))
menu_bar.add_cascade(label="Trợ giúp", menu=help_menu)
window.config(menu=menu_bar)
window.mainloop()
