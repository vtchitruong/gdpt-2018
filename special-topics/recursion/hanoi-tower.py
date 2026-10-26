# Hàm dùng để giải bài toán Tháp Hà Nội
def hanoi_tower(disk, source, target):
    # Trường hợp cơ sở
    if disk == 1:
        print(f'Chuyển dĩa 1: từ cột {source} đến cột {target}')
        return

    # Xác định cột trung gian
    spare = 6 - (source + target)

    # Bước 1: di chuyển disk - 1 dĩa nằm trên từ cột bắt đầu đến cột trung gian
    hanoi_tower(disk - 1, source, spare)

    # Bước 2: di chuyển dĩa thứ disk nằm dưới cùng từ cột bắt đầu đến cột mục tiêu
    print(f'Chuyển dĩa {disk}: từ cột {source} đến cột {target}')

    # Bước 3: di chuyển disk - 1 dĩa từ cột trung gian đến cột mục tiêu
    hanoi_tower(disk - 1, spare, target)


# Chương trình chính
if __name__ == '__main__':
    n = int(input('Số lượng dĩa: '))
    s = int(input('Cột bắt đầu: '))
    t = int(input('Cột mục tiêu: '))

    hanoi_tower(n, s, t)