def deg_arraay(nums):
    freq = dict()
    start = dict()
    stop = dict()
    for i in nums:
        if freq.get(i) is None:
            freq.update({i: 1})
        else:
            freq.update({i: freq.get(i) + 1})
    for i in range(len(nums)):
        if start.get(nums[i]) is None:
            start.update({nums[i]: i})
    _ = nums[::-1]
    for i in range(len(_)):
        if stop.get(_[i]) is None:
            stop.update({_[i]: len(nums) - i - 1})

    degree = 0
    for key,item in freq.items():
        degree = max(degree, item)
    print(degree)
    minlen = len(nums)
    for key,item in freq.items():
        if degree == item:
            #print(key, "has the same freq as deg,start at", start[key], " stop at", stop[key])
            nowlen = stop[key] - start[key] +1
            minlen = min(nowlen, minlen)
    return minlen



with open("2.txt", "r") as f:
    for line in f.readlines():
        _ = line.split(' ')
        num = _[0].split(',')
        result = _[1].strip()
        for i in range(len(num)):
            num[i] = int(num[i])
        result = int(result)
        if deg_arraay(num) != result:
            print(_, "failed")
