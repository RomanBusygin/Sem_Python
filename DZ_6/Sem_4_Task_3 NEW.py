numbers = input('Введите элементы через пробел: ').split(' ')
print(f'Неповторяющиеся элементы из Вашего списка: {list(filter(lambda x: numbers.count(x) == 1, numbers))}')