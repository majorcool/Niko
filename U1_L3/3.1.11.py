import time
stars=30
while stars > 0:
    print("-", end='')
    stars -= 1
print("")
stars = 30
while stars > 0:
    print("*", end='')
    time.sleep(.5)
    stars -= 1