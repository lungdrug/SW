##########
#
#   File:   pythag.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for solving Pythagoras problems
#           Version 3 - Added a menu
#
##########

# Procedure to find the long side of a right angled triangle
def findHypotenuse():
    # Get the two short sides
    sideOne = float(input("Enter the length of side A: "))
    sideTwo = float(input("Enter the length of side B: "))
    # Add the squares of the two short sides, then square root
    hypotenuse = (sideOne ** 2 + sideTwo ** 2) ** (1/2)
    print("The hypotenuse is: " + str(hypotenuse))

# Procedure to find a short side of a right angled triangle
def findSide():
    # Get the known short side an the hypotenuse
    sideOne = float(input("Enter the length of side A: "))
    hypotenuse = float(input("Enter the length of the hypotenuse: "))
    # Calculate the length of the missing side
    sideTwo = (hypotenuse ** 2 - sideOne ** 2) ** (1/2)
    print("The missing side is is: " + str(sideTwo))

# Procedure to display the menu
def displayMenu():
    print("")
    print("==========")
    print("Pythagoras Problem Sovler")
    print("")
    print("1. Find the hypotenuse")
    print("2. Find a short side")
    print("0. Quit")
    print("")

# MAIN PROGRAM

# Set the choice so that the while loop will run
choice = ""

# Repeat until the user chooses 0
while choice != 0:
    # Display menu and validate the user's choice
    displayMenu()
    choice = int(input("Choose an option: "))
    while choice not in (0, 1, 2):
        print("Invalid option")
        displayMenu()
        choice = int(input("Choose an option: "))

    # Run the procedure chosen by the user
    if choice == 1:
        findHypotenuse()
    elif choice == 2:
        findSide()
