##########
#
#   File:   bands.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for storing and displaying scores
#           Version 2 - Now collects and stores the scores for each band
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
        score = int(input("How many votes did " + line + " receive? "))
        # Add a list to the end of the bands list - creating a 2D list
        bands.append([line,score])
        # This line lets you see how the list is growing
        # It should be removed for the final version
        print(bands)

    # Delete the contents of bandScores.txt and write the new details
    file = open("bandScores.txt","w")
    # Add each item to a line - the band name and the score
    for item in bands:
        file.write(item[0] + "," + str(item[1]) + "\n")
    file.close()

# MAIN PROGRAM

getScores()


