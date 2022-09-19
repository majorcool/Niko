stu_cnt=30
totscr=0
while stu_cnt > 0:
    print("remaing stu=",stu_cnt)
    tmpscr = int (input("scr?"))
    if tmpscr > 100 or tmpscr < 0:
        print("error!")
    else:
        stu_cnt -= 1
        totscr += tmpscr
print("finished! avg=",totscr/30)