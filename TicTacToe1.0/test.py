import random

player1 = "X"
player2 = "O"
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

#2D array 1 list of 3 tuples

chart = ([0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0])

for row in chart:
    for spot in row:
        print(spot, end=" ")
    print()

#Game mechanics

#player turn system

#function to take coordinates(user input) and reference/alter 2D array value
# def coord_input():
#     xy_pos = array('i', [x, y])
#     ref_value = chart[xy_pos]

#xy_pos = int(array('i', [input("Enter the x and y coordinates of the grid: ")]))

def x_turn():
    print("X's turn!")
    x = int(input("Enter the x value of the grid: "))
    y = int(input("Enter the y value of the grid: "))
    while chart[x][y] != 0:
        print(f"Spot already taken: {chart[x][y]}")
        print(chart)
        x = int(input("Enter a different x value of the grid: "))
        y = int(input("Enter a different y value of the grid: "))
    chart[x][y] = "X"
    print(chart)

def o_turn():
    print("O's turn!")
    x = int(input("Enter the x value of the grid: "))
    y = int(input("Enter the y value of the grid: "))
    while chart[x][y] != 0:
        print(f"Spot already taken: {chart[x][y]}")
        print(chart)
        x = int(input("Enter a different x value of the grid: "))
        y = int(input("Enter a different y value of the grid: "))
    chart[x][y] = "O"
    print(chart)

while game_running:
    #test if win condition is met, game_running = false
    if curr_player == "X":
        x_turn()
        curr_player = "O"
    else: #current player is O
        o_turn()
        curr_player = "X"