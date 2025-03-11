import numpy as np

# Hàm insertion_sort() dùng để thực hiện sắp xếp chèn
def insertion_sort(A):
    # n là số lượng phần tử
    n = len(A)

    # Duyệt từng phần tử A[i] trong phạm vi [1..n - 1]
    for i in range(1, n):
        # Lưu giá trị A[i] vào biến tạm t
        t = A[i]

        # Duyệt từng phần tử A[j] của mảng con [i - 1..0]
        # Trong khi A[j] vẫn lớn hơn t
        j = i - 1
        while j >= 0 and A[j] > t:
            # Dịch chuyển A[j] về phía sau một vị trí
            A[j + 1] = A[j]

            # Giảm j để tiếp tục xét những A[j] mà lớn hơn t
            j = j - 1

        # Chèn t vào vị trí j + 1
        A[j + 1] = t


# Chương trình chính
if __name__ == '__main__':
    # Khởi tạo mảng Array
    Array = np.array([1, 7, 4, 0, 9, 4, 8, 8])

    # In mảng ban đầu
    print(f'Mảng gốc chưa có thứ tự: {Array}')

    # Gọi hàm insertion_sort()
    insertion_sort(Array)

    # In mảng sau khi sắp xếp
    print(f'Mảng có thứ tự tăng dần: {Array}')