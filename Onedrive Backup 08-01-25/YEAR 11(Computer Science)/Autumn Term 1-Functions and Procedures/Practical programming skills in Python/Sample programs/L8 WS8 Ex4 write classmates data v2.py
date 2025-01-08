##Program name: L8 WS8 Ex4 write classmates data v2.py
##In this version, the newline character \n is in a field of its own.
##To find all the people whose favourite food was "chocolate"
##You would have to search for data[2] = "chocolate"

number = int(input("How many details do you want to store? "))
file = open("classmates2.txt", "w")
for loop in range(number):
    name = input("Enter the name of a friend: ")
    band = input("Enter their favourite band: ")
    food = input("Enter their favourite food: ")
    #notice the last comma, separating the field containing the newline character
    file.write(name + "," + band + "," + food +"," + "\n")
file.close()


file = open("classmates2.txt","r")
for loop in range(number):
    line = file.readline()
    data = line.split(",")
    print(data[0],data[1],data[2])
file.close()
