#Program L3 HW3 Guess number
import random

def getGuess():
    guess = 0
    while guess < 1 or guess > 100:
        guess = int(input("Enter a guess between 1 and 100: "))
    return guess

def displayRules():
    print("This is a guessing game.")
    print("You have to guess the number between 1 and 100 \
chosen by the computer")
          

def playGame(target):
    guessedNumber = False
    guess = getGuess()
    while guess != target:
        if guess > target:
            guess = int(input("Too high - guess lower: "))
        elif guess < target:
            guess = int(input("Too low - guess higher: "))
        else:
            guessedNumber = True
    print("\nThat's correct, well done!")
    return guessedNumber

#main
choice = "0" 
while choice != "3":
    print("\nMain Menu")
    print("1. Display the rules")
    print("2. Play the game")
    print("3. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        displayRules()
    elif choice == "2":
        guessedNumber = playGame(random.randint(1,100))         
    elif choice !="3":
        print("Invalid choice - must be between 1 and 3 ")
input("Goodbye ... press Enter to Quit program ")
            
    
