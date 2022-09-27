from random import randint


candies = 2021
max_move = 28
turn = randint(1, 2)
last_move = turn

while candies > 0:
    if turn == 1:
        if candies != 0:
            player_1 = int(input('Ход Игрока 1: '))
            if player_1 <= max_move:
                print(f'Конфет осталось: {candies - player_1}')
                candies -= player_1
                last_move = 1
                turn = 2
            else: print('Куда столько берёшь?!')
    if turn == 2:
        if candies != 0:
            player_2 = int(input('Ход Игрока 2: '))
            if player_2 <= max_move:
                print(f'Конфет осталось: {candies - player_2}')
                candies -= player_2
                last_move = 2
                turn = 1
            else: print('Куда столько берёшь?!')

print(f'Победил Игрок {last_move}!')