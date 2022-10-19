def bin_add(str1, str2):
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    return str(bin(int1+int2)).removeprefix('0b')


print(bin_add("11", "1"))