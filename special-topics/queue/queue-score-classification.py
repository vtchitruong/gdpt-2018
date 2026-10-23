from queue import Queue

data = '1 7 4 0 9 4 8 8 2 4 5 5'


# Hàm chuyển đổi dữ liệu chuỗi thành hàng đợi
def init_original_queue(dt):
    # Tách chuỗi dt theo khoảng trắng để tạo thành các số nguyên
    scores = map(int, dt.split())

    # Khởi tạo hàng đợi q
    q = Queue()

    # Duyệt từng số nguyên trong scores
    for score in scores:
        # Nạp từng số nguyên này vô hàng đợi q
        q.put(score)

    return q


# Hàm phân các số nguyên vô hai hàng đợi: đạt (>= 5) và chưa đạt (< 5)
def classify(q):
    # Khởi tạo hai hàng đợi
    pass_queue = Queue()
    fail_queue = Queue()

    # Trong khi hàng đợi q vẫn còn số nguyên
    while not q.empty():
        # thì lấy số nguyên nằm ở đầu hàng đợi
        score = q.get()

        # và nạp số nguyên này vô hàng đợi tương ứng
        if score >= 5:
            pass_queue.put(score)
        else:
            fail_queue.put(score)

    return pass_queue, fail_queue


# Chương trình chính
if __name__ == '__main__':
    # Gọi hàm init_original_queue để khởi tạo hàng đợi ban đầu
    original_queue = init_original_queue(data)

    # In hàng đợi ban đầu
    print('Hàng đợi điểm số ban đầu:', *original_queue.queue)

    # Gọi hàm classify để phân loại
    pass_queue, fail_queue = classify(original_queue)

    # In hai hàng đợi phân loại điểm số
    print('Hàng đợi xếp loại đạt:', *pass_queue.queue)
    print('Hàng đợi xếp loại chưa đạt:', *fail_queue.queue)

    # In hàng đợi ban đầu sau khi phân loại
    print('Hàng đợi điểm số ban đầu:', *original_queue.queue)