from tkinter import Button, Entry, Label, Tk


def click(box_number, pos_num):
    res[pos_num] = box_number.get()
    last_move.reverse()
    move.configure(text = f'Ход игрока {last_move[0]}')
    win_or_not()

def win_or_not():
    count_x = 0
    count_o = 0
    for i in range(len(res)):
        if (res[i] == 'x') or (res[i] == 'х'):
            count_x += 1
        if (res[i] == 'o') or (res[i] == 'о'):
            count_o += 1
        if (count_x == 3) or (count_o == 3):
            move.configure(text = f'Победил игрок {last_move[1]}', font = ("Arial", 24))

def all_reset():
    box_1_1.delete(0)
    box_1_2.delete(0)
    box_1_3.delete(0)
    box_2_1.delete(0)
    box_2_2.delete(0)
    box_2_3.delete(0)
    box_3_1.delete(0)
    box_3_2.delete(0)
    box_3_3.delete(0)
    move.configure(text = f'Ход игрока {last_move[1]}', font = ("Arial", 12))

last_move = [1, 2]
res = ['' for i in range(9)]
win_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

game_window = Tk()
game_window.title("Крестики-нолики")
game_window.geometry('800x300')

lbl = Label(game_window, text = "В поля вводить 'x' или 'o'", font = ("Arial", 12))
lbl.grid(column = 0, row = 0)

box_1_1 = Entry(game_window, width = 5)
box_1_1.grid(column = 0, row = 1)
button_1_1 = Button(game_window, text = "Сходить", command = lambda: click(box_1_1, 0))
button_1_1.grid(column = 1, row = 1)

box_1_2 = Entry(game_window, width = 5)
box_1_2.grid(column = 2, row = 1, padx = 20)
button_1_2 = Button(game_window, text = "Сходить", command = lambda: click(box_1_2, 1))
button_1_2.grid(column = 3, row = 1, padx = 20)

box_1_3 = Entry(game_window, width = 5)
box_1_3.grid(column = 4, row = 1, padx = 20)
button_1_3 = Button(game_window, text = "Сходить", command = lambda: click(box_1_3, 2))
button_1_3.grid(column = 5, row = 1, padx = 20)

box_2_1 = Entry(game_window, width = 5)
box_2_1.grid(column = 0, row = 2)
button_2_1 = Button(game_window, text = "Сходить", command = lambda: click(box_2_1, 3))
button_2_1.grid(column = 1, row = 2)

box_2_2 = Entry(game_window, width = 5)
box_2_2.grid(column = 2, row = 2, padx = 20)
button_2_2 = Button(game_window, text = "Сходить", command = lambda: click(box_2_2, 4))
button_2_2.grid(column = 3, row = 2, padx = 20)

box_2_3 = Entry(game_window, width = 5)
box_2_3.grid(column = 4, row = 2, padx = 20)
button_2_3 = Button(game_window, text = "Сходить", command = lambda: click(box_2_3, 5))
button_2_3.grid(column = 5, row = 2, padx = 20)

box_3_1 = Entry(game_window, width = 5)
box_3_1.grid(column = 0, row = 3)
button_3_1 = Button(game_window, text = "Сходить", command = lambda: click(box_3_1, 6))
button_3_1.grid(column = 1, row = 3)

box_3_2 = Entry(game_window, width = 5)
box_3_2.grid(column = 2, row = 3, padx = 20)
button_3_2 = Button(game_window, text = "Сходить", command = lambda: click(box_3_2, 7))
button_3_2.grid(column = 3, row = 3, padx = 20)

box_3_3 = Entry(game_window, width = 5)
box_3_3.grid(column = 4, row = 3, padx = 20)
button_3_3 = Button(game_window, text = "Сходить", command = lambda: click(box_3_3, 8))
button_3_3.grid(column = 5, row = 3, padx = 20)

move = Label(game_window, text = f'Ход игрока {last_move[0]}', font = ("Arial", 12))
move.grid(column = 0, row = 5)

clear_button = Button(game_window, text = "Очистить", command = all_reset)
clear_button.grid(column = 0, row = 6)

game_window.mainloop()