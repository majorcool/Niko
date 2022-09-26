totscr=0
for i in range(30):
    print("finished stu=",i)
    tmpscr = int (input("scr?"))
    while ( tmpscr > 100 or tmpscr < 0):
        print("error!")
        tmpscr = int(input("scr?"))
    totscr += tmpscr
print("finished! avg=",totscr/30)