number = input('Введите число: ')
sum = 0

for i in range(len(number)):
    if number[i] != '.':
        sum += int(number[i])
print(f'Сумма чисел введенного числа равна: {sum}')