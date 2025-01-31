import numpy as np

if __name__ == '__main__':
    # Khởi tạo mảng một chiều A gồm 12 phần tử là số nguyên
    A = np.array([1, 7, 4, 0, 9, 4, 8, 8, 2, 4, 5, 5])
    print(f'Mảng A: {A}')

    # Khởi tạo mảng zeros gồm 8 phần tử đều mang giá trị 0
    zeros = np.full(8, 0)
    print(f'Mảng zeros: {zeros}')

    # In ra phần tử đầu tiên của mảng A
    print(f'Phần tử đầu tiên của mảng A: {A[0]}')

    # In ra phần tử cuối cùng của mảng A
    print(f'Phần tử cuối cùng của mảng A: {A[len(A) - 1]}')

    # Chương trình báo lỗi vì không có chỉ số 12 trong mảng A
    # print(f'Phần tử thứ 12 của mảng A: {A[12]}')

    # In các phần tử của mảng A trên từng dòng
    for i in range(len(A)):
        print(f'A[{i}] = {A[i]}')

    # In mảng A theo thứ tự từ cuối ngược về đầu
    for i in range(len(A) - 1, -1, -1):
        print(A[i], end=' ')
