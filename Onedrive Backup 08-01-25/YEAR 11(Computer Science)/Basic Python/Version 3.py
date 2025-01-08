#                       DATA 

Code = ["1066","1966","0007","1234","9999"]
Product = ["Pencil    ","Ruler     ","Stapler    ","Mouse Mat ","Paperclips"]
Price = ["0.28","0.84","4.90","3.00","1.25"]
Receipt = []

#           define "Barcode" and Quantity
Barcode = "0"

#While loop
while Barcode !="-1":
    Barcode = input("Enter a barcode here>")
    if Barcode !="-1":
         Quantity = int(input("Enter the Quantity>"))

#                    For loop
    Flag = 0
    for i in range(len(Code)):


        if Barcode == Code[i]:
            Receipt.append(Code[i])
            Receipt.append(Product[i])
            Receipt.append(Price[i])
            Receipt.append(Quantity)
            Subtotal = Quantity*float(Price[i])
            Subtotal = int(Subtotal*100)/100 # limit to 2 dp
            Receipt.append(Subtotal)
            Flag = 1

    if Flag == 0 and Barcode != "-1":
        print ("No result with this Barcode")

        print("\nGoodbye")




        print("\n   Morrisons")
        print("   =========\n")

        print("Code  Product     Price  QTY  Total\n")

        for i in range(0,len(Receipt),5):
            print(Receipt[i]," ",Receipt[i+1]," ",Receipt[i+2]," ",Receipt[i+3]," ",Receipt[i+4])
            
