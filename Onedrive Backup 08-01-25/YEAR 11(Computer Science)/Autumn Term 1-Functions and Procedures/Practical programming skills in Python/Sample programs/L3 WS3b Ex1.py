#Program L3 WS3b Ex1.py

def milesToKm():
	miles = int(input("How many miles? "))
	km = miles * 1.6093
	print(miles, "miles =", round(km,2), "km")

def feetToM():
	feet = int(input("How many feet? "))
	metres = feet * 0.3048
	print(feet, "ft =", round(metres,2), "m")

# MAIN PROGRAM
milesToKm()
feetToM()
