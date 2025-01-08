#Program L3 WS3b Ex2.py

def milesToKm():
	miles = int(input("\nHow many miles? "))
	km = round(miles * 1.6093,2)
	return km, "km"

def feetToM():
	feet = int(input("\nHow many feet? "))
	metres = round(feet * 0.3048,2)
	return metres, "m"

# MAIN PROGRAM

value, unit = milesToKm()
print("Conversion =", str(value)+unit)

value, unit = feetToM()
print("Conversion =", str(value)+unit)
input("\nPress Enter to exit ")