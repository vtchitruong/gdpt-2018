if __name__ == '__main__':
    # Khai báo bảng điểm môn Tin học bằng cách liệt kê các phần tử
    score_list = [8.1, 9.6, 3.5, 5.5, 10, 10, 7.4, 8.4, 4.9, 6.8]

    # In danh sách ra màn hình
    print(f'Bảng điểm: {score_list}')

    # Khai báo danh sách rỗng
    empty_score_list = []

    # In danh sách ra màn hình
    print(f'Danh sách rỗng: {empty_score_list}')

    # In ra phần tử đầu tiên
    print(f'Phần tử đầu tiên: {score_list[0]}')

    # In ra phần tử có chỉ số 1
    print(f'Phần tử có chỉ số 1: {score_list[1]}')

    # In ra phẩn tử cuối cùng
    n = len(score_list)
    print(f'Phần tử cuối cùng: {score_list[n - 1]}')

    # In ra các điểm số trên từng dòng
    n = len(score_list)
    for i in range(n):
        print(score_list[i])

    # In ra các điểm số trên từng dòng
    for score in score_list:
        print(score)