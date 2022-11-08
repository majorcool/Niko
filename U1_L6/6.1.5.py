eng_characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
nums = "1234567890"


def str_cnt(x):
    eng_cnt = 0
    nums_cnt = 0
    for i in x:
        eng_cnt += i.isalpha()

    for i in x:
        nums_cnt += i.isdigit()
    return (eng_cnt, nums_cnt, x.count(' '), len(x) - eng_cnt - nums_cnt - x.count(' '))


print(str_cnt(input()))
