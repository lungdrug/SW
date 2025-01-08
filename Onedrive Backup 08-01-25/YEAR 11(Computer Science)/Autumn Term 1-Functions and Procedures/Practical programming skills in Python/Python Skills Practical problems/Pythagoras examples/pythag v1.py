##########
#
#   File:   pythag.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for solving Pythagoras problems
#           Version 1 - Only deals with finding the hypotenuse
#
##########

def findHypotenuse():
    sideOne = float(input("Enter the length of side A: "))
    sideTwo = float(input("Enter the length of side B: "))
    hypotenuse = (sideOne ** 2 + sideTwo ** 2) ** (1/2)
    print("The hypotenuse is: " + str(hypotenuse))

findHypotenuse()
