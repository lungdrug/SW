#Program L9 WS9a Ex 3-5.py
salaries = [["Steve",35000],["Alice",47000],["Kevin",22000],["Karen",33000]]
print(salaries[1][0], "has an annual salary of £", salaries[1][1])

row = int(input("Enter the number for a member of staff (0-3)"))
print(salaries[row][0], "has an annual salary of £", salaries[row][1])

newSalary = int(input("Enter the updated salary for that staff member: "))
salaries[row][1] = newSalary

print(salaries)

newStaff = input("Enter the name of a new staff member: ")
newSalary = int(input("Enter their annual salary: "))
salaries.append([newStaff,newSalary])
print(salaries)

