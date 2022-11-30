f = open("2.txt", "r")
raw_str = f.read()
numlist = []
for i in range(len(raw_str)):
    if raw_str[i] == '0' and i != 0:
        if raw_str[i-1] == '1':
            numlist.pop()
            numlist.append(10)
        else:
            numlist.append(0)
    else:
        numlist.append(int(raw_str[i]))
numlist.sort()
print(numlist)
f.close()