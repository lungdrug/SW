#Program L8 WS8 Ex5 read and write classmates.py
classFile = open("classmates.txt", "w")
name = input("Enter the name of a friend: ")

#using the method "upper" converts the user entry to uppercase
#so even if they enter "stop" it will be recognised
while name.upper() != "STOP":
    band = input("Enter their favourite band: ")
    food = input("Enter their favourite food: ")
    classFile.write(name + "," + band + "," + food + "\n")
    name = input("Enter the name of a friend: ")
classFile.close()
classFile = open("classmates.txt","r")

for line in classFile:
    print(line)
#   or alternatively you could split into individual fields
#    line = classFile.readline()
#    data = line.split(",")
#    print(data[0],data[1],data[2])
classFile.close()


