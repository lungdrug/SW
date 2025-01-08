# program L6 WS6 Ex6 Parcel weights.py

parcelWeights = []
weight = 100
while weight!=0:
    weight = int(input("Enter weight as an integer value, 0 to end "))
    if weight!=0:
        parcelWeights.append(weight)
    print(parcelWeights)
sortedWeights = sorted(parcelWeights, reverse = True)
#delete the first item in the list
del sortedWeights[0]
print("sorted weights, without maximum ",sortedWeights)
size = len(sortedWeights)

# delete the last item in the sorted list
# remember the last index is size-1 because we start counting at 0

del sortedWeights[size-1]

print("sorted weights, less max and min: ", sortedWeights)
averageWeight = sum(sortedWeights)/(size-1)

print ("average weight = ", averageWeight)

