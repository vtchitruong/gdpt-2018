# Tạo kiểu dữ liệu node gồm hai thành phần data và next
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Tạo kiểu dữ liệu danh sách liên kết, đặt tên là linked_list
class linked_list:
    def __init__(self):
        self.head = None


# Hàm in ra dữ liệu của các node trong danh sách liên kết
def print_linked_list(l, message):
    print(message)                          # In ra thông báo nào đó

    current =  l.head                       # Cho current trỏ đến head
    while current is not None:              # Trong khi chưa gặp None
        print(current.data , end = ' -> ')  # thì in ra data của current,
                                            # kèm theo mũi tên
        current = current.next              # Cho current trỏ đến node tiếp theo

    print()                                 # Xuống dòng


# Hàm chèn vào trước một node có dữ liệu key
def insert_before(l, key, new_data):
    new_node = node(new_data)    # Tạo node mới

    # Dùng vòng lặp để tìm node có dữ liệu key
    current = l.head             # Cho current trỏ đến head
    while current is not None:
        if current.data == key:  # Nếu tìm thấy key thì ngắt vòng lặp
            break

        previous = current       # Ngược lại, nếu chưa tìm thấy,
                                 # thì cho previous thay thế current
        current = current.next   # và current di chuyển đến node tiếp theo

    new_node.next = current      # Cho next của node mới trỏ đến current
    previous.next = new_node     # Cho next của previous trỏ đến node mới


# Hàm xoá node có dữ liệu key
def remove(self, key):
    current = self.head           # Cho current trỏ đến node đầu tiên

    # Dùng vòng lặp để tìm node có dữ liệu key
    while current is not None:
        if current.data == key:   # Nếu tìm thấy key thì ngắt vòng lặp
            break

        previous = current        # Ngược lại, nếu chưa tìm thấy,
                                  # thì cho previous thay thế current
        current = current.next    # và current di chuyển đến node tiếp theo


    previous.next = current.next  # Ngắt liên kết đến current bằng cách
                                  # cho next của previous trỏ đến
                                  # node liền sau current
    del current                   # xoá current


# Chương trình chính
if __name__ == '__main__':
    L = linked_list()  # Khai báo biến danh sách liên kết L

    # Khởi tạo 3 node đơn lẻ
    first = node('o')
    second = node('l')
    third = node('d')

    # Liên kết các node với nhau
    L.head = first       # Cho head của L trỏ đến first
    first.next = second  # Cho first trỏ đến second
    second.next = third  # Cho second trỏ đến third

    # Gọi hàm print_linked_list để in ra danh sách liên kết
    print_linked_list(L, 'Danh sách liên kết ban đầu:')

    # Gọi hàm insert_before để chèn thêm node mới có dữ liệu 'y'
    # vào trước node có dữ liệu 'd'
    insert_before(L, 'd', 'y')

    # Gọi hàm print_linked_list để in ra danh sách liên kết
    print_linked_list(L, 'Danh sách liên kết sau khi chèn thêm:')

    # Gọi hàm remove để xoá node có dữ liệu 'y'
    remove(L, 'y')

    # Gọi hàm print_linked_list để in ra danh sách liên kết
    print_linked_list(L, 'Danh sách liên kết sau khi xoá node:')