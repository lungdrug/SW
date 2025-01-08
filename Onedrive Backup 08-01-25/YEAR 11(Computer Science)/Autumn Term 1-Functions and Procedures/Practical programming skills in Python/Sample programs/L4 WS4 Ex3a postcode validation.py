#Program name: L4 WS4 Ex3a postcode validation.py
#Worksheet 4 Qu 3: Program tests postcodes according to the rule,
#starts with 1 or 2 capital letters and 1 or 2 numbers,
#followed by a space and one number followed by 2 letters
import re

print ("Test as many postcodes as you like.. press Enter to end.")
anotherGo = True
while anotherGo:
    postcode = input("Please input your postcode: ")
    valid = re.match("[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z][A-Z]",postcode)
    if len(postcode)==0:
        anotherGo=False
    else:
        if valid:
            print("valid postcode")
        else:
            print("invalid postcode")
