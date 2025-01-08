def ClearScreen():
    print("\n"*30)

def Message(text):
    print("        ",text + "\n")

def BlankLines(lines):
    print("\n" * lines)

def GetWidth():
    width = int(input("Enter width in cm "))
    width = (width * 4)+ 1
    return width

def Triangle(width):
    row = int((width/2) - 1)
    print(" "*(row+8),"o")
    row = row-2
    gap = 1
    while row > 0:
        print(" "*(row+8),"o"," "*gap,"o")
        row = row-2
        gap = gap+4
    print(" "*7,"o"*width)

def CheckWidth(width,flag):
    if width > 61:
        print("Maximum is 15 cm")
    else:
        flag = "true"
    return flag

#StartOfProgram

ClearScreen()
Message("Drawing Triangles")
Message("------------------")
width=GetWidth()
Triangle(width)
BlankLines(2)
Triangle(width)
BlankLines(2)


ClearScreen()
Message("   Drawing Triangles")
Message("   ------------------")
flag="false"
while flag=="false":
     width=GetWidth()
     flag=CheckWidth(width,flag)
BlankLines(2)
Triangle(width)
BlankLines(2)

