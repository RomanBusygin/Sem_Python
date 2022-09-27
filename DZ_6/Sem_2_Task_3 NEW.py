k = int(input('Введите число: '))
f = lambda k: (1 + 1 / k) ** k
print(sum([f(k) for k in range(1, k + 1)]))