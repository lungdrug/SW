#Program L9 PP bubble sort
#This version swaps each field individually
gameScores=[["Dave", 18],
	    ["Christina", 23],
	    ["Phil",20],
            ["Minny",25],
            ["May",11],
            ["Ken",13]
	    ]
numRows = len(gameScores)
for row in range(numRows):
    print(gameScores[row])

#sort the list in descending order of scores
for i in range(numRows-1):
    #with a large list, it is more efficient for j to stop at numRows-1-i
    #with a small list, it is not a significant time saver!
    for j in range(numRows-1-i):
       #compare the scores in adjacent rows
       if gameScores[j][1] < gameScores[j+1][1]:
         for k in range(2):
            temp = gameScores[j][k]
	    #swap the names first time round the k loop, since k = 0
	    #swap the scores the second time round this loop, when k = 1
            gameScores[j][k] = gameScores[j+1][k]
            gameScores[j+1][k] = temp

print("\nSorted file:")
for row in range(numRows):
    print(gameScores[row])
    
input("Press Enter to end ")

#try adding two more names and running the program again 
                
