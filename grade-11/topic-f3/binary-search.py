import numpy as np

# Hàm binary_search() dùng để thực hiện tìm kiếm nhị phân
def binary_search(A, k):
    # Khởi tạo mốc trái và mốc phải
    left = 0
    right = len(A) - 1

    # Trong khi left chưa vượt quá right
    # thì xác định vị trí mid và so sánh A[mid] với k
    while left <= right:
        mid = (left + right) // 2

        if A[mid] == k:
            return mid
        elif A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    # Trả về -1, không tìm thấy
    return -1


# Chương trình chính
if __name__ == '__main__':
    # Khởi tạo mảng Array
    Array = [0, 1, 2, 4, 4, 4, 5, 5, 7, 8, 8, 9]
    
    # Cho người dùng nhập giá trị cần tìm
    key = int(input('Nhập giá trị cần tìm: '))

    # Gọi hàm binary_search()
    found_position = binary_search(Array, key)

    # Nếu kết quả trả về -1 thì thông báo không tìm thấy
    # Ngược lại, thì thông báo vị trí tìm thấy
    if found_position == -1:
        print(f'Không tìm thấy {key}')
    else:
        print(f'Tìm thấy {key} tại vị trí {found_position}')
