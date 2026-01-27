import numpy as np

# Hàm select_sort() dùng để thực hiện sắp xếp chọn
def selection_sort(A):
    # n là số lượng phần tử
    n = len(A)

    # Duyệt từng phần tử A[i] trong phạm vi [0..n - 2]
    for i in range(n - 1):
        # Tìm vị trí phần tử nhỏ nhất của mảng con [i..n - 1]
        min = i
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j

        # Hoán vị A[i] và A[min]
        A[i], A[min] = A[min], A[i]


# Chương trình chính
if __name__ == '__main__':
    # Khởi tạo mảng Array
    Array = np.array([1, 7, 4, 0, 9, 4, 8, 8])

    # In mảng ban đầu
    print(f'Mảng gốc chưa có thứ tự: {Array}')

    # Gọi hàm select_sort()
    selection_sort(Array)

    # In mảng sau khi sắp xếp
    print(f'Mảng có thứ tự tăng dần: {Array}')