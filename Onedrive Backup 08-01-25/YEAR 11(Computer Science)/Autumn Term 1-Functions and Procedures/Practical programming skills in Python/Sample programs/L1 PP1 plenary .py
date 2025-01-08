#Program L1 PP1 plenary.py
max = 10
valid = True
mynum = int(input("Pick a number up to " + str(max) + ": "))
if mynum > max:
    valid = False
if valid != False:
    result = mynum ** 3
    print(str(mynum) + " cubed = " + str(result))
else:
    print("Error, too big")
