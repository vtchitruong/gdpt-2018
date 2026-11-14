# Hàm phát sinh chuỗi nhị phân theo phương pháp quay lui
def generate_binary_string(option):
    if len(option) == n:
        # Nếu đã đủ số lượng thì ghép các phần tử của option thành một chuỗi
        s = ''.join(map(str, option))

        # Lưu chuỗi nhị phân hoàn chỉnh vào biến kết quả
        solutions.append(s)
        return

    # Duyệt các giá trị ứng viên: 0 và 1
    for candidate in [0, 1]:
        # Bước 1 - Thử: nạp một ký tự vô phương án
        option.append(candidate)

        # Bước 2 - Tiến: gọi đệ quy để nạp ký tự ở vị trí tiếp theo
        generate_binary_string(option)

        # Bước 3 - Quay lui: gỡ bỏ ký tự vừa nạp ở cuối
        option.pop()


# Chương trình chính
if __name__ == '__main__':
    # Số lượng ký tự của chuỗi nhị phân
    n = int(input('Nhập số ký tự: '))

    # Khởi tạo danh sách kết quả binary_strings
    solutions = []

    # Khởi tạo phương án rỗng
    option = []

    # Gọi hàm generate_binary_string()
    generate_binary_string(option)

    # In ra các chuỗi nhị phân trong danh sách kết quả
    for s in solutions:
        print(s)