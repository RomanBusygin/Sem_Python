from random import randint


candies = 2021
max_move = 28
turn = randint(1, 2)
last_move = turn

while candies > 0:
    if turn == 1:
        if candies != 0:
            player = int(input('Ход Игрока: '))
            if player <= max_move:
                print(f'Конфет осталось: {candies - player}')
                candies -= player
                last_move = 1
                turn = 2
            else: print('Куда столько берёшь?!')
    if turn == 2:
        if candies != 0:
            bot = candies % (max_move + 1)
            if bot == 0:
                bot = randint(1, 28)
            print(f'Ход Бота: {bot}')
            print(f'Конфет осталось: {candies - bot}')
            candies -= bot
            last_move = 2
            turn = 1

if last_move == 1:
    print('Победил Игрок!')
else: 
    print('Победил Бот!')