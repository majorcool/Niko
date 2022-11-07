def is_vowel(x):
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'


# 没调好
def reverse_vowels(s):
    vow_list = []
    for i in range(len(s)):
        if is_vowel(s[i]):
            vow_list.append(s[i])
    result = ""
    for i in s:
        if is_vowel(i):
            result += vow_list.pop()
        else:
            result += i
    return result


print(reverse_vowels("CoopEdu2022"))
