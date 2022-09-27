number = input('Введите число: ')
summ = sum(list(map(int, [number[i] for i in range(len(number)) if number[i] != '.'])))
print(f'Сумма чисел введенного числа равна: {summ}')