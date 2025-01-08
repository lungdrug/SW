# L4 Email lowercase.py

import re
email=input("Enter your email address in lowercase characters: ")
# The next statement only checks that the first character is lowercase
valid = re.match("[a-z]",email)
if valid:
	print("That looks OK")
else:
	print("Erm, try again!")

