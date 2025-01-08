#Program L8 WS8 Ex11.py
menu = "1. Display high scores\n\
2. Add a new high score\n\
3. Clear all high scores\n\
4. Quit"

choice = None

while choice != "4":
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
      file.write(name + "," + date + "," + score +  "\n")
      file.close()
      print("Score saved")
   elif choice == "3":
      file = open("highScores.txt", "w")
      file.close()
      print("Scores reset")
print("Goodbye!")
