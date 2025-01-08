##########
#
#   File:   bands.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for storing and displaying scores
#           Version 1 - Just collects band names and saves
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
        

# MAIN PROGRAM

getBandNames()
        

