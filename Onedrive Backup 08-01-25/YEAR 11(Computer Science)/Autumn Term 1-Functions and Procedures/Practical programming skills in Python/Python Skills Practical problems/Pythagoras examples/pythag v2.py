##########
#
#   File:   pythag.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for solving Pythagoras problems
#           Version 2 - Now finds a missing short side
#
##########

def findHypotenuse():
    sideOne = float(input("Enter the length of side A: "))
    sideTwo = float(input("Enter the length of side B: "))
    hypotenuse = (sideOne ** 2 + sideTwo ** 2) ** (1/2)
    print("The hypotenuse is: " + str(hypotenuse))

def findSide():
    sideOne = float(input("Enter the length of side A: "))
    hypotenuse = float(input("Enter the length of the hypotenuse: "))
    sideTwo = (hypotenuse ** 2 - sideOne ** 2) ** (1/2)
    print("The missing side is is: " + str(sideTwo))

findSide()
