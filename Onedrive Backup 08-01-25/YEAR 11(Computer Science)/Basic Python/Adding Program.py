#Adder
print("Keeping a running total")
print("***********************")
print("Enter numbers to add together then press 0 to exit")

#Initalise the Variables
count=0
runningTotal=0
number=int(input("Input the first number:  "))

#Add each number until 0 is entered

while number !=0:
    count = count + 1
    runningTotal= runningTotal + number
    number = int(input("Input next number (0 to finish) :  "))

#Display the total sum and the numbers of entries made
print("You entered   ",count, "numbers")
print("Total =  ", runningTotal)

input("Press ENTER to exit")
