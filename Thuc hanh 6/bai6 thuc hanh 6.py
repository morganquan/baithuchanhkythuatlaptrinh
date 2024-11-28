print("Pham Viet Quan Mssv 235752021610022")
class StringProcessor:
    def __init__(self):
        self.string = ""
    def get_String(self):
        self.string = input("Nhập một chuỗi: ")
    def print_String(self):
        print("Chuỗi in hoa:", self.string.upper())
processor = StringProcessor()
processor.get_String()
processor.print_String()
