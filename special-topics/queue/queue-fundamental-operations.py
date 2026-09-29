from queue import Queue

if __name__ == '__main__':
    # Khởi tạo hàng đợi
    q = Queue()

    # Thêm phần tử vô hàng đợi
    q.put('Elon Musk')
    q.put('Jeff Bezos')
    q.put('Mark Zuckerberg')
    q.put('Bernard Arnault')
    q.put('Larry Ellison')
    q.put('Jensen Huang')
    q.put('Andrej Karpathy')

    # In hàng đợi
    print('Hàng đợi hiện tại:')
    print(*q.queue, sep=', ')

    # Lấy phần tử ra khỏi hàng đợi
    # customer = q.get()
    # print(f'Đang phục vụ {customer}')

    # customer = q.get()
    # print(f'Đang phục vụ {customer}')

    # customer = q.get()
    # print(f'Đang phục vụ {customer}')

    # customer = q.get()
    # print(f'Đang phục vụ {customer}')

    # customer = q.get()
    # print(f'Đang phục vụ {customer}')

    # customer = q.get()
    # print(f'Đang phục vụ {customer}')

    # customer = q.get()
    # print(f'Đang phục vụ {customer}')

    # Lấy phần tử ra khỏi hàng đợi
    while not q.empty():
        customer = q.get()
        print(f'Đang phục vụ {customer}')