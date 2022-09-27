normalYear=[31,28,31,30,31,30,31,31,30,31,30,31]
leapYear=[31,29,31,30,31,30,31,31,30,31,30,31]
for i in range (len(leapYear)):
    print(i+1,"月，平年：",normalYear[i],"天，闰年",leapYear[i],"天")