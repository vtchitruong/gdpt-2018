import sys

# Thiết lập lại độ sâu đệ quy nhằm tăng số lượng số hạng
sys.setrecursionlimit(1000000)


# Hàm tính số Pi
def pi(n):
    # Trường hợp cơ sở
    if n <= 0:
        return 0.0

    # Trường hợp đệ quy
    k = n - 1
    term = 4 * ((-1) ** k) / (2 * k + 1)
    return term + pi(k)


# Chương trình chính
if __name__ == "__main__":
    number = int(input('Nhập số lượng số hạng tham gia tính toán: '))

    PI = pi(number)
    print(f'Giá trị của Pi với {number} số hạng: {PI}')