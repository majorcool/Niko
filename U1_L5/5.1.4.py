travel_list =["d","e","b","a","c"]
print(travel_list)
templist = travel_list.copy()

templist.sort()
print(templist)
print("original:",travel_list)

templist.reverse() #不浪费时间重新排序,有序状态下直接reverse
print(templist)
print("original:",travel_list)

travel_list.reverse()
print(travel_list)
travel_list.reverse()
print(travel_list)

travel_list.sort()
print(travel_list)
travel_list.reverse()
print(travel_list)