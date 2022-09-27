def prnt(x):
    cnt=0
    for i in range(0, x):
        for num in range(1, i + 2):
            print(num, "*", i + 1, "=", (i + 1) * num, end='\t')
            cnt+=1
        print("")
    return cnt

print( prnt( int ( input() ) ) )