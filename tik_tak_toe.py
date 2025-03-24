from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def callback(r, c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].config(text='X', bg='blue', fg='white')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game==False:
        b[r][c].config(text='O', bg='blue', fg='white')
        states[r][c] = 'O'
        player = 'X'
    check_winner()


def check_winner():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            b[i][0].config(bg='yellow')
            b[i][1].config(bg='yellow')
            b[i][2].config(bg='yellow')
            stop_game = True
            messagebox.showinfo("info", "congratulation" + " " + b[i][2].cget('text')+" "+"you win the game")

    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i] != 0:
            b[0][i].config(bg='yellow')
            b[1][i].config(bg='yellow')
            b[2][i].config(bg='yellow')
            stop_game = True
            messagebox.showinfo("info", "congratulation" + " " + b[2][i].cget('text') + " " + "you win the game")
        if states[0][0] == states[1][1] == states[2][2] != 0:
            b[0][0].config(bg='yellow')
            b[1][1].config(bg='yellow')
            b[2][2].config(bg='yellow')
            stop_game = True
            messagebox.showinfo("info", "congratulation"+" " + b[2][2].cget('text')+" " + "you win the game")
        if states[2][0] == states[1][1] == states[0][2] != 0:
            b[2][0].config(bg='yellow')
            b[1][1].config(bg='yellow')
            b[0][2].config(bg='yellow')
            stop_game = True
            messagebox.showinfo("info", "congratulation" + " " + b[0][2].cget('text') + "  " + "you win the game")


window = Tk()
window.title("Welcome to play tic tac toe")
window.geometry('500x900')
window.configure(background = "grey")

b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(3):
    for j in range (3):
        b[i][j] = Button(font=("Arial", 64), width=4, bg='powder blue', command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)
player = 'X'
stop_game = False
window.mainloop()
