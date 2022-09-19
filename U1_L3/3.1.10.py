import math
x = int (input("something"))
i = 2
#OI的久远回忆+现查的 我菜菜
while i < int (math.sqrt(x))+1:
    if x % i == 0:
        while x % i == 0:
            x = x // i
            print(i, end= '*')
    i += 1
if x != 1:
    print(x)

