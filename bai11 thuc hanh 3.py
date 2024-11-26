print ("Pham Viet Quan Mssv 235751021610022")
import math
def benefit(t, n, k):
    A = n * (1 + t / 100) ** k
    return A
def main():
    try:
        t_input = input("Nhập lãi suất tiết kiệm hàng tháng (%): ")
        t = float(t_input)
        if t < 0:
            print("Lãi suất phải lớn hơn hoặc bằng 0.")
            return
        n_input = input("Nhập số vốn ban đầu (n): ")
        n = float(n_input)
        if n < 0:
            print("Số vốn ban đầu phải lớn hơn hoặc bằng 0.")
            return
        k_input = input("Nhập số tháng gửi tiết kiệm (k): ")
        if not k_input.isdigit():
            print("Số tháng gửi phải là một số nguyên không âm.")
            return
        k = int(k_input)
        if k < 0:
            print("Số tháng gửi phải lớn hơn hoặc bằng 0.")
            return
        final_amount = benefit(t, n, k)
        print(f"Số tiền nhận được sau {k} tháng là: {final_amount:.2f}")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số thực cho lãi suất và số vốn, và số nguyên cho số tháng gửi.")
if __name__ == "__main__":
    main()
