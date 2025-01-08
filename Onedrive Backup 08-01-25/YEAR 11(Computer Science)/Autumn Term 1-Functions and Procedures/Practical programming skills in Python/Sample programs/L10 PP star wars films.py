#Program name: L10 PP star wars films.py

validAnswers = ["a new hope","the empire strikes back","return of the jedi"]
film = input("Enter the title of your favourite Star Wars film: ")
film = film.lower()  #convert user input to lowercase
while film not in validAnswers:
      print("Invalid, film must be from the original trilogy.")
      film = input("Enter the title of your favourite Star Wars film: ")

print ("OK, good choice!")
input("Press Enter to exit")
