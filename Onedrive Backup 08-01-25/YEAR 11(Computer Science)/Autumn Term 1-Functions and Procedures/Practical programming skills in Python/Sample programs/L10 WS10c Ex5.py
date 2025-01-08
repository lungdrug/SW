#Program name: L10 WS10c Ex5.py
def add(numOne,numTwo):
      result = numOne + numTwo
      print("The result of adding is", result)

def sub(numOne,numTwo):
      result = numOne - numTwo
      print("The result of subtracting is", result)

def div(numOne,numTwo):
      result = numOne / numTwo
      print("The result of dividing is", result)

def mult(numOne,numTwo):
      result = numOne * numTwo
      print("The result of multiplying is", result)

choice = 9
while choice != 0:
      print("Do you want to:")
      print("1. Add two numbers")
      print("2. Subtract two numbers")
      print("3. Divide two numbers")
      print("4. Multiply two numbers")
      print("0. Quit")
      choice = int(input("Enter your choice: "))
      while choice not in (0,1,2,3,4):
            print("Invalid choice. Choose 1-4 or 0 to quit.")
            choice = int(input("Enter your choice: "))
      if choice != 0:
          numOne = int(input("Enter the first number: "))
          numTwo = int(input("Enter the second number: "))
          if choice == 1:
                add(numOne,numTwo)
          elif choice == 2:
                sub(numOne,numTwo)
          elif choice == 3:
                div(numOne,numTwo)
          elif choice == 4:
                mult(numOne,numTwo)

input("Press Enter to exit: ")
