#Program name: L5 WS5b Extension.py 

# Create a blank 2D list that, when full, will look like this:
# [ [Film0,Film1,Film2,Film3,Film4] , [Dir0,Dir1,Dir2,Dir3,Dir4] ]
# Film3 is in DVDs[0][3]
# Dir3 is in DVDs[1][3]

DVDs = [["Blank"]*5,["Blank"]*5]

# Loop round 5 times and ask for a film and a director - then store them
for loop in range(5):
    film = input("Enter the name of a film: ")
    director = input("Who is the director of that film? ")
    DVDs[0][loop] = film
    DVDs[1][loop] = director

# Print out populated list to check
#print(DVDs)

# Ask for a film to search for
choice = input("What film do you want to search for? ")

# If the film is in the first list then print out the details
if choice in DVDs[0]:
    position = DVDs[0].index(choice)
    print(DVDs[0][position],"was directed by",DVDs[1][position])
else:
    print("Sorry",choice,"is not in the databse")
