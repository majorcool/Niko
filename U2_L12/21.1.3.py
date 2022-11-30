f = open("1.txt", "r")
newline = f.readline()
while newline != "":
    if newline[0] != "#":
        print(newline.rstrip("\n").rstrip(" "))
    newline = f.readline()
f.close()