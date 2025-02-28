if __name__ == '__main__':
    # Khởi tạo danh sách my_list
    my_list = [1, 7, 4, 0, 9, 4, 8, 8]

    # In danh sách my_list ra màn hình
    print(f'Danh sách ban đầu: {my_list}')

    # Thêm phần tử có giá trị 2 vào cuối danh sách
    element = 2
    my_list.append(element)

    # In ra danh sách sau khi thêm
    print(f'Danh sách sau khi thêm: {my_list}')

    # Chèn phần tử có giá trị -1 vào vị trí đầu tiên
    position = 0
    element = -1
    my_list.insert(position, element)

    # In ra danh sách sau khi chèn
    print(f'Danh sách sau khi chèn: {my_list}')

    # Xoá phần tử có giá trị 2
    element = 2
    my_list.remove(element)

    # In ra danh sách sau khi xoá
    print(f'Danh sách sau khi xoá: {my_list}')

    # Xoá phần tử tại vị trí đầu tiên
    position = 0
    my_list.pop(position)

    # In ra danh sách sau khi xoá
    print(f'Danh sách sau khi xoá: {my_list}')

    # Xoá toàn bộ phần tử trong danh sách
    my_list.clear()

    # In ra danh sách sau khi xoá
    print(f'Danh sách sau khi xoá: {my_list}')
