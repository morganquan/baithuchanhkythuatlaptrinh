print("Pham Viet Quan Mssv 235752021610022")
class ReverseWords:
    def __init__(self):
        self.input_string = input("Nhập một chuỗi: ")

    def reverse_words(self):
        reversed_words = ' '.join(self.input_string.split()[::-1])
        return reversed_words
reverser = ReverseWords()
result = reverser.reverse_words()
print(f"Chuỗi sau khi đảo ngược từ: {result}")
