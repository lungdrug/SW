# DATA
code = ["1066","1966","007","12345","999"]
product =["Pencil","Ruler","Stapler","Mouse Mat","Paperclips"]
price = ["0.28","0.84","4.90","3.00","1.25"]


Barcode = "0"


while Barcode !="-1":
    Barcode = input  ("Enter the barcode here >")
    if Barcode !="-1":
        quantity = int(input("Enter the quantity  >"))

    Flag = 0
    for i in range(len(code)):
        if Barcode == code[i]:
            print("Barcode   -",code[i])
            print("Product   -",product[i])
            print("Price     -",price[i])
            print("Quantity  -",quantity)
            print("Total price  -",quantity*float(price[i]))
            Flag = 1


if Flag == 0 and Barcode !="-1":
    print("No product with this barcode")
    print("Goodbye")
