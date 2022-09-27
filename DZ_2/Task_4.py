from random import randint


number = int(input('Введите число: '))
list = []
multiply = 1

for i in range(number):
    list.append(randint(-number, number))
print(list)

position = input('Введите позиции для умножения через пробел (нумерация начинается с ноля): ')
position_spl = position.split(' ')

for j in range(len(position_spl)):
    multiply *= list[int(position_spl[j])]
print(multiply)