from tkinter import *

root = Tk()
field = []
sign = 'O'

for row in range(3):
    table = []
    for col in range(3):
        button = Button(root, text='', width=9, height=5, command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        table.append(button)
    field.append(table)


def click(row, col):
    global sign
    if field[row][col]['text'] == '' and sign == 'O':
        field[row][col]['text'] = 'X'
        sign = 'X'
        check_win()
    elif field[row][col]['text'] == '' and sign == 'X':
        field[row][col]['text'] = 'O'
        sign = 'O'
        check_win()


def check_win():
    for i in range(3):
        if field[i][0]['text'] == field[i][1]['text'] == field[i][2]['text'] != '':
            field[1][1]['text'] = f'Победил {sign}'
            break

    for i in range(3):
        if field[0][i]['text'] == field[1][i]['text'] == field[2][i]['text'] != '':
            field[1][1]['text'] = f'Победил {sign}'
            break

    if field[0][0]['text'] == field[1][1]['text'] == field[2][2]['text'] != '':
        field[1][1]['text'] = f'Победил {sign}'

    if field[0][2]['text'] == field[1][1]['text'] == field[2][0]['text'] != '':
        field[1][1]['text'] = f'Победил {sign}'


root.mainloop()
