def avg_score():
    scr_list=[]
    n = int(input("n=?"))
    for i in range(n):
        tmp = int(input("scr?"))
        while tmp > 100 or tmp < 0:
            tmp = int(input("ERR!\nscr?"))
        scr_list.append(tmp)

    return tuple(scr_list)

scr=avg_score()
print(scr)
total = 0
for i in scr:
    total+=i
print(total / len(scr))

tmpscr= list(scr)

tmpscr[0]=99

scr = tuple(tmpscr)
print(scr)
total = 0
for i in scr:
    total+=i
print(total / len(scr))