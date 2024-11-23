import random
from array import *

player1 = 'X'
player2 = 'O'
game_running = True

#coin flip using random to assign current player

def coin_flip():
    list1 = [1, 2]
    num = int(random.choice(list1)) % 2

    if num == 0:
        return player1
    else:
        return player2

curr_player = coin_flip()

#2D array 1 list of 3 tuples (Tic Tac Toe grid)

chart = ([0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0])

#Display Chart/Game Function:

def display_chart():
    for row in chart:
        for spot in row:
            print(spot, end=" ")
        print()

#X turn function

def x_turn():
    print("X's turn!")
    x = int(input("Enter the x value of the grid: "))
    y = int(input("Enter the y value of the grid: "))
    while chart[x][y] != 0:
        print(f"Spot already taken: {chart[x][y]}")
        display_chart()
        x = int(input("Enter a different x value of the grid: "))
        y = int(input("Enter a different y value of the grid: "))
    chart[x][y] = 'X'
    display_chart()

#O turn function

def o_turn():
    print("O's turn!")
    x = int(input("Enter the x value of the grid: "))
    y = int(input("Enter the y value of the grid: "))
    while chart[x][y] != 0:
        print(f"Spot already taken: {chart[x][y]}")
        display_chart()
        x = int(input("Enter a different x value of the grid: "))
        y = int(input("Enter a different y value of the grid: "))
    chart[x][y] = 'O'
    display_chart()

#tests if win condition is met, game_running = false

def win_condition1(): #tests horizontal win condition
    global game_running
    if chart[0][0] != 0 and chart[0][0] == chart[0][1] == chart[0][2]: 
        if chart[0][0] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False
    elif chart[1][0] != 0 and chart[1][0] == chart[1][1] == chart[1][2]:
        if chart[1][0] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False
    elif chart[2][0] != 0 and chart[2][0] == chart[2][1] == chart[2][2]:
        if chart[2][0] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False

def win_condition2(): #tests vertical win condition
    global game_running
    if chart[0][0] != 0 and chart[0][0] == chart[1][0] == chart[2][0]: 
        if chart[0][0] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False
    elif chart[0][1] != 0 and chart[0][1] == chart[1][1] == chart[2][1]:
        if chart[0][1] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False
    elif chart[0][2] != 0 and chart[0][2] == chart[1][2] == chart[2][2]:
        if chart[0][2] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False

def win_condition3(): #tests diagonal win condition
    global game_running
    if chart[0][0] != 0 and chart[0][0] == chart[1][1] == chart[2][2]: 
        if chart[0][0] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False
    elif chart[2][0] != 0 and chart[2][0] == chart[1][1] == chart[0][2]:
        if chart[2][0] == 'X':
            print("Player 1 (X) is the winner!")
            display_chart()
        else:
            print("Player 2 (O) is the winner!")
            display_chart()
        game_running = False

#tests if draw, game_running = False

def draw():
    global game_running
    if (game_running and not any(0 in sublist for sublist in chart)):
        print("Draw!")
        display_chart()
        game_running = False

#restart game prompt (should restore chart to default and re-flip coin for player turn)

def restart():
    global game_running
    global chart
    global curr_player
    if not game_running:
        print("---------- GAME OVER ----------")
        print()
        x = input("Would you like to restart the game? (Type Y to restart): ")
        print()
        if x == 'Y':
            chart = ([0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0])
            curr_player = coin_flip()
            game_running = True
        else:
            print("---------- Thanks for playing! ----------")

#player turn system

while game_running:
    if curr_player == 'X':
        x_turn()
        curr_player = 'O'

    else: #current player is O
        o_turn()
        curr_player = 'X'
    win_condition1()
    win_condition2()
    win_condition3()
    draw()
    restart()
