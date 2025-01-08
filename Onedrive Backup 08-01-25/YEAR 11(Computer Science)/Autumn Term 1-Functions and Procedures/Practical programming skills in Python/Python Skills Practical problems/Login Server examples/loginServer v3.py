##########
#
#   File:   loginServer.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A simple login server program
#           Version 3 - Added new account creation
#
##########

# Import regular expression module for checking password strength
import re

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

# Procedure to display the menu
def displayMenu():
    print("==========")
    print("LOGIN SERVER")
    print("")
    print("1. Log In")
    print("2. Create New Account")
    print("")

# Procedure to add a new account
def newAccount():
    # Set flag to false so that the while loop will run
    unique = False

    # Keep asking for a new username until a unique one is entered
    while unique == False:
        # Set the flag to True so that we can change it if a match is found
        unique = True
        username = input("Choose a new username: ")
        file = open("users.txt","r")
        # Check file for a match. If there is one, set unique to False
        for line in file:
            data = line.split(",")
            if data[0] == username:
                unique = False
                break
        file.close()

        # display appropriate error message if needed, before looping back
        if unique == False:
            print("Sorry, that username is already taken.")

    # Set the flag to False so that the while loop will run
    strongPassword = False
    
    # Keep repeating until a strong password is entered
    while strongPassword == False:
        password = input("Choose a strong password: ")
        # Check if password contains a lower case, upper case and digit
        if re.search("[a-z]",password) and re.search("[A-Z]",password) \
           and re.search("[0-9]",password):
            strongPassword = True
        else:
            print("Sorry, your password is not strong enough")

    # Open file in append mode (so it will add to the end)
    file = open("users.txt","a")
    # Write the username and password to a file, adding a comma and newline
    file.write(username + "," + password + "\n")
    # Close the file
    file.close()

    print("New user account successfully added")
    

# MAIN PROGRAM

displayMenu()
choice = int(input("Enter a choice: "))
while choice != 1 and choice != 2:
    print("Error, invalid option")
    print("")
    displayMenu()
    choice = int(input("Enter a choice: "))

if choice == 1:
    checkLogin()
elif choice == 2:
    newAccount()
    
        
