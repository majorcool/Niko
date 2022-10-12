def str_stripper(str1, str2):
    for i in range(len(str2)):
        print(str2[i])
        str1 = str1.replace(str2[i], '')
    return str1


print(str_stripper(input("1:"), input("2:")))
