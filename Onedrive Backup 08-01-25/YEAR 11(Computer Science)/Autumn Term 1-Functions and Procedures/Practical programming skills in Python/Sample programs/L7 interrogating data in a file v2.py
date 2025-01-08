#Program name: L7 interrogating data in a file v2.py

file = open("people2.txt", "r")
for loop in range (9):
    line = file.readline()
    data = line.split(",")
    if data[2] == "Musician":
        print(data[0],data[1])
file.close()
