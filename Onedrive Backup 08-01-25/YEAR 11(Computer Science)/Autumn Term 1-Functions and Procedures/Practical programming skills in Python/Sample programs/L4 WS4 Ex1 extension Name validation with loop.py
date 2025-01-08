#Program name: L4 WS4 Ex1 extension Name validation with loop.py

import re
name = input("Enter your name: ")
valid = re.match("[A-Z]", name)

while not valid:
   print("Invalid, no capital")
   name = input("Please re-enter your name: ")
   valid = re.match("[A-Z]", name)
print ("That looks OK")
