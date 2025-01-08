#Program name: L5 WS5a Extension.py

# This is a string that goes over several lines

menu = "\nNOW SCREENING\n\
\n\
1. Reset list \n\
2. View entire list \n\
3. View one item \n\
4. Edit list \n\
5. Quit \n\
\n\
Enter a choice: "

films = ["Blank"]*6
choice = int(input(menu))

while choice != 5:

    # Choice 1 - Reset the list to all blanks
    
    if choice == 1:
        films = ["Blank"]*6
        print("List reset")

    # Choice 2 - Print the entire list
    
    elif choice == 2:
        print("List:")
        print(films)

    # Choice 3 - Print just one film (with some error handling)
    
    elif choice == 3:
        index = int(input("Which film do you want to view? (0-5): "))
        if index <= 5 and index >= 0:
            print(films[index])
        else:
            print("Error, you must choose a number between 0 and 5")

    # Choice 4 - Replace one item (with some error handling) 
    
    elif choice == 4:
        index = int(input("Which film do you want to change? (0-5): "))
        if index <= 5 and index >= 0:
            print("You are replacing film:",films[index])
            newFilm = input("What do you want to replace it with? ")
            films[index] = newFilm
            print("Films list updated")
        else:
            print("Error, you must choose a number between 0 and 5")

    # Choice 5 - Quit the program
    elif choice == 5:
        print("Goodbye!")

    # Error handling on the main menu
    
    else:
        print("Invalid number - you must pick between 1 and 5")

    # Ask for a new choice or you get stuck in a loop

    choice = int(input(menu))
