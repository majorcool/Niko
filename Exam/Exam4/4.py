def bignum_add (num1, num2):
    if num1.find('.') == -1 and num2.find('.') == -1:
        #happy
        return str(int(num1) + int(num2))


    num1_pointloc = len(num1) - num1.find('.') #Right to left
    num2_pointloc = len(num2) - num2.find('.')

    if num1.find('.') == -1:
        num1_pointloc = 1
    if num2.find('.') == -1:
        num2_pointloc = 1
    #整数加小树

    actualpoint = max(num1_pointloc , num2_pointloc)

    print("pontloc:",num1_pointloc,"2:  ",num2_pointloc)


    for i in range(actualpoint - num2_pointloc):
        num2 += '0'
    for i in range(actualpoint - num1_pointloc):
        num1 += '0'

    print(num1,' ',num2)

    num2_withoutdot = ''
    num1_withoutdot = ''
    for i in range(len(num2)):
        if num2[i] != '.':
            num2_withoutdot += num2[i]
    for i in range(len(num1)):
        if num1[i] != '.':
            num1_withoutdot += num1[i]

    print(num1_withoutdot, ' ', num2_withoutdot)
    result_int = int(num2_withoutdot) + int(num1_withoutdot)
    print(result_int)
    result = str(result_int)
    return result[:(len(result)-actualpoint)+1]+ '.' + result[(len(result)-actualpoint)+1:]


print(bignum_add("11000.677","200.1"))