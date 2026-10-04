def factorial(n):
    # Trường hợp cơ sở
    if n == 0 or n == 1:
        return 1

    # Trường hợp đệ quy
    return factorial(n - 1) * n


if __name__ == '__main__':
    number = int(input('Nhập số nguyên không âm: '))

    result = factorial(number)
    print(f'{number}! = {result}')