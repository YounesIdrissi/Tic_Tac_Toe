import tkinter as tk
import random

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

def change(): #changes button text to curr_player (X or O) when clicked and tests for wins after each text change
    global curr_player
    global game_running
    if game_running == True:
        if btn1["text"] == "":
            btn1.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn1 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change)
btn1.grid(row=0, column=0, sticky=tk.E+tk.W)

def change2():
    global curr_player
    global game_running
    if game_running == True: 
        if btn2["text"] == "":
            btn2.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn2 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change2)
btn2.grid(row=0, column=1, sticky=tk.E+tk.W)

def change3():
    global curr_player
    global game_running
    if game_running == True:
        if btn3["text"] == "":
            btn3.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn3 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change3)
btn3.grid(row=0, column=2, sticky=tk.E+tk.W)

def change4():
    global curr_player
    global game_running
    if game_running == True:
        if btn4["text"] == "":
            btn4.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn4 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change4)
btn4.grid(row=1, column=0, sticky=tk.E+tk.W)

def change5():
    global curr_player
    global game_running
    if game_running == True:
        if btn5["text"] == "":
            btn5.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn5 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change5)
btn5.grid(row=1, column=1, sticky=tk.E+tk.W)

def change6():
    global curr_player
    global game_running
    if game_running == True:
        if btn6["text"] == "":
            btn6.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn6 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change6)
btn6.grid(row=1, column=2, sticky=tk.E+tk.W)

def change7():
    global curr_player
    global game_running
    if game_running == True:
        if btn7["text"] == "":
            btn7.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn7 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change7)
btn7.grid(row=2, column=0, sticky=tk.E+tk.W)

def change8():
    global curr_player
    global game_running
    if game_running == True:
        if btn8["text"] == "":
            btn8.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn8 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change8)
btn8.grid(row=2, column=1, sticky=tk.E+tk.W)

def change9():
    global curr_player
    global game_running
    if game_running == True:
        if btn9["text"] == "":
            btn9.configure(text=curr_player)
            if curr_player == 'X':
                curr_player = 'O'
            else:
                curr_player = 'X'
            turn_label["text"] = "Current Player: " + curr_player
            win_condition1()
            win_condition2()
            win_condition3()
            draw()
        else:
            pass

btn9 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30), command=change9)
btn9.grid(row=2, column=2, sticky=tk.E+tk.W)


buttonframe.pack(fill='x')

#win conditions and draw condition

def win_condition1(): #tests horizontal win condition
    global game_running
    if game_running == True:
        if btn1["text"] != "" and btn1["text"] == btn2["text"] == btn3["text"]: 
            if btn1["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False
        elif btn4["text"] != "" and btn4["text"] == btn5["text"] == btn6["text"]:
            if btn4["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False
        elif btn7["text"] != "" and btn7["text"] == btn8["text"] == btn9["text"]:
            if btn7["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False

def win_condition2(): #tests vertical win condition
    global game_running
    if game_running == True:
        if btn1["text"] != "" and btn1["text"] == btn4["text"] == btn7["text"]: 
            if btn1["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False
        elif btn2["text"] != "" and btn2["text"] == btn5["text"] == btn8["text"]:
            if btn2["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False
        elif btn3["text"] != "" and btn3["text"] == btn6["text"] == btn9["text"]:
            if btn3["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False

def win_condition3(): #tests diagonal win condition
    global game_running
    if game_running == True:
        if btn1["text"] != "" and btn1["text"] == btn5["text"] == btn9["text"]: 
            if btn1["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False
        elif btn3["text"] != "" and btn3["text"] == btn5["text"] == btn7["text"]:
            if btn3["text"] == 'X':
                turn_label["text"] = "X is the winner!"
            else:
                turn_label["text"] = "O is the winner!"
            game_running = False

def draw(): #tests for draw
    global game_running
    if (game_running and btn1["text"] != "" and btn2["text"] != "" and btn3["text"] != "" and btn4["text"] != "" 
    and btn5["text"] != "" and btn6["text"] != "" and btn7["text"] != "" and btn8["text"] != "" and btn9["text"] != ""):
        turn_label["text"] = "Draw!"
        game_running = False

#reset button

def restart(): #resets game: game_running is True, btn texts are cleared, coin is refliped
    global game_running
    game_running = True
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""
    coin_flip()

reset = tk.Button(root, text=("Reset"), font=("Comic Sans", 40), command=restart)
reset.pack(pady=20)

root.mainloop()