#Program name: L2 WS2b Ex2.py
goalsTotal = 0
matches = int(input("How many matches were played? "))

for count in range (matches):
    matchno = count + 1
    goals = int(input("How many goals were scored in match " 
    + str(matchno) + "? "))
    goalsTotal = goalsTotal + goals

print("Total goals:", goalsTotal)
print("Average goals:", round(goalsTotal/matches,1))
