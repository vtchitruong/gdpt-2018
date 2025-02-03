data = '''
0 1 2 3 4 5 6
0 1
0 2
1 2
1 3
1 4
2 4
3 4
3 5
4 5
0
5
'''


# Hàm khởi tạo danh sách kề
def init_adjacency_list(input_data):
    # Chuyển đổi input thành danh sách các dòng riêng lẻ
    lines = input_data.strip().split('\n')

    # Tách rời các số của dòng đầu tiên, lưu vào biến V là danh sách các đỉnh
    V = list(map(int, lines[0].split()))

    # Khởi tạo danh sách kề L rỗng (dùng kiểu dictionary)
    L = {v: [] for v in V}

    # Duyệt các dòng tiếp theo và nạp phần tử vào các danh sách đỉnh kề
    for line in lines[1:len(lines) - 2]:
        u, v = map(int, line.split())
        L[u].append(v)
        L[v].append(u)

    return L


# Hàm tìm đường đi từ đỉnh start đến đỉnh finish bằng DFS
def dfs(adj_list, start, finish):
    # Khởi tạo ngăn xếp stack để áp dụng thuật toán DFS
    stack = [start]

    # Khởi tạo dictionary trace để lưu vết đường đi
    trace = {start: None}

    # Trong khi stack vẫn còn phần tử
    while stack:
        # Lấy đỉnh trên cùng ra khỏi ngăn xếp, đặt là đỉnh current
        current = stack.pop()

        # Nếu đỉnh u là đỉnh finish thì trả về True
        if current == finish:
            return trace

        # Duyệt các đỉnh kề của đỉnh current
        for v in adj_list[current]:
            # Nếu đỉnh kề chưa được ghé thăm
            if v not in trace:
                # Đánh dấu đỉnh kề đã được ghé thăm bằng cách lưu vết đường đi
                trace[v] = current

                # Thêm đỉnh kề vào ngăn xếp
                stack.append(v)
        
    # Nếu không tìm thấy đường đi từ start đến finish thì trả về None
    return None


# Hàm truy vết đường đi từ đỉnh start đến đỉnh finish
def get_path(trace, start, finish):
    # Nếu không tìm thấy đường đi
    if trace is None:
        # thì trả về mảng rỗng
        return []
        
    # Khởi tạo mảng path để lưu đường đi từ đỉnh start đến đỉnh finish
    path = []

    # Biến tạm node dùng để di chuyển ngược từ đỉnh finish về đỉnh start
    node = finish

    # Trong khi node chưa về đến đỉnh start
    while node != start:
        # Thêm node vào mảng path
        path.append(node)

        # Di chuyển ngược về đỉnh trước đó
        node = trace[node]

    # Thêm đỉnh start vào mảng path
    path.append(start)

    # Đảo ngược mảng path để in ra đúng thứ tự
    path.reverse()

    return path


# Chương trình chính
if __name__ == '__main__':
    # Đọc dữ liệu input và đưa vào biến al
    al = init_adjacency_list(data)

    # Lấy đỉnh bắt đầu và đỉnh kết thúc
    lines = data.strip().split('\n')
    s = int(lines[-2])
    f = int(lines[-1])

    # Gọi hàm tính dfs() và lưu kết quả vào biến path
    trace_result = dfs(al, s, f)

    # Gọi hàm truy vết để lấy đường đi từ đỉnh s đến đỉnh f
    path_result = get_path(trace_result, s, f)

    # In đường đi
    if trace_result:
        print(f'Đường đi từ đỉnh {s} đến đỉnh {f} là:', end=' ')
        print(' -> '.join(map(str, path_result)))
    else:
        print(f'Không tìm thấy đường đi từ đỉnh {s} đến đỉnh {f}')