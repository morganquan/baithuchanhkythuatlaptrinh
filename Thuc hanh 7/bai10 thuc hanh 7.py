print("Pham Viet Quan mssv 235752021610022")
def find_longest_words(text):
    words = text.split()
    cleaned_words = [word.strip(".,!?;:()[]{}\"'") for word in words]
    max_length = max(len(word) for word in cleaned_words)
    longest_words = [word for word in cleaned_words if len(word) == max_length]
    return longest_words
text = """
Python is a great programming language that helps in solving many complex problems
with easy and efficient solutions. It is widely used in various fields like data science,
artificial intelligence, machine learning, and web development.
"""
longest_words = find_longest_words(text)
print("Những từ dài nhất trong văn bản là:", longest_words)
