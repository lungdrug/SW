##########
#
#   File:   rockPaperScissors.py
#   Author: pgOnline
#   Date:   January 2017
#   Notes:  A computerised version of Rock, Paper, Scissors
#           Version 2 - Added a loop and scores to play a longer game
#
##########

# Import the random library for generating a random number
import random

# A function to get the player's go
def playerGo():
    # Get the user's choice. Use .lower() to force lower case
    choice = input("Choose Rock, Paper or Scissors: ").lower()
    
    # validate user's choice and ask again if invalid
    while choice not in ("rock","paper","scissors"):
        print("Error - invalid choice")
        choice = input("Choose Rock, Paper or Scissors: ").lower()
        
    # return the choice back to the main program
    return choice

# A function to get the computer's go
def computerGo():
    # Generate a random number
    choice = random.randint(1,3)

    # Convert the random number to rock, paper or scissors
    if choice == 1:
        choice = "rock"
    elif choice == 2:
        choice = "paper"
    elif choice == 3:
        choice = "scissors"

    # return the choice back to the main program
    return choice

# MAIN PROGRAM

# Set lives at the start
playerLives = 3
computerLives = 3

# Keep going until someone is out of lives
while playerLives > 0 and computerLives > 0:
    # Call the functions to get the player and computer turns
    player = playerGo()
    computer = computerGo()

    # Display the two choices
    print("Player chose:" , player)
    print("Computer chose:" , computer)

    # Check if the player has won
    if (player == 'rock' and computer == 'scissors') \
       or (player == 'scissors' and computer == 'paper') \
       or (player == 'paper' and computer == 'rock'):
        print("Player wins!")
        computerLives = computerLives - 1
        
    # Check if the computer has won
    elif (player == 'rock' and computer == 'paper') \
       or (player == 'scissors' and computer == 'rock') \
       or (player == 'paper' and computer == 'scissors'):
        print("Computer wins :-(")
        playerLives = playerLives - 1
        
    # Otherwise it must be a draw
    else:
        print("Draw!")

    # Display remaining lives
    print("Player lives remaining:",playerLives)
    print("Computer lives remaining:",computerLives)

# End of loop

if playerLives == 0:
    print("You lose!")
else:
    print("You win!")
    
