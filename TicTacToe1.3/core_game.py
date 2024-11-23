import random
from array import *

game_running = True
curr_player = 'X or O' #serves as declaration of variable ('X or O' will be changed)

#2D array 1 tuple of 3 lists (Tic Tac Toe grid)

chart = ([0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0])

class GameFunctions:

    def coin_flip(self): #coin flip using random to assign current player
        global curr_player
        list1 = [1, 2]
        num = int(random.choice(list1)) % 2

        if num == 0:
            curr_player = 'X'
        else:
            curr_player = 'O'

    def display_chart(self): #Displays Chart/Game Function:
        for row in chart:
            for spot in row:
                print(spot, end=" ")
            print()

    def x_turn(self): #X turn function
        print("X's turn!")
        x = int(input("Enter the x value of the grid: "))
        y = int(input("Enter the y value of the grid: "))
        while chart[x][y] != 0:
            print(f"Spot already taken: {chart[x][y]}")
            game.display_chart()
            x = int(input("Enter a different x value of the grid: "))
            y = int(input("Enter a different y value of the grid: "))
        chart[x][y] = 'X'
        game.display_chart()

    def o_turn(self): #O turn function
        print("O's turn!")
        x = int(input("Enter the x value of the grid: "))
        y = int(input("Enter the y value of the grid: "))
        while chart[x][y] != 0:
            print(f"Spot already taken: {chart[x][y]}")
            game.display_chart()
            x = int(input("Enter a different x value of the grid: "))
            y = int(input("Enter a different y value of the grid: "))
        chart[x][y] = 'O'
        game.display_chart()

    def restart(self): #restart game prompt (restores chart to default and re-flip coin)
        global game_running
        global chart
        if not game_running:
            print("---------- GAME OVER ----------")
            print()
            x = input("Would you like to restart the game? (Type Y to restart): ")
            print()
            if x == 'Y':
                chart = ([0, 0, 0], 
                        [0, 0, 0], 
                        [0, 0, 0])
                game.coin_flip()
                game_running = True
            else:
                print("---------- Thanks for playing! ----------")

    def core_system(self): #core game system/player turn system
        global curr_player
        game.coin_flip()

        while game_running:
            if curr_player == 'X':
                game.x_turn()
                curr_player = 'O'

            else: #current player is O
                game.o_turn()
                curr_player = 'X'
            win.win_condition1()
            win.win_condition2()
            win.win_condition3()
            win.draw()
            game.restart()

game = GameFunctions()


class WinConditions: #tests if win/end condition is met, game_running = false

    def win_condition1(self): #tests horizontal win condition
        global game_running
        if chart[0][0] != 0 and chart[0][0] == chart[0][1] == chart[0][2]: 
            if chart[0][0] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False
        elif chart[1][0] != 0 and chart[1][0] == chart[1][1] == chart[1][2]:
            if chart[1][0] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False
        elif chart[2][0] != 0 and chart[2][0] == chart[2][1] == chart[2][2]:
            if chart[2][0] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False

    def win_condition2(self): #tests vertical win condition
        global game_running
        if chart[0][0] != 0 and chart[0][0] == chart[1][0] == chart[2][0]: 
            if chart[0][0] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False
        elif chart[0][1] != 0 and chart[0][1] == chart[1][1] == chart[2][1]:
            if chart[0][1] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False
        elif chart[0][2] != 0 and chart[0][2] == chart[1][2] == chart[2][2]:
            if chart[0][2] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False

    def win_condition3(self): #tests diagonal win condition
        global game_running
        if chart[0][0] != 0 and chart[0][0] == chart[1][1] == chart[2][2]: 
            if chart[0][0] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False
        elif chart[2][0] != 0 and chart[2][0] == chart[1][1] == chart[0][2]:
            if chart[2][0] == 'X':
                print("Player 1 (X) is the winner!")
                game.display_chart()
            else:
                print("Player 2 (O) is the winner!")
                game.display_chart()
            game_running = False

    def draw(self): #tests if there is no win (draw), game_running = False
        global game_running
        if (game_running and not any(0 in sublist for sublist in chart)):
            print("Draw!")
            game.display_chart()
            game_running = False

win = WinConditions()

game.core_system()
