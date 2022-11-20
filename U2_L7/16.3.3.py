def find_repeat_n(l):
    ldict = dict()
    for i in l:
        if ldict.get(i) == None:
            ldict.update({i: 1})
        else:
            ldict.update({i: ldict[i] + 1})
    for key, value in ldict.items():
        if value == len(l)//2:
            print(key, "repeated", value, "times")
            return key
    return None


nums = [5,1,5,2,5,3,5,4]
find_repeat_n(nums)