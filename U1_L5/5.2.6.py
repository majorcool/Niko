stupidming = [0,4,1,3,7,2,1,5]

stupidming.sort()

while len(stupidming) > 1:
    a=stupidming[0]
    b=stupidming[1]
    stupidming.append(a*b+1)

    stupidming.pop(0)
    stupidming.pop(0)
    stupidming.sort()

print(stupidming[0])