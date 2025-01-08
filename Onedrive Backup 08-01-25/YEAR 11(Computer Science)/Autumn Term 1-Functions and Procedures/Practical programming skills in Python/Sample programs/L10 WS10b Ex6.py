#Program L10 WS10b Ex6.py
#validates a car registration number
import re
reg = input("Enter a registration number in the format AA11 AAA: ")
while not re.match("[A-Z]{2}[0-9]{2} [A-Z]{3}",reg):
      print("Invalid, try again!")
      reg = input("Enter a registration number: ")
print("Number accepted")