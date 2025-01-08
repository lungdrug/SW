#L7 Reading one line at a time.py
file= open("people.txt","r")
line = file.readline()
print(line)
line = file.readline()
print(line)
file.close()
