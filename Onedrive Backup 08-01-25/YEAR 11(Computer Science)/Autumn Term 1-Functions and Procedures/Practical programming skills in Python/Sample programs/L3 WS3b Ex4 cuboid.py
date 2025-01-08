#Program L3 WS3b Ex4 cuboid.py


def getDimensions():
    height = int(input("Enter height of the cuboid: "))
    width = int(input("Enter width of the cuboid: "))
    depth = int(input("Enter depth of the cuboid: "))
    return height, width, depth

def calculateArea(height, width, depth):
    side1 = height * width
    side2 = width * depth
    side3 = height * depth
    totalArea = 2 * (side1 + side2 + side3)
    return totalArea

def calculateVol(height, width, depth):
    volume = height * width * depth
    return volume

def displayResults(area, volume):
    print("The cuboid has a total surface area of", area)
    print("and a volume of", volume)


# MAIN PROGRAM

height, width, depth = getDimensions()
area = calculateArea(height, width, depth)
volume = calculateVol(height, width, depth)
displayResults(area, volume)
