import math
x = int (input("something"))
#OI的久远回忆+现查的 我菜菜
#ref: https://oi-wiki.org/math/number-theory/pollard-rho/
for i in range (2, int (math.sqrt(x))+1):
    if x % i == 0:
        while x % i == 0:
            x = x // i
            print(i, end= '*')
if x != 1:
    print(x)