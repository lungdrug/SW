#Program name: L7 WS7b Task 1 Albums.py
file = open("albums.txt", "r")
line = file.readline()
file.close()
data = line.split(",")
print("Artist: ",data[0])
print("Title: ",data[1])
print("Year:",data[2])
print("Genre:",data[3])
print("Sales: ",data[4])

# program prints just the artist and album name
# from the third line of the data file
print("\n2(b) Prints just the artist and album name from the third line of the data file")
file = open("albums.txt", "r")
line = file.readline()
line = file.readline()
line = file.readline()
file.close()
data = line.split(",")
print("Artist: ",data[0])
print("Album: ",data[1])

# program prints out names of all the Rock albums

print("\n2c Prints out the names of all the Rock albums")
file = open("albums.txt", "r")
for loop in range(15):
   line = file.readline()
   data = line.split(",")
   if data[3] == "Rock":
      print(data[1])
file.close()

# 2d Print out the Title and Year for each album by the Eagles

print ("\n2d Print out the Title and Year for each album by the Eagles")
file = open("albums.txt", "r")
for loop in range(15):
   line = file.readline()
   data = line.split(",")
   if data[0] == "Eagles":
      print(data[1],data[2])
file.close()

# 2e Print the Title and Total Sales for each album if it is either Country or Soundtrack.
print("\n2e Print the Title and Total Sales for each album if it is either Country or Soundtrack")
file = open("albums.txt", "r")
for loop in range(15):
   line = file.readline()
   data = line.split(",")
   if data[3] == "Country" or data[3] == "Soundtrack":
      print(data[1],data[4])
file.close()

#2f Add up the total sales for all 15 albums
total = 0
file = open("albums.txt", "r")
for loop in range(15):
   line = file.readline()
   data = line.split(",")
   total = total + float(data[4])
file.close()
print("\nTotal Sales for all albums: £",total, "million")


