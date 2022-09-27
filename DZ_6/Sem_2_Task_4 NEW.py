from random import randint


number = int(input('Введите число: '))
multiply = 1
my_list = [randint(-number, number) for i in range(number)]
print(my_list)
position = list(map(int, input('Введите позиции для умножения через пробел (нумерация начинается с ноля): ').split()))

for i in range(len(position)):
    multiply *= my_list[position[i]]

print(multiply)