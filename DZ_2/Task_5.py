from random import randint


list_str = input('Введите элементы списка через пробел: ')
list = list_str.split(' ')
new_list = []
numbers = []

numbers.append(randint(0, len(list) - 1))
for i in range(1, len(list)):
    rand = randint(0, len(list) - 1)
    while rand in numbers:
        rand = randint(0, len(list) - 1)
    numbers.append(rand)

for j in range(len(list)):
    new_list.append(list[numbers[j]])
print(f'Перемешанный список: {new_list}')