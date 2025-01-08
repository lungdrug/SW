#Program name: L7 HW7 Ex4 read file.py
dateFile = open("dates.txt", "r")
for dateRec in dateFile:
    data = dateRec.split("/")
    print("Day:" , data[0])
    print("Month:" , data[1])
    print("Year:" , data[2])
dateFile.close()                          
