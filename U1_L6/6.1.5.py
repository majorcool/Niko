eng_characters = "qwertyuiopasdfghjklzxcvbnm"
nums = "1234567890"


def str_cnt(x):
    eng_cnt = 0
    nums_cnt = 0
    for i in range(len(eng_characters)):
        eng_cnt += x.count(eng_characters[i])

    for i in range(len(nums)):
        nums_cnt += x.count(nums[i])
    return (eng_cnt, nums_cnt, x.count(' '), len(x) - eng_cnt - nums_cnt - x.count(' '))


print(str_cnt(input()))
