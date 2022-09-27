def multiply2(list_):
    for i in range(len(list_)):
        if type(list_[i]) == int or type(list_[i]) == float:
            list_[i]*=2
    return list_

print(multiply2([1,2,3,4,"a",True]))