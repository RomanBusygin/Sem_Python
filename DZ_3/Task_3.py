def diff_fractional(fractional_list: list) -> int:
    min_fr = fractional_list[0] % 1
    max_fr = fractional_list[0] % 1
    for i in range(len(fractional_list)):
        if (fractional_list[i] % 1) < min_fr:
            min_fr = fractional_list[i] % 1
        if (fractional_list[i] % 1) > max_fr:
            max_fr = fractional_list[i] % 1
    return max_fr - min_fr

number_list = input('Введите вещественные числа через пробел: ').split(' ')
for j in range(len(number_list)):
    number_list[j] = float(number_list[j])

print(f'Разница между максимальным и минимальным дробным числом элементов равна: {diff_fractional(number_list)}')