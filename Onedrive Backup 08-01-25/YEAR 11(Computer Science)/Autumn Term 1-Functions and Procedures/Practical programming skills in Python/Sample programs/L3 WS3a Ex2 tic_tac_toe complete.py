#Program name: L3 WS3 Ex 2 tic-tac-toe complete.py

import random

def displayGrid(grid):
    print("")
    print("Current Grid")
    print("")
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print("-----")
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print("-----")
    print(grid[6] + "|" + grid[7] + "|" + grid[8])

def getChoice(grid):
    grid, valid = userChoice(grid)
    while valid == False:
        print("Error, that position is already taken")
        grid, valid = userChoice(grid)
    return grid

def userChoice(grid):
    valid = False
    print("Choose your position (1-9)")
    choice = int(input())
    while choice < 1 or choice > 9:
        print("Error, must be 1-9. Try again")
        choice = int(input())
    if grid[choice-1] == "?":
        grid[choice-1] = "O"
        valid = True
    return grid, valid

def getPlayer2(grid):
    grid, valid = userChoice2(grid)
    while valid == False:
        print("Error, that position is already taken")
        grid, valid = userChoice2(grid)
    return grid

def userChoice2(grid):
    valid = False
    print("Choose your position (1-9)")
    choice = int(input())
    while choice < 1 or choice > 9:
        print("Error, must be 1-9. Try again")
        choice = int(input())
    if grid[choice-1] == "?":
        grid[choice-1] = "X"
        valid = True
    return grid, valid

def cpuChoice(grid):
    cpuChoice = random.randint(1,9)
    while grid[cpuChoice-1] != "?":
        cpuChoice = random.randint(1,9)
    grid[cpuChoice-1] = "X"
    return grid

def checkWinner(grid):
    if grid[0] == grid[1] == grid[2] != "?":
        displayWinner(grid, 0)
    elif grid[3] == grid[4] == grid[5] != "?":
        displayWinner(grid, 3)
    elif grid[6] == grid[7] == grid[8] != "?":
        displayWinner(grid, 6)
    elif grid[0] == grid[3] == grid[6] != "?":
        displayWinner(grid, 0)
    elif grid[1] == grid[4] == grid[7] != "?":
        displayWinner(grid, 1)
    elif grid[2] == grid[5] == grid[8] != "?":
        displayWinner(grid, 2)
    elif grid[0] == grid[4] == grid[8] != "?":
        displayWinner(grid, 0)
    elif grid[2] == grid[4] == grid[6] != "?":
        displayWinner(grid, 2)

def displayWinner(grid, position):
    displayGrid(grid)
    if grid[position] == "O":
        print("Player wins!")
    else:
        print("CPU wins :-(")
    
    input("Press enter to exit")
#The next statement stops execution of the program
    exit()

# MAIN PROGRAM

grid = ["?"]*9

# MAIN PROGRAM
# uncomment the lines below and repeat them as many times as you need to

# The solution here would benefit from the use of a loop
# Note that there needs to be 9 goes in total
#   - so you can't simply repeat the first two blocks

# Player Go
displayGrid(grid)
grid = getChoice(grid)
checkWinner(grid)

# Computer Go
displayGrid(grid)
grid = cpuChoice(grid)
checkWinner(grid)

# Player Go
displayGrid(grid)
grid = getChoice(grid)
checkWinner(grid)

# Computer Go
displayGrid(grid)
grid = cpuChoice(grid)
checkWinner(grid)

# Player Go
displayGrid(grid)
grid = getChoice(grid)
checkWinner(grid)

# Computer Go
displayGrid(grid)
grid = cpuChoice(grid)
checkWinner(grid)

# Player Go
displayGrid(grid)
grid = getChoice(grid)
checkWinner(grid)

# Computer Go
displayGrid(grid)
grid = cpuChoice(grid)
checkWinner(grid)

# Player Go
displayGrid(grid)
grid = getChoice(grid)
checkWinner(grid)

