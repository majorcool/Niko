x = int(input("something"))
flag = 0
for i in range (2,x):
    if x % i == 0:
        flag = 1
        break
if flag:
    print("rubbish!")
else:
    print("yes")