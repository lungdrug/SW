##########
#
#   File:   bands.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for storing and displaying scores
#           Version 7 - Replaced the lambda function with a
#                       bubble sort to provide an alternative
#                       solution
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
    namefile = open("bandNames.txt","w")
    # Write each band to the file, with a newline character
    for item in bands:
        namefile.write(item + "\n")
    # Close the file
    namefile.close()

# Procedure to get scores for each band and save to a file
def getScores():
    # Declare an empty list
    bands = []

    # Open the bandNames file to get the band names
    namefile = open("bandNames.txt","r")
    # Ask for the score for each band in the file
    for line in namefile:
#        line = line.rstrip("\n")
        bandName = namefile.readline()
        score = int(input("How many votes did " + bandName + " receive? "))
        # Add a list to the end of the bands list - creating a 2D list
        bands.append([bandName,score])
        # This line lets you see how the list is growing

    # Delete the contents of bandScores.txt and write the new details
    bandScores = open("bandScores.txt","w")
    # Add each item to a line - the band name and the score
    for item in bands:
        bandScores.write(item[0] + "," + str(item[1]) + "\n")
    bandScores.close()

# Procedure to display all scores
def displayAllScores():
    # Open the file with band names and scores in read mode
    bandFile = open("bandScores.txt","r")
    # read first record
    bandScoresRec = bandFile.readline()
    while bandScoresRec != "":      #read up to end of file
        data = bandScoresRec.split(",")      # Split into a list of band / score
        bandName = data[0]    #Bandname is first field
        bandScore = data[1]
        print("Band: " + bandName + " | " + bandScore)
        bandScoresRec = bandFile.readline()
    
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
    bandNames = []
    bandScores = []
    # Open the file with band names and scores in read mode
    bandFile = open("bandScores.txt","r")
    # read first record
    bandScoresRec = bandFile.readline()
    #read rest of file, storing in two arrays bandNames and bandScores
    while bandScoresRec != "":      #read up to end of file
        data = bandScoresRec.split(",")      # Split into a list of band / score
        bandName = data[0]    #Bandname is first field
        bandScore = int(data[1])
        bandNames.append(bandName)
        bandScores.append(bandScore)
        bandScoresRec = bandFile.readline()
 
    # Sort the two arrays into ascending sequence using a bubble sort
    for i in range (10):
        for j in range (9-i):
            # If the two neighbouring values are in the wrong order, swap them
            if bandScores[j] > bandScores[j + 1]:
                # First swap the scores
                temp = bandScores[j]
                bandScores[j] = bandScores[j+1]
                bandScores[j+1] = temp
                # Then swap band names
                temp = bandNames[j]
                bandNames[j] = bandNames[j+1]
                bandNames[j+1] = temp


    # If top = True print the first three names
    if top == False:
        for i in range(3):
            print("Band: " + bandNames[i] + " | " + str(bandScores[i]) + " votes")
    else:
        for i in range(9,6, -1):
            print("Band: " + bandNames[i] + " | " + str(bandScores[i]) + " votes")

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

