import queue

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


# Hàm tạo danh sách kề
def init_adjacent_list(d):
    # Chuyển đổi input thành danh sách các dòng riêng lẻ
    lines = d.strip().split('\n')

    # Tách rời các số của dòng đầu tiên, lưu vào biến V là danh sách các đỉnh
    V = list(map(int, lines[0].split()))

    # Khởi tạo danh sách kề L rỗng (dùng kiểu dictionary)
    L = {v: [] for v in V}

    # Duyệt các dòng còn lại và nạp phần tử vào các danh sách đỉnh kề
    for line in lines[1:]:
        u, v = map(int, line.split())
        L[u].append(v)
        L[v].append(u)

    return L


# Hàm in danh sách kề
def print_adjacent_list(M):
    for u, neighbors in M.items():
        print(f'{u}: {neighbors}')


# Hàm tính khoảng cách từ đỉnh start đến đỉnh finish bằng BFS
def bfs(graph, start, finish):
    # Khởi tạo hàng đợi q để áp dụng thuật toán BFS
    q = queue.Queue()

    # Khởi tạo danh sách visited để lưu các đỉnh đã ghé thăm
    visited = []

    # Khởi tạo dictionary distance để lưu khoảng cách từ start đến các đỉnh khác
    distance = {start: 0}

    # Thêm đỉnh start vào hàng đợi
    q.put(start)

    # Đánh dấu đỉnh u đã ghé thăm
    visited.append(start)

    # Duyệt BFS: Trong khi hàng đợi vẫn còn phần tử
    while not q.empty():
        # Lấy đỉnh u ra khỏi hàng đợi
        u = q.get()

        # Nếu đỉnh u là đỉnh finish thì trả về khoảng cách
        if u == finish:
            return distance[u]

        # Duyệt các đỉnh kề của u
        for v in graph[u]:
            # Nếu đỉnh v chưa ghé thăm thì thêm đỉnh u vào hàng đợi
            if v not in visited:
                # Thêm đỉnh v vào hàng đợi
                q.put(v)

                # Đánh dấu đỉnh v đã ghé thăm
                visited.append(v)

                # Cập nhật khoảng cách từ start đến v
                distance[v] = distance[u] + 1
    
    # Nếu không tìm thấy đường đi từ start đến finish thì trả về -1
    return -1    
    

# Chương trình chính
if __name__ == '__main__':
    # Đọc dữ liệu input và đưa vào matrix
    adj_list = init_adjacent_list(data)

    # In danh sách kề
    print_adjacent_list(adj_list)

    # Đỉnh bắt đầu
    s = 0
    
    # Đỉnh kết thúc
    f = 5

    # Gọi hàm tính bfs() để khoảng cách từ đỉnh s đến đỉnh f
    d = bfs(adj_list, s, f)

    # In kết quả
    print(f'Khoảng cách từ {s} đến {f} là {d}')