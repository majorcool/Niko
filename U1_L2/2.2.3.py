age=0
if age<1:
    print("婴儿")
elif 1<=age<=2:
    print("幼儿")
elif 3<=age<=12:
    print("儿童")
else:
    if 13<=age<=20:
        print("青春期")
    if 15<=age<=24:
        print("年轻人")
    if 18<=age<=64:
        print("成年人")
    if age>65:
        print("老年人")