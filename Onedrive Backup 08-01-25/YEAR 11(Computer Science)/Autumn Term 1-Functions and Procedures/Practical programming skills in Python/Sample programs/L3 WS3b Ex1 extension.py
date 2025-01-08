#Program L3 WS3b Ex1 extension.py

def menu():
    print("MAIN MENU")
    print("1. Convert miles to km")
    print("2. Convert feet to metres")
    print("0. Quit")
    choice = int(input("Enter a choice: "))
    if choice == 0:
        exit()
    elif choice == 1:
        milesToKm()
    elif choice == 2:
        feetToM()
    else:
        print("Error, invalid")


def milesToKm():
    miles = int(input("How many miles? "))
    km = miles * 1.6093
    print(miles, "miles =", round(km,2), "km")

def feetToM():
    feet = int(input("How many feet? "))
    metres = feet * 0.3048
    print(feet, "ft =", round(metres,2), "m")

# MAIN PROGRAM

while True:
    menu()

