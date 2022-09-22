def is_complete(x):
    if x == 0:
        return False
    total = 0
    for i in range (1,x):
        if x % i == 0:
            total += i
    return total == x


for i in range(1, 1001):
    if is_complete(i):
        print(i)