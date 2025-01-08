#Program name: L7 HW7 Ex3 dates.py

file = open("dates.txt", "r")
for counter in range(4):
   line = file.readline()
   data = line.split("/")
   print("Day:" , data[0])
   print("Month:" , data[1])
   print("Year:" , data[2])
file.close()
