#Program name: L3 WS3a tic_tac_toe with loop.py
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

def getPlayerChoice(grid):
    grid, valid = validateChoice(grid)
    while valid == False:
        print("Error, that position is already taken")
        grid, valid = validateChoice(grid)
    return grid

def validateChoice(grid):
    valid = False
    print("\nChoose your position (1-9)")
    choice = int(input())
    while choice < 1 or choice > 9:
        print("Error, must be 1-9. Try again")
        choice = int(input())
    if grid[choice-1] == "?":
        grid[choice-1] = "O"
        valid = True
    return grid, valid

def cpuChoice(grid):
    cpuChoice = random.randint(1,9)
    while grid[cpuChoice-1] != "?":
        cpuChoice = random.randint(1,9)
    grid[cpuChoice-1] = "X"
    return grid

def checkWinner(grid):
    winnerFound = False
    symbol = "?"
    if grid[0] == grid[1] == grid[2] != "?":
        winnerFound = True
        symbol = grid[0]
    elif grid[3] == grid[4] == grid[5] != "?":
        winnerFound = True
        symbol = grid[3]
    elif grid[6] == grid[7] == grid[8] != "?":
        winnerFound = True
        symbol = grid[6]
    elif grid[0] == grid[3] == grid[6] != "?":
        winnerFound = True
        symbol = grid[0]
    elif grid[1] == grid[4] == grid[7] != "?":
        winnerFound = True
        symbol = grid[1]
    elif grid[2] == grid[5] == grid[8] != "?":
        winnerFound = True
        symbol = grid[2]
    elif grid[0] == grid[4] == grid[8] != "?":
        winnerFound = True
        symbol = grid[0]
    elif grid[2] == grid[4] == grid[6] != "?":
        winnerFound = True
        symbol = grid[2]
    return winnerFound, symbol
        

def displayWinner(grid, symbol):
    displayGrid(grid)
    if symbol == "O":
        print("\nPlayer wins!")
    else:
        print("\nCPU wins :-(")
    
    

# MAIN PROGRAM

grid = ["?"]*9
winnerFound = False
placesTaken = 0

# While loop to repeat until either a winner is found
# or all 9 places are taken
while winnerFound == False and placesTaken < 9:
    
# Player Go

    displayGrid(grid)
    grid = getPlayerChoice(grid)
    placesTaken += 1
    winnerFound, symbol = checkWinner(grid)
 
    if winnerFound :
        displayWinner(grid, symbol)
    else:
        if placesTaken == 9:
            print ("\nIt's a draw!")

# Computer go
    if placesTaken < 9:
        displayGrid(grid)
        grid = cpuChoice(grid)
        placesTaken += 1
        winnerFound, symbol = checkWinner(grid)
        
        if winnerFound:
            displayWinner(grid, symbol)

input("\nPress enter to exit")
