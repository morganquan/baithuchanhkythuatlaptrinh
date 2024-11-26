print("Pham Viet Quan Mssv 235752021610022")
def is_all_digits_even(number):
    for digit in str(number):
        if int(digit) % 2 != 0: 
            return False
    return True
result = []
for num in range(1000, 3001):
    if is_all_digits_even(num):
        result.append(str(num))
print(",".join(result))
