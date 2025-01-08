# L4 Email full.py
# Validation for an email address using more complicated regular expressions
# Checks an email must have:
# - an @ symbol and a full stop
# - at least one character before and after the @ symbol
# - at least one character after the full stop

import re
email=input("Enter your email address: ")
valid = re.match("[\.\w]{1,}[@]\w+[.]\w+",email)

while not valid:
        print("Invalid address!")
        email=input("Enter your email address: ")
        valid = re.match("[\.\w]{1,}[@]\w+[.]\w+",email)
print("Valid email address")

