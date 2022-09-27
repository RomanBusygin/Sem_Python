my_list = list(map(int, input('Введите числа через пробел: ').split(' ')))
print(f'Сумма элементов на нечётных позициях равна: {sum(filter(lambda x: my_list.index(x) % 2 != 0, my_list))}')