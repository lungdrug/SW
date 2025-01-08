#L1 WS1 Ex1.py
target = 12
guess = 1
userChoice = int(input("Guess the number: "))
while userChoice != target:
    guess = guess + 1
    if userChoice < target:
        print("Guess higher!")
    else:
        print("Guess lower!")
    userChoice = int(input("Guess the number: "))
print("It took you" , guess, "guesses")

