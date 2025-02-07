# Hàm dùng để phân hoạch mảng A từ vị trí left đến vị trí right
def partition(A, left, right):
    # Chọn phần tử trục là phần tử cuối mảng con
    pivot = A[right]
    
    # Khởi tạo i để theo dõi phần tử cuối cùng nhỏ hơn hoặc bằng pivot
    i = left - 1
    
    # Duyệt qua các phần tử trong phạm vi [left..right - 1]
    for j in range(left, right):
        # Nếu phần tử A[j] nhỏ hơn hoặc bằng pivot
        if A[j] <= pivot:
            # Tăng i trước khi hoán vị để đảm bảo vùng nhỏ hơn pivot được mở rộng
            i = i + 1

            # Hoán vị A[i] và A[j]
            A[i], A[j] = A[j], A[i]

    # Hoán vị pivot, tức A[right], với phần tử ở vị trí i + 1
    A[i + 1], A[right] = A[right], A[i + 1]
    
    # Trả về chỉ số mới của pivot
    return i + 1


# Hàm dùng để sắp xếp theo thuật toán sắp xếp nhanh
def quick_sort(A, left, right):
    # Thác tác trị
    # Nếu chỉ còn một phần tử hoặc không còn phần tử nào thì kết thúc hàm
    if left >= right:
        return
    
    # Thao tác chia
    # Phân hoạch mảng A từ vị trí left đến vị trí right
    pivot_idx = partition(A, left, right)
    
    # Thao tác chia và trị
    quick_sort(A, left, pivot_idx - 1)
    quick_sort(A, pivot_idx + 1, right)


# Chương trình chính
if __name__ == '__main__':
    # Mảng cần sắp xếp
    array = [1, 7, 4, 0, 9, 4, 8]
    print(f'Mảng gốc chưa có thứ tự: {array}')

    # Gọi hàm quick_sort để sắp xếp mảng
    quick_sort(array, 0, len(array) - 1)

    # In mảng sau khi sắp xếp
    print(f'Mảng có thứ tự tăng dần: {array}')