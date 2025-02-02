# Input
data = '''
0 1 2 3 4 5
0 1
0 2
1 2
1 3
1 4
2 4
3 4
3 5
4 5
'''


# Hàm khởi tạo ma trận kề
def init_adjacency_matrix(input_data):
    # Chuyển đổi input thành danh sách các dòng riêng lẻ
    lines = input_data.strip().split('\n')

    # Tách rời các số của dòng đầu tiên, lưu vào biến V là danh sách các đỉnh
    V = list(map(int, lines[0].split()))

    # n là số đỉnh
    n = len(V)

    # Khởi tạo ma trận kề A gồm các phần tử 0
    M = [[0] * n for _ in range(n)]

    # Tách hai số của các dòng tiếp theo và gán giá trị 1 vào phần tử tương ứng
    for line in lines[1:]:
        u, v = map(int, line.split())
        M[u][v] = 1
        M[v][u] = 1

    return M


# Hàm khởi tạo danh sách kề
def init_adjacency_list(input_data):
    # Chuyển đổi input thành danh sách các dòng riêng lẻ
    lines = input_data.strip().split('\n')

    # Tách rời các số của dòng đầu tiên, lưu vào biến V là danh sách các đỉnh
    V = list(map(int, lines[0].split()))

    # Khởi tạo danh sách kề L rỗng (dùng kiểu dictionary)
    L = {v: [] for v in V}

    # Duyệt các dòng tiếp theo và nạp phần tử vào các danh sách đỉnh kề
    for line in lines[1:]:
        u, v = map(int, line.split())
        L[u].append(v)
        L[v].append(u)

    return L

# Chương trình chính
if __name__ == '__main__':
    # Đọc dữ liệu input và đưa vào matrix
    matrix = init_adjacency_matrix(data)

    # In ma trận kề
    print('Ma trận kề:')
    for row in matrix:
        print(row)

    # Đọc dữ liệu input và đưa vào adj_list
    adj_list = init_adjacency_list(data)

    # In danh sách kề
    print('Danh sách kề:')
    for u, neighbors in adj_list.items():
        print(f'{u}: {neighbors}')
    