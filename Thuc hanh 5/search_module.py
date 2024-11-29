# search_module.py

def Sequential_Search(dlist, item):
    """
    Tìm kiếm tuyến tính trong danh sách dlist.

    :param dlist: Danh sách các phần tử.
    :param item: Phần tử cần tìm.
    :return: Tuple (True, index) nếu tìm thấy, (False, -1) nếu không tìm thấy.
    """
    for index, value in enumerate(dlist):
        if value == item:
            return True, index  # Trả về True và vị trí của item
    return False, -1  # Nếu không tìm thấy, trả về False và -1
