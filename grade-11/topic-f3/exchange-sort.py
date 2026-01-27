import numpy as np

# Hàm exchange_sort() dùng để thực hiện sắp xếp tráo đổi
def exchange_sort(A):
    # n là số lượng phần tử
    n = len(A)

    # Duyệt từng phần tử A[i] trong phạm vi [0..n - 2]
    for i in range(n - 1):
        # Duyệt từng phần tử A[j] của mảng con [i + 1..n - 1]
        for j in range(i + 1, n):
            # So sánh và tráo đổi A[i] và A[j]
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]


# Chương trình chính
if __name__ == '__main__':
    # Khởi tạo mảng Array
    Array = np.array([1, 7, 4, 0, 9, 4, 8, 8])

    # In mảng ban đầu
    print(f'Mảng gốc chưa có thứ tự: {Array}')

    # Gọi hàm exchange_sort()
    exchange_sort(Array)

    # In mảng sau khi sắp xếp
    print(f'Mảng có thứ tự tăng dần: {Array}')