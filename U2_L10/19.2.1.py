import random
while True:
    try:
        start = int(input())
        end = int(input())
        print(random.randint(start, end))
    except Exception as result:
        print(result)
    else:
        break
