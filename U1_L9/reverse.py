def reverse(n):
    if n // 10 == 0:
        return n
    string_num = str(n)
    return int(string_num[-1] + '0' * (len(string_num) - 1)) + reverse(n // 10)


print(reverse(123455432112))
