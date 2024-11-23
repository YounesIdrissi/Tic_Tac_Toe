#Integrating OOP with Tkinter GUI for a complete project
import tkinter as tk
import random
from array import *

game_running = True
curr_player = 'X or O' #serves as declaration of variable ('X or O' will be changed)

chart = ([0, 0, 0], #2D array 1 tuple of 3 lists (Tic Tac Toe grid)
         [0, 0, 0], 
         [0, 0, 0])

root = tk.Tk() #instantiation of the master (root) window --------------------------------------------------------------

#game functions

def coin_flip(): #coin flip using random to assign current player
        global curr_player
        list1 = [1, 2]
        num = int(random.choice(list1)) % 2

        if num == 0:
            curr_player = 'X'
        else:
            curr_player = 'O'

def x_turn():
    global curr_player
    if chart[0][0] != 0:
        pass
    else:
        btn1.configure(text=curr_player)
        curr_player = 'O'

def o_turn():
    global curr_player
    if chart[0][0] != 0:
        pass
    else:
        btn1.configure(text=curr_player)
        curr_player = 'X'

def game():
    global curr_player
    coin_flip()
    if curr_player == 'X':
        x_turn()
    else:
        o_turn()
        
def each_button(btn):
    while btn == 0:
        btn.configure(text=curr_player)       

#the following are some basic window parameters

root.geometry("500x500")
root.title("Tic-Tac-Toe")
label = tk.Label(root, text=("Tic-Tac-Toe"), font=("Cosmic Sans", 40))
label.pack(pady=10)
turn_label = tk.Label(root, text=(curr_player), font=("Ariel", 30))
turn_label.pack(pady=5)

#the following is the tic-tac-toe grid layout // this is the grid user interface (think of the chart 2D array)

buttonframe = tk.Frame(root) #frame is instantiated inside the master (root) window
buttonframe.columnconfigure(0, weight=1) #column is vertical organization of button objects
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn_change = tk.StringVar() #allows button text to change when clicked

btn1 = tk.Button(buttonframe, text=(chart[0][0]), font=("Comic Sans", 30), command=lambda : each_button("btn1"))
btn1.grid(row=0, column=0, sticky=tk.E+tk.W)

btn2 = tk.Button(buttonframe, text=(chart[0][1]), font=("Comic Sans", 30), command=lambda : each_button("btn2"))
btn2.grid(row=0, column=1, sticky=tk.E+tk.W)

btn3 = tk.Button(buttonframe, text=(chart[0][2]), font=("Comic Sans", 30), command=lambda : each_button("btn3"))
btn3.grid(row=0, column=2, sticky=tk.E+tk.W)

btn4 = tk.Button(buttonframe, text=(chart[1][0]), font=("Comic Sans", 30), command=lambda : each_button("btn4"))
btn4.grid(row=1, column=0, sticky=tk.E+tk.W)

btn5 = tk.Button(buttonframe, text=(chart[1][1]), font=("Comic Sans", 30), command=lambda : each_button("btn5"))
btn5.grid(row=1, column=1, sticky=tk.E+tk.W)

btn6 = tk.Button(buttonframe, text=(chart[1][2]), font=("Comic Sans", 30), command=lambda : each_button("btn6"))
btn6.grid(row=1, column=2, sticky=tk.E+tk.W)

btn7 = tk.Button(buttonframe, text=(chart[2][0]), font=("Comic Sans", 30), command=lambda : each_button("btn7"))
btn7.grid(row=2, column=0, sticky=tk.E+tk.W)

btn8 = tk.Button(buttonframe, text=(chart[2][1]), font=("Comic Sans", 30), command=lambda : each_button("btn8"))
btn8.grid(row=2, column=1, sticky=tk.E+tk.W)

btn9 = tk.Button(buttonframe, text=(chart[2][2]), font=("Comic Sans", 30), command=lambda : each_button("btn9"))
btn9.grid(row=2, column=2, sticky=tk.E+tk.W)

buttonframe.pack(fill='x')

btn_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

def all_buttons():
    for button in btn_list:
        while button["text"] == 0:
            button.configure(text=curr_player)



reset = tk.Button(root, text="RESET", font=("Comic Sans", 40))
reset.pack(pady=20)



root.mainloop() #runs the window/continuously displays the window -----------------------------------------------------------