def sum_of_unique(nums):
    dict_nums = dict()
    for i in nums:
        if dict_nums.get(i) is None:
            dict_nums.update({i: 1})
        else:
            dict_nums.update({i: dict_nums[i]+1})
    s = 0
    for key, item in dict_nums.items():
        if item == 1:
            s += key
    return s



nums = [1,2,3,4,5]
print(sum_of_unique(nums))