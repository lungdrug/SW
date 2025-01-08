#This program uses 3 1D array
#CODE[] stores barcode,product[]store product names
#and prices for a single unit

#This version allows you to look up product details using a code
#When you want to stop enter -1 instead of a bar code
#It also uses a flag.The flag is set to 0 and changes to a 1
#If there is a match.It is used so the computer knows
#When to output "no product with this barcode"

code = ["1066","1966","007","12345","999"]
product = ["Pencil","Ruler","Stapler","Mouse Mat","Paperclips"]
price = ["0.28","0.84","4.90","3.00","1.25"]

barcode="0"


while barcode !="-1":
    barcode=input("Enter the barcode here>")


    flag=0
    for i in range(len(code)):

        if barcode== code[i]:
            print("Bar code  -",code[i])
            print("Product  -",product[i])
            print("Price  -",price[i])
            flag=1


if flag==0 and barcode != "-1":
    print("No product with this bar code")

print("/nGoodbye")


    
