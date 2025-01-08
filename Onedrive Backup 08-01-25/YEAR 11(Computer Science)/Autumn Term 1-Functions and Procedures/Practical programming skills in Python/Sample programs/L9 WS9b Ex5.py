# Program L9 WS9b Ex5.py

filmRatings = [ [ "Lion" , 9.7 , 7.8 , 9.5 ] ]
filmRatings.append( ["Transformers" , 3.7 , 6.8 , 5.2] )
filmRatings.append( ["Pirates of the Caribbean" , 6.1 , 4.9 , 7.3] )
filmRatings.append( ["Moana" , 8.2 , 7.9 , 6.7] )
filmRatings.append( ["War Games" , 7.3 , 8.1 , 7.7] )
total = 0
reviewer = int(input("Enter the reviewer number (1-3): "))
for count in range(len(filmRatings)):
    total = total + filmRatings[count][reviewer]
average = total / len(filmRatings)
print("Average for reviewer " + str(reviewer) + " is " \
          + str(round(average,2)))

input("\nPress Enter to exit ")
