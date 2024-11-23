import tkinter as tk
import random
from functools import partial

root = tk.Tk()
game_running = True

#basic window parameters
root.geometry("500x500")
root.title("Tic-Tac-Toe")
label = tk.Label(root, text=("Tic-Tac-Toe"), font=("Cosmic Sans", 40))
label.pack(pady=10)
turn_label = tk.Label(root, text=(""), font=("Ariel", 30))
turn_label.pack(pady=5)

def coin_flip(): #selects at random first player (X or O) and displays the first player in turn label
    global curr_player
    num = random.randint(1, 2) % 2
    if num == 0:
        curr_player = 'X'
    else:
        curr_player = 'O'
    turn_label["text"] = "Current Player: " + curr_player

coin_flip()

#main grid
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

def change(btn): #changes button text to curr_player (X or O) when clicked and tests for wins after each text change
    global curr_player
    if game_running:
        if btn["text"] == "":
            btn.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            horizontal_win()
            vertical_win()
            diagonal_win()
            draw()
            

btn1 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn1.grid(row=0, column=0, sticky=tk.E+tk.W)
btn1.config(command=partial(change, btn1))

btn2 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn2.grid(row=0, column=1, sticky=tk.E+tk.W)
btn2.config(command=partial(change, btn2))

btn3 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn3.grid(row=0, column=2, sticky=tk.E+tk.W)
btn3.config(command=partial(change, btn3))

btn4 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn4.grid(row=1, column=0, sticky=tk.E+tk.W)
btn4.config(command=partial(change, btn4))

btn5 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn5.grid(row=1, column=1, sticky=tk.E+tk.W)
btn5.config(command=partial(change, btn5))

btn6 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn6.grid(row=1, column=2, sticky=tk.E+tk.W)
btn6.config(command=partial(change, btn6))

btn7 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn7.grid(row=2, column=0, sticky=tk.E+tk.W)
btn7.config(command=partial(change, btn7))

btn8 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn8.grid(row=2, column=1, sticky=tk.E+tk.W)
btn8.config(command=partial(change, btn8))

btn9 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn9.grid(row=2, column=2, sticky=tk.E+tk.W)
btn9.config(command=partial(change, btn9))

btn_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9] #list is after btn objects are declared

buttonframe.pack(fill='x')

#win conditions and draw condition

def end_game(btn): #decides whether X or O is the winner, game_running = False
    global game_running
    if btn["text"] == 'X':
        turn_label["text"] = "X is the winner!"
    else:
        turn_label["text"] = "O is the winner!"
    game_running = False

def horizontal_win(): #tests horizontal win condition
    if game_running:
        if btn1["text"] != "" and btn1["text"] == btn2["text"] == btn3["text"]: 
            end_game(btn1)
        elif btn4["text"] != "" and btn4["text"] == btn5["text"] == btn6["text"]:
            end_game(btn4)
        elif btn7["text"] != "" and btn7["text"] == btn8["text"] == btn9["text"]:
            end_game(btn7)

def vertical_win(): #tests vertical win condition
    if game_running:
        if btn1["text"] != "" and btn1["text"] == btn4["text"] == btn7["text"]: 
            end_game(btn1)
        elif btn2["text"] != "" and btn2["text"] == btn5["text"] == btn8["text"]:
            end_game(btn2)
        elif btn3["text"] != "" and btn3["text"] == btn6["text"] == btn9["text"]:
            end_game(btn3)

def diagonal_win(): #tests diagonal win condition
    if game_running:
        if btn1["text"] != "" and btn1["text"] == btn5["text"] == btn9["text"]: 
            end_game(btn1)
        elif btn3["text"] != "" and btn3["text"] == btn5["text"] == btn7["text"]:
            end_game(btn3)

def draw(): #tests for draw, checks if game is still running, and all spots taken
    global game_running
    if game_running and all(button["text"] for button in btn_list): #checks if text exists in all button texts
        turn_label["text"] = "Draw!"
        game_running = False

#reset button

def restart(): #resets game: game_running is True, btn texts are cleared, coin is refliped, resets turn
    global game_running
    game_running = True
    for button in btn_list:
        button["text"] = ""
    coin_flip()

reset = tk.Button(root, text=("Reset"), font=("Comic Sans", 40), command=restart)
reset.pack(pady=20)

root.mainloop()