def is_vowel(x):
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'


# 没调好
def reverse_vowels(s):
    for i in range(len(s) // 2):
        if is_vowel(s[i]):
            max_pos = max(s.rfind('a'), s.rfind('e'), s.rfind("o"), s.rfind("u"), s.rfind("i"))
            if max_pos != -1 and max_pos > i:
                tmp = s[max_pos]
                s = s[:max_pos] + s[i] + s[max_pos:]
                s = s[:i] + tmp + s[i:]
    return s


print(reverse_vowels("CoopEdu2022"))
