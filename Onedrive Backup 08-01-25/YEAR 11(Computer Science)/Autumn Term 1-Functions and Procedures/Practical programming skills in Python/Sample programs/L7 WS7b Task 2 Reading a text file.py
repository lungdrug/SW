#Program L7 WS7b Task 2 Reading a text file.py
#print all the records
#when you don't know how many lines there are
print("\nPrint all the records in the list")
peoplelist = open("people.txt", "r")
for line in peoplelist:
    print(line)
peoplelist.close()

#reading a textfile into a list
#when you don't know how many lines there are
print("\nRead files into a list first, then find the number of recs in the list")
print("Then print just their surnames")
file = open("people.txt", "r")
lines = file.readlines()
#lines now refers to a list
#with each element of the list holding one record

#Find the number of lines in the list
numberOfRecs = len(lines)
print("There are ",numberOfRecs," records in the list")
file.close()
#start at the beginning of the file again
#now you know how many records are in the list
file = open("people.txt", "r")
for n in range(numberOfRecs):
    line = file.readline()
    data = line.split(",")
    print(data[1])
file.close()

