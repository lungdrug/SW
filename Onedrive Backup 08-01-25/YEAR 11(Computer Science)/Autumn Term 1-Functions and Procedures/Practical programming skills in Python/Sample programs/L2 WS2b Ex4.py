#Program name: L2 WS2b Ex4.py

points = 101
darts = 0

while points > 0:
   print("Points left:", points)
   score = int(input("Enter the score on this throw: "))
   points = points - score
   darts = darts + 1

print("Game won! Darts thrown:", darts)
