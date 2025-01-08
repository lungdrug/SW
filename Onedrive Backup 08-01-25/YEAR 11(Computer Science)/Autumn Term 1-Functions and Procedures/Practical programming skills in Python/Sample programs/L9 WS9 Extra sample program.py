#Program name: L9 Extra sample program.py
# Create a blank 2D list

drivers = [["Blank"]*5,["Blank"]*5]

# Loop round 5 times and ask for a driver and their points - then store them
for loop in range(5):
    driver = input("Enter the name of a driver: ")
    points = int(input("How many points does that driver have? "))
    drivers[0][loop] = driver
    drivers[1][loop] = points

# Print out populated list to check
#print(drivers)

#######################################
# Solution 1 -
    # Copy the list of points
    # Sort that list into descending order
    # Find the matching driver with those points from the main 2D list
    # Print out the details for each driver
    # NB: This will not work if 2 drivers have the same score

points = drivers[1]
points = sorted(points,reverse=True)

for loop in range(5):
    pointsToPrint = points[loop]
    position = drivers[1].index(pointsToPrint)
    driverToPrint = drivers[0][position]
    print(driverToPrint,"|",pointsToPrint)

#######################################
# Solution 2 -
    # Think of the data as though it is typed into a spreadsheet:
    # Driver 1 | Score
    # Driver 2 | Score
    # Driver 3 | Score
    # etc...

    # It is much easier to sort on rows rather than columns:
    # Driver 1 | Driver 2 | Driver 3 | etc...
    # Score    | Score    | Score    | etc...

    # Use the zip function to re-arrange the data into rows
    # Each list item will contain the driver AND and score
    # This is called a 'tuple' (the bit in brackets):
        # [(driver1,score) , (driver2,score) , etc...]
    # Each item can be addressed in the same way as a 2D list
    
    # Next, use a lambda function to sort on a given field
    
    # Note that printing the list requires some tweaking
    # as the list is now a list of tuples

drivers = sorted(zip(*drivers), key = lambda drivers:drivers[1],reverse=True)

print(drivers)

for loop in range(5):
    print(drivers[loop][0],"|",drivers[loop][1])
