#Program name: L10 PP test myList sequence.py
valid = True
myList = [12,17,42,56,68]
i = 0
while valid == True and i < len(myList)-1:
    if myList[i] > myList[i+1]:
        valid = False
        print("List is unsorted")
    else:
        i = i + 1
if valid == True:
    print("List is in ascending sequence")
input("Press Enter to exit: ")
