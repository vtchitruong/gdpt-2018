from queue import Queue

# Các câu lệnh
data = '''
ADD PARCEL_A
ADD PARCEL_B
DISPATCH
ADD PARCEL_C
ADD PARCEL_D
CANCEL PARCEL_B
ADD PARCEL_E
ADD PARCEL_F
CANCEL PARCEL_E
ADD PARCEL_G
DISPATCH
DISPATCH
DISPATCH
'''


# Khởi tạo hàng đợi (chính là băng tải)
conveyor = Queue()


# Hàm xử lý câu lệnh ADD
def add(parcel):
    # Đưa kiện hàng lên băng tải
    conveyor.put(parcel)

    # In ra thông báo
    print(f'Thêm kiện hàng {parcel} lên băng tải')


# Hàm xử lý câu lệnh DISPATCH
def dispatch():
    if conveyor.empty():
        # Nếu băng tải rỗng thì thông báo hết kiện hàng
        print('Không còn kiện hàng nào để xuất kho')
    else:
        # Ngược lại, nếu không rỗng thì xuất kho kiện hàng nằm ở đầu băng tải
        p = conveyor.get()

        # In ra thông báo
        print(f'Tiến hành xuất kho kiện hàng {p}')


# Hàm xử lý câu lệnh CANCEL
def cancel(parcel):
    # Dùng biến found để đánh dấu đã tìm thấy kiện hàng cần hủy
    found = False

    # Trong khi băng tải vẫn còn kiện hàng
    while not conveyor.empty():
        # Lấy kiện hàng ở đầu băng tải để xét
        p = conveyor.get()

        if p == parcel:
            # Nếu đúng là kiện hàng cần hủy thì in ra thông báo hủy
            print(f'Tiến hành hủy kiện hàng {parcel}')

            # Đánh dấu đã tìm thấy kiện hàng cần hủy
            found = True

            # Ngắt vòng lặp
            break
        else:
            # Ngược lại, nếu p chưa phải là kiện hàng cần hủy thì cho nó quay về cuối băng tải
            conveyor.put(p)

    if not found:
        # Nếu found == False thì thông báo lệnh CANCEL không thể xử lý
        print(f'Băng tải không có kiện hàng {parcel}, không có gì để hủy')


# Hàm đọc dữ liệu đầu vào
def parse_data(d):
    # Chuyển đổi dữ liệu đầu vào thành danh sách các câu lệnh
    return d.strip().splitlines()


# Hàm xử lý danh sách các câu lệnh
def process(commands):
    # Duyệt danh sách các câu lệnh
    for command in commands:
        # Phân tách hai thành phần của câu lệnh vô biến c
        c = command.split()

        # Xét thành phần đầu tiên của câu lệnh
        if c[0] == 'ADD':
            add(c[1])
        elif c[0] == 'DISPATCH':
            dispatch()
        elif c[0] == 'CANCEL':
            cancel(c[1])

        # In ra tình trạng hiện tại của băng tải
        print('Băng tải:', *conveyor.queue)
        print()


# Chương trình chính
if __name__ == '__main__':
    # Đọc dữ liệu đầu vào và đưa vô biến command_lines
    command_lines = parse_data(data)

    # Gọi hàm process() để xử lý các câu lệnh
    process(command_lines)