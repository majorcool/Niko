list1=[]
list1.append(1)
print(list1)

list1.insert(0,2)
print(list1)

list1.extend([3,4])
print(list1)

del list1[0]
print(list1)

newlist=list1
del list1

newlist.remove(3)
print(newlist)

newlist.pop()
print(newlist)

newlist.clear()
print(newlist)

newlist=[1,2,3,4]
newlist[0]=114514
print(newlist)

newlist.sort()
print(newlist)

newlist.sort(reverse = True)
print(newlist)

newlist.reverse()
print(newlist)

print(len(newlist))
print(newlist.count(114514))