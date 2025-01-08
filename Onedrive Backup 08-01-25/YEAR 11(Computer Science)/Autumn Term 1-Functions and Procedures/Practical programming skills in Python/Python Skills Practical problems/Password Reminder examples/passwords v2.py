##########
#
#   File:   passwords.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for storing passwords for online accounts
#           Version 2 - Added procedure to store account details
#
##########

# Procedure to encrypt a password
def encrypt():
    # Declare an empty string for the encrypted message
    ciphertext = ""

    # Get the original message from the user and make it lower case
    password = input("Enter your password: ")

    # Set the key, based on the length of the password
    key = len(password) % 26

    # Convert each letter
    for letter in password:
        # If the letter is between a and z then shift it
        if ord(letter) > 96 and ord(letter) < 123:
            # Get the ASCII value and take 97 (so a = 0 and z = 25)
            # Then add the key
            value = ord(letter) - 97 + key
            # Modulo makes the alphabet wrap around
            # Then add 97 to get the ASCII value
            value = value % 26 + 97
            # convert back to the ASCII character and add to ciphertext
            ciphertext = ciphertext + chr(value)
        elif ord(letter) > 64 and ord(letter) < 91:
            # Get the ASCII value and take 65 (so a = 0 and z = 25)
            # Then add the key
            value = ord(letter) - 65 + key
            # Modulo makes the alphabet wrap around
            # Then add 97 to get the ASCII value
            value = value % 26 + 65
            # convert back to the ASCII character and add to ciphertext
            ciphertext = ciphertext + chr(value)
        else:
            # If the character is not a letter, then don't shift it
            ciphertext = ciphertext + letter
    # Return the completed ciphertext
    return ciphertext

# Procedure to store the details in a file
def addPassword():
    # Open passwords.txt in append mode so that new details are added
    # at the end of the file without deleting previous data
    file = open("passwords.txt","a")

    # Get the account and username
    account = input("Enter the name of the account you wish to add: ")
    username = input("Enter your username for " + account + ": ")

    # Get the password and encrypt it
    encryptedPassword = encrypt()

    # Add the data to the file
    file.write(account + "," + username + "," + encryptedPassword + "\n")

    # Close the file
    file.close()
    
        

# MAIN PROGRAM

addPassword()

