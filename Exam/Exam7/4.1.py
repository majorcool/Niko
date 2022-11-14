def is_all_same_num(n):
    num = n[0]
    for i in n:
        if i != num:
            return False
    return True


def gcd_pro_max_1(*n: int) -> int:
    n = list(n)
    #print(n)
    while not is_all_same_num(n):
        n = list(sorted(n))[::-1]
        for i in range(len(n) - 1):
            if n[i] % n[i + 1] == 0:
                n[i] = n[i + 1]
            else:
                n[i] = n[i] % n[i + 1]
    return n[0]


def gcd_pro_max_2(*n: int) -> int:
    n = list(n)
    #print(n)
    if is_all_same_num(n):
        return n[0]
    n = list(sorted(n))[::-1]
    for i in range(len(n) - 1):
        if n[i] % n[i + 1] == 0:
            n[i] = n[i + 1]
        else:
            n[i] = n[i] % n[i + 1]
    return gcd_pro_max_2(*n)

print(gcd_pro_max_1(999, 1999, 2999, 3999, 4999))
