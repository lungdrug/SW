price=int(input("Enter price of the item:  "))
quantity=int(input("Enter the quantity of the item:  "))
total=price*quantity
if total >= 50:
    discount=0.1*total
    total=total-discount
    print("You qualify for a discount")
    print("--------------------------")
    print("Discount applied")
    print("Please pay:",total)
else:
    print("You do not qualify for a 10% Discount")
    print(total)
