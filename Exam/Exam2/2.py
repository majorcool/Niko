while True:
    x = float (input("x=?"))
    y = float (input("y=?"))
    ope = input("ope=?")
    if ope == '+':
        print("res=",x+y)
    elif ope == '-':
        print("res=",x-y)
    elif ope == '*':
        print("res=",x*y)
    elif ope == '/':
        if y == 0:
            print("y cannot be 0 if you use '/' as operator")
        else:
            print(x/y)
    else :
        print("invalid operator!")