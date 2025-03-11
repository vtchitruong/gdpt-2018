import numpy as np

# Hàm bubble_sort() dùng để thực hiện sắp nổi bọt
def bubble_sort(A):
    # n là số lượng phần tử
    n = len(A)

    # Cho i chạy trong phạm vi [0..n - 2]
    for i in range(n - 1):
        # Duyệt từng phần tử A[j] của mảng con [0..n - 1 - i]
        for j in range(n - 1 - i):
            # So sánh và hoán vị hai phần tử cạnh nhau
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


# Chương trình chính
if __name__ == '__main__':
    # Khởi tạo mảng Array
    Array = np.array([1, 7, 4, 0, 9, 4, 8, 8])

    # In mảng ban đầu
    print(f'Mảng gốc chưa có thứ tự: {Array}')

    # Gọi hàm bubble_sort()
    bubble_sort(Array)

    # In mảng sau khi sắp xếp
    print(f'Mảng có thứ tự tăng dần: {Array}')