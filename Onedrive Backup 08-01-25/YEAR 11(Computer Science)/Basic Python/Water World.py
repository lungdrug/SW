def Title(text):
    print("\n"*6)
    print()
    print()
    print()



def PriceCodes():
    print(" A for adults over 18")
    print(" S for students 11-18")
    print(" C for children under 11")
    print()




def GetCode():
    code=input("Enter Code")
    code=code.upper()
    return code



def LookUpPrice(code):
    if code=="A":
        price=17
    elif code=="S":
        price=12
    else:
        price=9
    return price


def Display(price):
    print()
    print(" the cost of ticket £ ", price)
    
    

#StartOfProgram

Title("Water World")
PriceCodes()
code=GetCode()
price=LookUpPrice(code)
Display(price)
