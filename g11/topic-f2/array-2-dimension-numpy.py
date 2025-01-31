import numpy as np

if __name__ == '__main__':
    # Khởi tạo mảng hai chiều A gồm 12 phần tử là số nguyên
    A = np.array([[1, 7, 4, 0], [9, 4, 8, 8], [2, 4, 5, 5]])
    print(f'Mảng A:\n{A}')
    
    # Khởi tạo mảng zeros gồm 3 hàng, 4 cột với các phần tử đều mang giá trị 0
    row_number = 3
    col_number = 4
    zeros = np.full((row_number, col_number), 0)
    print(f'Mảng zeros:\n{zeros}')

    # In ra phần tử đầu tiên của mảng A
    print(f'Phần tử đầu tiên của mảng A: {A[0][0]}')

    # In ra phần tử nằm ở hàng 2, cột 3 của mảng A
    print(f'Phần tử nằm ở hàng 2, cột 3 của mảng A: {A[2][3]}')
    
    # In ra số hàng của mảng A
    A_row_number = len(A)
    print(f'Số hàng của mảng A: {A_row_number}')

    # In ra số cột của mảng A
    A_col_number = len(A[0])
    print(f'Số cột của mảng A: {A_col_number}')

    # Duyệt từng hàng của mảng A
    for r in range(A_row_number):
        # Duyệt từng cột của mảng A
        for c in range(A_col_number):
            # In ra giá trị của phần tử tại hàng r, cột c
            print(A[r][c], end=' ')
        
        # Xuống hàng tiếp theo
        print()
