# Hàm dùng để trộn hai mảng con thành một
def merge_two_arrays(A, left, mid, right):
    # Tính số phần tử của hai mảng con trái và phải
    number_of_left = mid - left + 1
    number_of_right = right - mid

    # Khởi tạo hai mảng con L và R từ mảng A 
    L = A[left : left + number_of_left]
    R = A[mid + 1 : mid + 1 + number_of_right]

    # Khởi tạo các biến chỉ số cho mảng L, R và A
    left_idx = 0
    right_idx = 0
    A_idx = left
    
    # Trong khi cả hai mảng L và R còn phần tử
    while left_idx < number_of_left and right_idx < number_of_right:
        # Nếu phần tử của mảng L nhỏ hơn hoặc bằng phần tử của mảng R
        if L[left_idx] <= R[right_idx]:
            # thì đặt phần tử của mảng L vào mảng A
            A[A_idx] = L[left_idx]

            # Di chuyển chỉ số của mảng L sang vị trí tiếp theo
            left_idx = left_idx + 1
        else:
            # Ngược lại, đặt phần tử của mảng R vào mảng A
            A[A_idx] = R[right_idx]

            # Di chuyển chỉ số của mảng R sang vị trí tiếp theo
            right_idx = right_idx + 1

        # Di chuyển chỉ số của mảng A sang vi trí tiếp theo
        A_idx = A_idx + 1

    # Trong khi mảng L còn phần tử
    while left_idx < number_of_left:
        # Đặt phần tử của mảng L vào mảng A
        A[A_idx] = L[left_idx]

        # Di chuyển chỉ số của mảng L sang vị trí tiếp theo
        left_idx = left_idx + 1

        # Di chuyển chỉ số của mảng A sang vi trí tiếp theo
        A_idx = A_idx + 1
    
    # Trong khi mảng R còn phần tử
    while right_idx < number_of_right:
        # Đặt phần tử của mảng R vào mảng A
        A[A_idx] = R[right_idx]

        # Di chuyển chỉ số của mảng R sang vị trí tiếp theo
        right_idx = right_idx + 1

        # Di chuyển chỉ số của mảng A sang vi trí tiếp theo
        A_idx = A_idx + 1


# Hàm dùng để sắp xếp theo thuật toán trộn
def merge_sort(A, left, right):
    # Thao tác trị
    # Nếu chỉ còn một phần tử thì kết thúc hàm
    if left == right:
        return
    
    # Thao tác chia
    mid = (left + right) // 2

    # Thao tác chia và trị
    merge_sort(A, left, mid)
    merge_sort(A, mid + 1, right)

    # Thao tác kết hợp
    merge_two_arrays(A, left, mid, right)


# Chương trình chính
if __name__ == '__main__':
    # Mảng cần sắp xếp
    array = [1, 7, 4, 0, 9, 4, 8]
    print(f'Mảng gốc chưa có thứ tự: {array}')
    
    # Gọi hàm merge_sort để sắp xếp mảng
    merge_sort(array, 0, len(array) - 1)

    # In mảng sau khi sắp xếp
    print(f'Mảng có thứ tự tăng dần: {array}')