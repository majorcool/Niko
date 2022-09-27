def add0(list_):
    result=[]
    for i in range(len(list_)):
        result.append(list_[i])
        if i % 2 == 1:
            result.append(0)
    return result

print(add0([1,'a',True,2,3,4]))