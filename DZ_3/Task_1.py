def even_sum(sum_even_list: list) -> int:
    sum = 0
    for i in range(1, len(sum_even_list), 2):
        sum += int(sum_even_list[i])
    return sum

my_list = input('Введите числа через пробел: ').split(' ')
print(f'Сумма элементов на нечётных позициях равна: {even_sum(my_list)}')