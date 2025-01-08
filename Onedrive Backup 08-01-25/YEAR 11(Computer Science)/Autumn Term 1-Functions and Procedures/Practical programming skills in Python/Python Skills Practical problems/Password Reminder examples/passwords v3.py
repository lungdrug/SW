##########
#
#   File:   passwords.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A program for storing passwords for online accounts
#           Version 3 - Added decryption procedure
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

# Procedure to encrypt a password
def decrypt(encryptedPassword):
    # Declare an empty string for the original password
    password = ""

    # Set the key, based on the length of the encrypted password
    key = len(encryptedPassword) % 26

    # Convert each letter
    for letter in encryptedPassword:
        # If the letter is between a and z then shift it
        if ord(letter) > 96 and ord(letter) < 123:
            # Get the ASCII value and take 97 (so a = 0 and z = 25)
            # Then subtract the key to reverse the encryption
            value = ord(letter) - 97 - key
            # Modulo makes the alphabet wrap around
            # Then add 97 to get the ASCII value
            value = value % 26 + 97
            # convert back to the ASCII character and add to ciphertext
            password = password + chr(value)
        elif ord(letter) > 64 and ord(letter) < 91:
            # Get the ASCII value and take 65 (so a = 0 and z = 25)
            # Then subtract the key to reverse the encryption
            value = ord(letter) - 65 - key
            # Modulo makes the alphabet wrap around
            # Then add 97 to get the ASCII value
            value = value % 26 + 65
            # convert back to the ASCII character and add to ciphertext
            password = password + chr(value)
        else:
            # If the character is not a letter, then don't shift it
            password = password + letter
    # Return the completed ciphertext
    return password

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
    

def displayPassword():
    # Set boolean flag to assume that the account details are not found
    found = False
    
    # Open passwords.txt in read mode
    file = open("passwords.txt","r")
    
    # Get the account and username
    account = input("Which account are you looking at?: ")
    username = input("Enter your username for " + account + ": ")

    # Check each line of the file
    for line in file:
        line = line.rstrip("\n")    # Remove the newline character
        data = line.split(",")      # Split the data into a list
        # Check if the account and username are in the file
        if account == data[0] and username == data[1]:
            # Decrpyt the password, print it and update the flag
            password = decrypt(data[2])
            print("Password: " + password)
            found = True
    file.close()

    # If the account and username aren't in the file then
    # display an error message for the user
    if found == False:
        print("Details do not match")

# MAIN PROGRAM


displayPassword()

