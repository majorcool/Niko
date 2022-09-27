def prnt(x):
    for i in range(0, x):
        for num in range(1, i + 2):
            print(num, "*", i + 1, "=", (i + 1) * num, end='\t')
        print("")
prnt(int(input()))