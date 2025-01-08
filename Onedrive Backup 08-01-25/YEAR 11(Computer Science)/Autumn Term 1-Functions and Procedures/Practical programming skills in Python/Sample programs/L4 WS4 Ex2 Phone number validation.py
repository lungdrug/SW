#Program name: L4 WS4 Ex2 Phone number validation.py

import re
pattern1 = "(01[0-9][0-9][0-9]) [0-9]{6}"
pattern2 = "(01[0-9]1) [0-9]{3} [0-9]{4}"
pattern3 = "(011[0-9]) [0-9]{3} [0-9]{4}"
pattern4 = "(02[0-9]) [0-9]{4} [0-9]{4}"

print ("Test as many phone numbers as you like.. press Enter to end.")
anotherGo = True
while anotherGo:
    phonenumber = input("Please input your phone number (spaces but no brackets): ")
    if len(phonenumber)==0:
        anotherGo=False
    else:
        if re.match(pattern1, phonenumber):
            print("valid phone number")
        elif re.match(pattern2, phonenumber):
                print("valid phone number")
        elif re.match(pattern3, phonenumber):
            print("valid phone number")
        elif re.match(pattern4, phonenumber):
            print("valid phone number")
        else:
            print("invalid phone number")
