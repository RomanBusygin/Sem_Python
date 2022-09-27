x = int(input('Введите координату Х: '))
y = int(input('Введите координату Y: '))

if (x > 0) and (y > 0):
    print('I Четверть')
elif (x < 0) and (y > 0):
    print('II Четверть')
elif (x < 0) and (y < 0):
    print('III Четверть')
elif (x > 0) and (y < 0):
    print('IV Четверть')
