#Program name: L4 WS4 Ex1 Name validation.py

import re
name = input("Enter your name: ")
valid = re.match("[A-Z]", name)
if valid:
    print("That looks OK")
else:
    print("Invalid, no capital")

