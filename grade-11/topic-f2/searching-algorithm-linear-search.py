import numpy as np

# Hàm linear_search() dùng để thực hiện tìm kiếm tuần tự
def linear_search(A, k):
    # n là số lượng phần tử
    n = len(A)

    # Duyệt từng phần tử từ đầu đến cuối mảng
    # Nếu A[i] nào đó bằng k thì trả về vị trí i
    for i in range(n):
        if A[i] == k:
            return i

    # Trả về -1, không tìm thấy
    return -1


# Chương trình chính
if __name__ == '__main__':
    # Khởi tạo mảng Array
    Array = np.array([1, 7, 4, 0, 9, 4, 8, 8, 2, 4, 5, 5])
    
    # Cho người dùng nhập giá trị cần tìm
    key = int(input('Nhập giá trị cần tìm: '))

    # Gọi hàm linear_search()
    found_position = linear_search(Array, key)

    # Nếu kết quả trả về -1 thì thông báo không tìm thấy
    # Ngược lại, thì thông báo vị trí tìm thấy 
    if found_position == -1:
        print(f'Không tìm thấy {key}')
    else:
        print(f'Tìm thấy {key} tại vị trí {found_position}')
