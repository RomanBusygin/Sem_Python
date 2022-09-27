def to_bin(n: int) -> list:
    number_bin = []
    while n > 0:
        number_bin.insert(0, n % 2)
        n = int(n / 2)
    print(f'Число {number} в двоичной системе равно: ', end='')
    for i in range(len(number_bin)):
        print(number_bin[i], end='')

number = int(input('Введите число в десятичной системе: '))
to_bin(number)