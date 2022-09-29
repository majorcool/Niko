
list_num=[1, 3, 4, 3, 7, 3, 9, 8, 6, 3]
del_index=[]
for i in range(len(list_num)):
    if list_num[i] == 3:
        print(i, end = ' ')
        del_index.append(i)
for i in range(len(del_index)-1, -1, -1):
    list_num.pop(del_index[i])

print(list_num)