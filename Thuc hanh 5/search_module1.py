# search_module.py

def binary_search(lst, value):
    """
    Tìm kiếm nhị phân trong danh sách lst.

    :param lst: Danh sách đã sắp xếp.
    :param value: Phần tử cần tìm.
    :return: True nếu tìm thấy, False nếu không tìm thấy.
    """
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2  # Tính chỉ số phần tử giữa
        if lst[mid] == value:
            return True  # Nếu tìm thấy, trả về True
        elif lst[mid] < value:
            left = mid + 1  # Tiến về bên phải của danh sách
        else:
            right = mid - 1  # Tiến về bên trái của danh sách

    return False  # Nếu không tìm thấy, trả về False
