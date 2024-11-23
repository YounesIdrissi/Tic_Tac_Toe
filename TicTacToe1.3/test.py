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

#Higher Order Function
def btn_pass(btn): #this is the master function, it allows the passing of btn argument and the RETURN of the repeatable/inner function
    def change(): #changes button text to curr_player (X or O) when clicked and tests for wins after each text change
        global curr_player
        global game_running
        if game_running:
            if btn["text"] == "":
                btn.config(text=curr_player)
                if curr_player == 'X':
                    curr_player = 'O'
                else:
                    curr_player = 'X'
                turn_label["text"] = "Current Player: " + curr_player
    return change #there is another way: from functools import partial does the job the master function does here using: partial(change, btn1)

btn1 = tk.Button(buttonframe, text=(""), font=("Cosmic Sans", 30))
btn1.grid(row=0, column=0, sticky=tk.E+tk.W)
btn1.config(command=btn_pass(btn1))

buttonframe.pack(fill='x')


root.mainloop()