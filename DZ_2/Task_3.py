k = int(input('Введите число: '))
list = []
sum = 0

for i in range(1, k + 1):
    list.append((1 + 1 / i) ** i)
    sum += list[i - 1]
print(sum)