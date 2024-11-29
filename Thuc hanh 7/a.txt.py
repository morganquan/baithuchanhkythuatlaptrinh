# Tạo file trong ổ D
file_path = ("D:/baith7.txt")  # Đường dẫn đến file trong ổ D

with open(file_path, "w") as file:
    file.write("Xin chao\n")
    file.write("tambiet\n")
    file.write("64k2\n")

print(f"File đã được tạo tại: {file_path}")
