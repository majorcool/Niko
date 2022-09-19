x = int(input("something"))
i=2
flag = 0
while i<x:
    if x % i == 0:
        flag = 1
        break
if flag:
    print("rubbish!")
else:
    print("yes")