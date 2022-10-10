def dedup(original):
    org_list = list(original)
    tmplist = org_list
    for i in org_list:
        while tmplist.count(i) > 1:
        #print(i,"removed")
            tmplist.remove(i)
    return tmplist


def funfun(numlist):
    numlist.sort()
    anslist = []
    for i in range(0, len(numlist)-2):
        for j in range(i+1, len(numlist)-1):
            for k in range(j+1, len(numlist)):
                if numlist[i] + numlist[j] + numlist[k] == 0:
                    anslist.append((numlist[i], numlist[j], numlist[k]))
    anslist = dedup(anslist)
    return anslist


def max_multiply(numlist):
    max_mul = numlist[0] * numlist[1] * numlist[2]
    reslist = numlist[0:3]
    for i in range(0, len(numlist) - 2):
        for j in range(i + 1, len(numlist) - 1):
            for k in range(j + 1, len(numlist)):
                now_mul = numlist[i] * numlist[j] * numlist[k]
                if now_mul > max_mul:
                    max_mul = now_mul
                    reslist = [numlist[i], numlist[j], numlist[k]]
    return max_mul


#num_list = [-1, 0, 1, 2, -1, -4, 0, 2, 0, 4, -4, -2, -1, 2]
#num_list = [-1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
num_list = [1, 2, 3]
print(max_multiply(num_list))
