import random as rd

# Hàm dùng để phát sinh ngẫu nhiên n số nguyên có giá trị từ 1 đến 100
def generate(n):
    # Khởi tạo danh sách L rỗng
    L = []

    # Lặp n lần thao tác thêm (append) số nguyên vào L
    for i in range(n):
        L.append(rd.randint(1, 100))

    # Trả về danh sách kết quả
    return L


# Hàm filter_even() lọc ra các số chẵn trong danh sách
def filter_even(L):
    # Lấy số lượng phần tử của L
    n = len(L)

    # Khởi tạo danh sách kết quả là rỗng
    even_list = []

    # Duyệt từng phần tử trong phạm vi [0..n - 1]
    # Nếu phần tử L[i] chẵn thì nạp nó vào danh sách kết quả
    for i in range(n):
        if L[i] % 2 == 0:
            even_list.append(L[i])

    # Trả về danh sách kết quả
    return even_list


# Hàm count_multiple_of_3_and_5() dùng để đếm các số chia hết cho 3 và 5
def count_multiple_of_3_and_5(L):
    # Lấy số lượng phần tử của L
    n = len(L)

    # Khởi tạo biến đếm bằng 0
    counter = 0

    # Duyệt từng phần tử trong phạm vi [0..n - 1]
    # Nếu phần tử L[i] chia hết cho cả 3 và 5 thì tăng biến đếm lên 1
    for i in range(n):
        if L[i] % 3 == 0 and L[i] % 5 == 0:
            counter = counter + 1

    # Trả về kết quả
    return counter


# Hàm find() dùng để tìm phần tử có giá trị k trong danh sách
def find(L, k):
    # Lấy số lượng phần tử của L
    n = len(L)

    # Duyệt từng phần tử trong phạm vi [0..n - 1]
    # Nếu phần tử L[i] bằng k thì trả về i
    for i in range(n):
        if L[i] == k:
            return i

    # Nếu không tìm thấy thì trả về -1
    return -1


# Hàm max_value() dùng để tìm giá trị lớn nhất trong danh sách
def max_value(L):
    # Lấy số lượng phần tử của L
    n = len(L)

    # Khởi tạo max_val bằng giá trị của phần tử đầu tiên
    max_val = L[0]

    # Duyệt từng phần tử trong phạm vi [1..n - 1]
    # Nếu phần tử L[i] lớn hơn max_val thì cập nhật giá trị mới cho max_val
    for i in range(n):
        if L[i] > max_val:
            max_val = L[i]

    # Trả về giá trị lớn nhất tìm được
    return max_val


# Chương trình chính
if __name__ == '__main__':
    # Cho người dùng nhập số lượng phần tử
    number_of_elements = int(input('Nhập số lượng phần tử: '))

    # Gọi hàm generate() để phát sinh danh sách ngẫu nhiên
    my_list = generate(number_of_elements)

    # In danh sách ra màn hình
    print(f'Danh sách ban đầu: {my_list}')

    # Gọi hàm filter_even() và in ra danh sách số chẵn
    even_list = filter_even(my_list)
    print(f'Danh sách các số chẵn: {even_list}')

    # Gọi hàm count_multiple_of_3_and_5() và in ra số lượng
    count_result = count_multiple_of_3_and_5(my_list)
    print(f'Số lượng các số chia hết cho 3 và 5: {count_result}')

    # Cho người dùng nhập số cần tìm và gọi hàm find()
    key = int(input('Nhập số cần tìm đi bạn hiền: '))
    index = find(my_list, key)

    # Xét chỉ số kết quả và in ra thông báo tương ứng
    if index == -1:
        print('Có không giữ mất đừng tìm')
    else:
        print(f'Tìm thấy {key} tại vị trí {index}')

    # Gọi hàm max_value() và in ra giá trị lớn nhất
    my_max = max_value(my_list)
    print(f'Giá trị lớn nhất: {my_max}')
