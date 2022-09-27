def negafibonacci(n: int) -> list:
    fibonacci = [0, 1]
    count = 1
    for i in range(n - 1):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    for j in range(n):
        if j % 2 == 0:
            fibonacci.insert(0, fibonacci[j + count])
            count += 1
        else: 
            fibonacci.insert(0, (fibonacci[j + count] * -1))
            count += 1
    print(fibonacci)

number = int(input('Введите число: '))
print(f'Последовательность Негафибоначчи (почти Мега, но нет) для числа {number} равна: ', end='')
negafibonacci(number)