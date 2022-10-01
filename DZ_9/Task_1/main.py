from tkinter import Button, Label, Tk
from tkinter.ttk import Combobox


def click(box_number, pos_num):
    res[pos_num] = box_number.get()
    last_move.reverse()
    move.configure(text = f'Ход игрока {last_move[0]}')
    win_or_not()

def win_or_not():
    combo_x = []
    combo_y = []
    for i in range(len(res)):
        if (res[i] == 'X'):
            combo_x.append(i)
        if (res[i] == 'O'):
            combo_y.append(i)
        if (combo_x in win_combo) or (combo_y in win_combo):
            move.configure(text = f'Победил игрок {last_move[1]}', font = ("Arial", 16))

def all_reset():
    box_1_1.set('')
    box_1_2.set('')
    box_1_3.set('')
    box_2_1.set('')
    box_2_2.set('')
    box_2_3.set('')
    box_3_1.set('')
    box_3_2.set('')
    box_3_3.set('')
    global res
    res = ['' for i in range(9)]
    last_move = [1, 2]
    move.configure(text = f'Ход игрока {last_move[0]}', font = ("Arial", 12))
    

last_move = [1, 2]
res = ['' for i in range(9)]
win_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

game_window = Tk()
game_window.title("Крестики-нолики")

lbl = Label(game_window, text = "В поля вводить 'x' или 'o'", font = ("Arial", 12))
lbl.grid(column = 0, row = 0)

box_1_1 = Combobox(game_window, width = 5)
box_1_1['values'] = ('X', 'O')
box_1_1.grid(column = 0, row = 1)
button_1_1 = Button(game_window, text = "Сходить", command = lambda: click(box_1_1, 0))
button_1_1.grid(column = 1, row = 1)

box_1_2 = Combobox(game_window, width = 5)
box_1_2['values'] = ('X', 'O')
box_1_2.grid(column = 2, row = 1, padx = 20)
button_1_2 = Button(game_window, text = "Сходить", command = lambda: click(box_1_2, 1))
button_1_2.grid(column = 3, row = 1, padx = 20)

box_1_3 = Combobox(game_window, width = 5)
box_1_3['values'] = ('X', 'O')
box_1_3.grid(column = 4, row = 1, padx = 20)
button_1_3 = Button(game_window, text = "Сходить", command = lambda: click(box_1_3, 2))
button_1_3.grid(column = 5, row = 1, padx = 20)

box_2_1 = Combobox(game_window, width = 5)
box_2_1['values'] = ('X', 'O')
box_2_1.grid(column = 0, row = 2)
button_2_1 = Button(game_window, text = "Сходить", command = lambda: click(box_2_1, 3))
button_2_1.grid(column = 1, row = 2)

box_2_2 = Combobox(game_window, width = 5)
box_2_2['values'] = ('X', 'O')
box_2_2.grid(column = 2, row = 2, padx = 20)
button_2_2 = Button(game_window, text = "Сходить", command = lambda: click(box_2_2, 4))
button_2_2.grid(column = 3, row = 2, padx = 20)

box_2_3 = Combobox(game_window, width = 5)
box_2_3['values'] = ('X', 'O')
box_2_3.grid(column = 4, row = 2, padx = 20)
button_2_3 = Button(game_window, text = "Сходить", command = lambda: click(box_2_3, 5))
button_2_3.grid(column = 5, row = 2, padx = 20)

box_3_1 = Combobox(game_window, width = 5)
box_3_1['values'] = ('X', 'O')
box_3_1.grid(column = 0, row = 3)
button_3_1 = Button(game_window, text = "Сходить", command = lambda: click(box_3_1, 6))
button_3_1.grid(column = 1, row = 3)

box_3_2 = Combobox(game_window, width = 5)
box_3_2['values'] = ('X', 'O')
box_3_2.grid(column = 2, row = 3, padx = 20)
button_3_2 = Button(game_window, text = "Сходить", command = lambda: click(box_3_2, 7))
button_3_2.grid(column = 3, row = 3, padx = 20)

box_3_3 = Combobox(game_window, width = 5)
box_3_3['values'] = ('X', 'O')
box_3_3.grid(column = 4, row = 3, padx = 20)
button_3_3 = Button(game_window, text = "Сходить", command = lambda: click(box_3_3, 8))
button_3_3.grid(column = 5, row = 3, padx = 20)

move = Label(game_window, text = f'Ход игрока {last_move[0]}', font = ("Arial", 12))
move.grid(column = 0, row = 5)

clear_button = Button(game_window, text = "Очистить", command = all_reset)
clear_button.grid(column = 0, row = 6)

game_window.mainloop()