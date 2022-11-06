def perms(l):
    return_list = []
    for i in range(len(l)):
        for j in range(len(l)):
            for k in range(len(l)):
                for l_ in range(len(l)):
                    for m in range(len(l)):
                        if i == j or i == k or i == l_ or i == m:
                            continue
                        if j == k or j == l_ or j == m:
                            continue
                        if k == l_ or k == m:
                            continue
                        return_list.append((l[i], l[j], l[k], l[l_], l[m]))
    return sorted(return_list)


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
print(len(perms([1, 2, 3, 4, 5])))
