# Hàm phát sinh các hoán vị theo phương pháp quay lui
def generate_permutations(option, used):
    if len(option) == n:
        # Nếu đã đủ số từ thì ghép thành câu
        s = ' '.join(option)

        # Lưu câu hoàn chỉnh vào danh sách kết quả
        sentences.append(s)
        return

    # Duyệt các từ trong danh sách words
    for i in range(n):
        if not used[i]:
            # Bước 1 - Thử: nạp từ chưa xài vô phương án, rồi đánh dấu đã xài
            option.append(words[i])
            used[i] = True

            # Bước 2: Tiến: gọi đệ quy để chọn từ cho vị trí tiếp theo
            generate_permutations(option, used)

            # Bước 3: Quay lui: gỡ bỏ từ vừa nạp và khôi phục trạng thái chưa xài
            option.pop()
            used[i] = False


# Chương trình chính
if __name__ == '__main__':
    # Danh sách các từ ban đầu
    words = ['hôm', 'bữa', 'đi', 'học', 'chưa']

    # Tính số lượng từ
    n = len(words)

    # Khởi tạo danh sách kết quả sentence
    sentences = []

    # Khởi tạo phương án rỗng
    option = []

    # Khởi tạo danh sách used dùng để đánh dấu các từ đã xài
    used = [False] * n

    # Gọi hàm generate_permutations
    generate_permutations(option, used)

    # In ra các câu trong danh sách kết quả
    for s in sentences:
        print(s)