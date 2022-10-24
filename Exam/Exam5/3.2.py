def reverse_bin(n):
    res_str = str(bin(n)).removeprefix('0b')
    if len(res_str) < 32:
        res_str = '0' * (32 - len(res_str)) + res_str
    print(res_str)
    res_str = res_str[::-1]
    print(res_str)
    res = 0
    for i in range(len(res_str)):
        res += (int(res_str[len(res_str) - i - 1])) * (pow(2, i))
    return res


print(reverse_bin(4294967293))
