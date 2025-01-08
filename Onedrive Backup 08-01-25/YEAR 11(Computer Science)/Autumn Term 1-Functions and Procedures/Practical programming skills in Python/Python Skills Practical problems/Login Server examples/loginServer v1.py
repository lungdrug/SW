##########
#
#   File:   loginServer.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A simple login server program
#           Version 1 - Only deals with login process
#
##########

# A function to check login details
def checkLogin():
    # Set a flag to see if the username was found
    userFound = False

    # Get the username from the user
    user = input("Enter your username: ")

    # Check the file to see if the username is found
    file = open("users.txt","r")
    # Read in each line
    for line in file:
        # Remove the newline character at the end of each line
        line = line.rstrip("\n")
        # Split into a list of data values
        data = line.split(",")
        # Check is username matches
        if data[0] == user:
            # Update flag and break out of loop
            userFound = True
            break
    # Close the file
    file.close()

    # Check the same record to see if the password matches
    password = input("Enter your password: ")
    if userFound == True and data[1] == password:
        print("Logged in")
    else:
        print("Error, username or password incorrect")

# MAIN PROGRAM

checkLogin()
    
        
