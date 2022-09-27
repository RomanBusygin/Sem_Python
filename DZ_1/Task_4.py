number = int(input('Введите номер четверти: '))
if number == 1:
    print('X [0; ∞] - Y [0; ∞]')
elif number == 2:
    print('X [-∞; 0] - Y [0; ∞]')
elif number == 3:
    print('X [-∞; 0] - Y [-∞; 0]')
elif number == 4:
    print('X [0; ∞] - Y [-∞; 0]')