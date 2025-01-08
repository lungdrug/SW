#Program L3 WS3b Ex3.py

def getRadius():
    radius = int(input("Enter radius of circle: "))
    return radius

def calculateCircumference(radius, pi):
    circ = 2 * pi * radius
    return circ

def calculateArea(radius, pi):
    area = pi * radius * radius
    return area

def displayResults(radius, circ, area):
    print("A circle of radius", radius)
    print("has a circumference of", circ)
    print("and an area of", area)

# MAIN PROGRAM

pi = 3.142
radius = getRadius()
circ = calculateCircumference(radius, pi)
area = calculateArea(radius, pi)
displayResults(radius, circ, area)
