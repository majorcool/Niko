list_num=[1, 3, 4, 3, 7, 3, 9, 8, 6, 3]
while (list_num.count(3)!=0):
    for i in range(len(list_num)):
        if list_num[i] == 3:
            print(i)
            del list_num[i]
            break

print(list_num)