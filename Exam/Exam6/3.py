import itertools
def perms(l):
    return list(itertools.permutations(l))


"""
WIP
def perms(l):
    print(l,"being called")
    if len(l) == 1:
        return [l]
    return_list = []
    for i in range(len(l)):
        print("i=",i,"calling", l[:i]+l[i+1:])
        return_list .append( [[l[i]] + perms(l[:i]+l[i+1:])] )
    return return_list

"""
print(perms([1, 2, 3, 4, 5]))
