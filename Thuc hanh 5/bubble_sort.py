# bubble_sort.py

def bubbleSort(nlist):
    """
    Hàm sắp xếp nổi bọt.
    Tham số:
        - nlist: danh sách các số cần sắp xếp.
    Trả về:
        - Danh sách đã được sắp xếp theo thứ tự tăng dần.
    """
    n = len(nlist)
    for i in range(n):
        # Vòng lặp bên trong
        for j in range(0, n - i - 1):
            # So sánh và hoán đổi nếu phần tử sau nhỏ hơn phần tử trước
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist
