##########
#
#   File:   bands.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for storing and displaying scores
#           Version 6 - Added a menu system
#                       Removed the extra print in getScores()
#
##########

# Procedure to get band names from the user and write to a file
def getBandNames():
    # Declare an empty list
    bands = []

    # Repeat 10 times (get 10 band names)
    for i in range(10):
        newBand = input("Enter the name of a band: ")
        # Validate by checking band name is not already stored
        while newBand in bands:
            print("Error, band already exists")
            newBand = input("Enter the name of a band: ")
        # Add the new band name to the list of bands
        bands.append(newBand)

    # Open bandNames.txt in write mode
    file = open("bandNames.txt","w")
    # Write each band to the file, with a newline character
    for item in bands:
        file.write(item + "\n")
    # Close the file
    file.close()

# Procedure to get scores for each band and save to a file
def getScores():
    # Declare an empty list
    bands = []

    # Open the bandNames file to get the band names
    file = open("bandNames.txt","r")
    # Ask for the score for each band in the file
    for line in file:
        line = line.rstrip("\n")
#        score = int(input("How many votes did " + line + " receive? "))
        # Add a list to the end of the bands list - creating a 2D list
        bands.append([line,score])
        # This line lets you see how the list is growing

    # Delete the contents of bandScores.txt and write the new details
    file = open("bandScores.txt","w")
    # Add each item to a line - the band name and the score
    for item in bands:
        file.write(item[0] + "," + str(item[1]) + "\n")
    file.close()

# Procedure to display all scores
def displayAllScores():
    # Open the file with band names and scores in read mode
    file = open("bandScores.txt","r")
    # Repeat for each line (each band)
    for line in file:
        line = line.rstrip("\n")    # Remove the newline character
        data = line.split(",")      # Split into a list of band / score
        print("Band: " + data[0] + " | " + data[1] + " votes")

def displayTotalVotes():
    # Set the total score to 0
    total = 0

    # Open the file with band names and scores in read mode
    file = open("bandScores.txt","r")
    # Repeat for each line (each band)
    for line in file:
        line = line.rstrip("\n")    # Remove the newline character
        data = line.split(",")      # Split into a list of band / score
        total = total + int(data[1])    # Add to the current total
    print("Total votes: " + str(total))

# Function takes a boolean value and displays either the
# top three or the bottom three scores
def displayThree(top):
    # Declare an empty list
    bands = []
    # Open the file with band names and scores in read mode
    file = open("bandScores.txt","r")
    # Repeat for each line (each band)
    for line in file:
        line = line.rstrip("\n")    # Remove the newline character
        data = line.split(",")      # Split into a list of band / score
        data[1] = int(data[1])      # Cast score to an int for sorting
        bands.append([data[0],data[1]])

    # If top = True then sort the highest scores to the top
    # Otherwise sort the lowest scores to the top
    if top == True:
        # Sort the list on the data[1] field - in reverse order (descending)
        bands = sorted(bands,key=lambda data:data[1], reverse=True)
        print("Top 3 bands")
    else:
        # Sort the list on the data[1] field - in order (ascending)
        bands = sorted(bands,key=lambda data:data[1])
        print("Bottom 3 bands")

    # Only do this for the top three
    for i in range(3):
        # Print out the band name and scores from the 2D list
        print("Band: " + bands[i][0] + " | " + str(bands[i][1]) + " votes")

# Procedure to display a menu
def displayMenu():
    print("")
    print("==========")
    print("BATTLE OF THE BANDS!")
    print("")
    print("1. Start a new list of bands")
    print("2. Add scores for each band")
    print("3. Print all scores")
    print("4. Print total votes")
    print("5. Print top 3 bands")
    print("6. Print bottom 3 bands")
    print("0. Quit")

# MAIN PROGRAM

# Set a choice that will cause the loop to run
choice = 9

# Repeat until the user enters 0
while choice != 0:
    # Display the menu and get the choice
    displayMenu()
    choice = int(input("Enter your choice: "))
    # Validate the choice is in the list of options
    while choice not in (1, 2, 3, 4, 5, 6, 0):
        print("Invalid choice")
        displayMenu()
        choice = int(input("Enter your choice: "))

    # Call the appropriate procedure
    if choice == 1:
        getBandNames()
    elif choice == 2:
        getScores()
    elif choice == 3:
        displayAllScores()
    elif choice == 4:
        displayTotalVotes()
    elif choice == 5:
        displayThree(True)
    elif choice == 6:
        displayThree(False)
    else:
        print("Goodbye!")

