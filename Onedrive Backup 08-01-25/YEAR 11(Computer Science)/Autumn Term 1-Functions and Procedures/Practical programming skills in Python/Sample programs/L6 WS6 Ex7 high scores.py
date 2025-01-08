# program L6 WS6 Ex7 high scores.py

highScores =[0,0,0,0,0]
print ("This program allows you to put in your score for a game, ")
print("which you can play any number of times ")
print ("It keeps the best 5 scores and prints them each time")
print ("there's no actual game in this program, it just tests the scoring")

anotherGo = 'y'
while anotherGo == 'y':
    newScore = int(input("Enter your latest score: "))
#
    if newScore > min(highScores):
        print("Well done - that's in the top 5!")
        n=0
        while n<5:
            if newScore > highScores[n]:
                temp = highScores[n]               
                highScores[4] = temp
                highScores[n] = newScore
                n=5
            else:
                n=n+1
# now re-sort the list
        sortedValues = sorted(highScores, reverse= True)
        highScores = sortedValues
    print("the 5 highest scores are ", highScores)
    anotherGo = input("Another go? Answer y or n ")

