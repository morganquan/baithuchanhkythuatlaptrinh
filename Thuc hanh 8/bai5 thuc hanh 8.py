import tkinter as tk
def on_selection_change():
    label.config(text=f"Bạn đã chọn: {selected_option.get()}")
window = tk.Tk()
window.title("Radio Button với Tkinter")
window.geometry("400x250")
label = tk.Label(window, text="Hãy chọn một tùy chọn bên dưới:", font=("Arial", 14))
label.pack(pady=20)
selected_option = tk.StringVar(value="Không có")
options = ["Tùy chọn 1", "Tùy chọn 2", "Tùy chọn 3"]
for option in options:
    radio = tk.Radiobutton(
        window,
        text=option,
        value=option,
        variable=selected_option,  
        command=on_selection_change,
        font=("Arial", 12),
        indicatoron=0,
        width=15,
        bg="lightblue",
    )
    radio.pack(pady=5)
window.mainloop()
