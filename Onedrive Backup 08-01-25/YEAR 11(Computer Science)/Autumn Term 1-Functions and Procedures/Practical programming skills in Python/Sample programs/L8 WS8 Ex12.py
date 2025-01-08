#Program L8 WS8 Ex12.py

menu = "1. Display high scores\n\
2. Add a new high score\n\
3. Clear all high scores\n\
4. Display the highest high score\n\
5. Quit"

choice = None

while choice != "5":
    print(menu)
    choice = input("Enter choice: ")
    if choice == "1":
        file = open("highScores.txt", "r")
        contents = file.read()
        print(contents)
        file.close()
    elif choice == "2":
        file = open("highScores.txt", "a")
        name = input("Enter name: ")
        date = input("Enter date: ")
        score = input("Enter score: ")
        file.write(name + "," + date + "," + score + "\n")
        file.close()
        print("Score saved")
    elif choice == "3":
        file = open("highScores.txt", "w")
        file.close()
        print("Scores reset")
    elif choice == "4":
        file = open("highScores.txt", "r")
        maxScore = 0
        maxName = ""
        for line in file:
            data = line.split(",")
            highScore = data[2]
            if int(highScore) > int(maxScore):
                maxScore = highScore
                maxName = data[0]
        file.close()
        print("Highest high score is", maxName, maxScore)

print("Goodbye!")
