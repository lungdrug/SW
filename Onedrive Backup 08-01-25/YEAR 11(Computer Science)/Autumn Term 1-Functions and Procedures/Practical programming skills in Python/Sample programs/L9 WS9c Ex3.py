#Program name: L9 WS9c Ex3.py

cpu = [ [ "Intel i5 6400     ", 2.7, 4, 6, 190 ] ]
cpu.append(["Intel i7 2600   ", 3.4, 4, 8, 266])
cpu.append(["AMD FX 8350     ", 4.0, 6, 8, 140])
cpu.append(["AMD Ryzen 7 1700", 3.0, 8, 20, 330])
cpu.append(["Intel i3 6100   ", 3.7, 2, 3, 110])


print("Choose from the following list")
print("1. Name")
print("2. Clock speed")
print("3. Number of cores")
print("4. Cache size")
print("5. Price")
choice = int(input("Enter your choice: "))
if choice == 1 or choice == 5:
      desc = False
else:
      desc = True
cpuSorted = sorted(cpu, key=lambda data:data[choice-1], reverse=desc)


#print titles with tabs
print("CPU\t\t\tClock speed\tCores\t\tCache size\tPrice in GBP")
for row in range(5):
      print(cpuSorted[row][0], "\t",cpuSorted[row][1],\
      "\t\t",cpuSorted[row][2],"\t\t",cpuSorted[row][3],"\t\t",cpuSorted[row][4])
print("\n")

#or a not-so-neat printout:
print("Same information, not tabbed...")
for row in range(5):
      print(cpuSorted[row][0] + ": " + str(cpuSorted[row][1]) + "GHz, " +
      str(cpuSorted[row][2]) + " cores " + str(cpuSorted[row][3]) + "MB at GBP" +
      str(cpuSorted[row][4]))

