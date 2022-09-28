def dedup_sort(original):
    org_list=list(original)
    org_list.sort()
    tmplist=org_list
    for i in org_list:
        while tmplist.count(i) > 1:
            tmplist.remove(i)
    return tuple(tmplist)


print(dedup_sort((1,1,1,1,1,1,12,3,4,1,2,1,1,1,1,1,1,True,114514)))