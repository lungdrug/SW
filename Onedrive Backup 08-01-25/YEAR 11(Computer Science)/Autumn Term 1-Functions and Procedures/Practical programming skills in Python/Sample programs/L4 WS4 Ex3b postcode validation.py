#Program name: L4 WS4 Ex3b postcode validation
#Worksheet 4 Qu 3b: Program tests postcodes according to the rule,
#"starts with 2 capital letters then a number"
import re

print ("Test as many postcodes as you like.. press Enter to end.")
anotherGo = True
while anotherGo:
    postcode = input("Please input your postcode: ")
    valid = re.match("[A-Z][A-Z][0-9]",postcode)
    if len(postcode)==0:
        anotherGo=False
    else:
        if valid:
            print("valid postcode")
        else:
            print("invalid postcode")
#
