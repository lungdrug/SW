#Program name: L7 WS7a Reading a text file.py

# Question 1
famousPeople = open("people.txt", "r")
line = famousPeople.readline()
print("\nQuestion 1")
line = famousPeople.readline()
print(line)
famousPeople.close()

# Question 2
famousPeople = open("people.txt", "r")
for counter in range(6):
    line = famousPeople.readline()
famousPeople.close()
print("\nQuestion 2")
print(line)

#question 3
famousPeople = open("people.txt", "r")
print("\nQuestion 3")
for counter in range(9):
    line = famousPeople.readline()
    print(line)
famousPeople.close()

#question 4
famousPeople = open("people.txt", "r")
print("\nQuestion 4")
for counter in range(5):

    line = famousPeople.readline()

famousPeople.close()
print(line)

