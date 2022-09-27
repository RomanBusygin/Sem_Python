from random import randint


def gen_polinom(degree: int) -> str:
    polinom = ""
    for i in range(k, -1, -1):
        if i > 1:
            rand = randint(0, 100)
            if rand != 0:
                polinom += f'{rand}x^{i} + '
        elif i == 1:
            rand = randint(0, 100)
            if rand != 0:
                polinom += f'{rand}x + '
        elif i == 0:
            rand = randint(0, 100)
            if rand != 0:
                polinom += f'{rand}'
    return polinom

k = int(input('Введите натуральную степень k: '))
with open('file.txt', 'w') as file:
    file.write(gen_polinom(k))