#Program name: L9 WS9b Ex4.py
filmRatings = [ [ "Lion" , 9.7 , 7.8 , 9.5 ] ]
filmRatings.append( ["Transformers" , 3.7 , 6.8 , 5.2] )
filmRatings.append( ["Pirates of the Caribbean" , 6.1 , 4.9 , 7.3] )
filmRatings.append( ["Moana" , 8.2 , 7.9 , 6.7] )
filmRatings.append( ["War Games" , 7.3 , 8.1 , 7.7] )

total = 0
for count in range(1,len(filmRatings[0])):
    total = total + filmRatings[0][count]
    print("Running total",total)
average = total / len(filmRatings[0])
print ("Total",total)
print("Average rating for Lion:",round(average,2))

input("\nPress Enter to exit ")
