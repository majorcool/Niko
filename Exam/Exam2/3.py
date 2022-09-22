res = 0
m = int(input("m=?"))
n = int(input("n=?"))
for i in range (1,n+1):
    newnum = 0
    for j in range(0,i):
        newnum += m*10**j
    res += newnum
print(res)