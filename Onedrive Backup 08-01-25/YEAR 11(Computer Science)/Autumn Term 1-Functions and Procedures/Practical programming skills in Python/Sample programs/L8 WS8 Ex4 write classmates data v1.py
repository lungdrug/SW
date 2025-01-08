#Program name: L8 WS8 Ex4 write classmates data v1.py
#In this version, the newline character \n is part of the last field, food.
#To find all the people whose favourite food was "chocolate",
#you would have to search for data[2] = "chocolate\n"

number = int(input("How many details do you want to store? "))
file = open("classmates.txt", "w")
for loop in range(number):
    name = input("Enter the name of a friend: ")
    band = input("Enter their favourite band: ")
    food = input("Enter their favourite food: ")
    file.write(name + "," + band + "," + food + "\n")
file.close()


file = open("classmates.txt","r")
for loop in range(number):
    line = file.readline()
    data = line.split(",")
    print(data[0],data[1],data[2])
file.close()
