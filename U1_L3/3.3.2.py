height = int(input("h="))

for i in range((height//2)+1):
    for j in range ((height//2)-i):
        print(" ",end='')
    for j in range ((i+1)*2-1):
        print("*", end='')
    print ("")

starnum = height-2
if height % 2 ==0:
    starnum += 1
for i in range(1,(height//2)+1):
    for j in range(i):
        print(" ",end='')
    for j in range(starnum):
        print("*",end='')
    starnum -= 2
    print("")