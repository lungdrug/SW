#Program name: L4 WS4 Ex4 postcode validation.py
import re
pattern =  '[A-Z]([A-Z](\d{1,2}|\d[A-Z])|\d{1,2}|\d[A-Z])\s\d[A-Z]{2}'


print ("Test as many postcodes as you like.. press Enter to end.")
anotherGo = "y"
while anotherGo == "y":
    postcode = input("Please input your postcode: ")
    if len(postcode)==0:
        anotherGo=False
    else:
        if re.match(pattern, postcode):
            print("valid postcode")
        else:
            print("invalid postcode")
    anotherGo = input ("Another go? (y or n): ")
    
        
