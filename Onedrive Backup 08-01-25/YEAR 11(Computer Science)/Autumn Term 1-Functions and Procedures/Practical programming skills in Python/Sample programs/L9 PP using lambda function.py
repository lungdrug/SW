#Program L9 PP using lambda function.py
#Uses lambda function to sort a 2-D list in descending sequence

gameScores=[["Dave", 18],
	    ["Christina", 23],
	    ["Phil",16],
	    ]
numRows = len(gameScores)
for row in range(numRows):
    print(gameScores[row])

#myData[1] specifies that the 2-D list is to be sorted on column 1.
#reverse = True is an optional parameter, specifying a sort in descending order
gameScores = sorted(gameScores, key = lambda myData:myData[1], reverse = True)

print("\nSorted data:")
for row in range(numRows):
    print(gameScores[row])