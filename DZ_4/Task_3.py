def unic_elements(full_list: list) -> list:
    unic_list = []
    for i in full_list:
        if full_list.count(i) == 1:
            unic_list.append(i)
    return unic_list


numbers = input('Введите числа через пробел: ').split(' ')
print(f'Неповторяющиеся элементы из Вашего списка: {unic_elements(numbers)}')