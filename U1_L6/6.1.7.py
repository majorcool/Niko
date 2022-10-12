def str_concat(connector, strlist):
    result = ""
    for i in range(len(strlist) - 1):
        result += strlist[i]
        result += connector
    return result + strlist[-1]  # add the previously untouched last element in strlist


print(str_concat("123", ['a', 'b', 'c']))
