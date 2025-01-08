#Program name: L7 interrogating data in a file v1.py

file = open("people.txt", "r")
for loop in range (9):
    line = file.readline()
    data = line.split(",")
    if data[2] == "Musician\n":
        print(data[0],data[1])
file.close()
