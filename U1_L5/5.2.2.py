def avg_score():
    scr_list=[]
    n = int(input("n=?"))
    for i in range(n):
        tmp = int(input("scr?"))
        while tmp > 100 or tmp < 0:
            tmp = int(input("ERR!\nscr?"))
        scr_list.append(tmp)
    total=0
    for i in scr_list:
        total+=i
    return total/n
print(avg_score())