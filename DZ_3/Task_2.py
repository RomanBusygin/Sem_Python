import math


def couple_multiply(multiply_list: list):
    multiply = 1
    for i in range(math.ceil(len(multiply_list) / 2)):
        multiply = int(multiply_list[i]) * int(multiply_list[-i - 1])
        print(multiply, end= ' ')

number_list = input('Введите числа через пробел: ').split(' ')
couple_multiply(number_list)