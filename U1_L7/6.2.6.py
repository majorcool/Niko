def excel_num_conv(x):
    return chr(ord('A') + x)


def no_excel(cnum):
    ans = ''
    while cnum > 0:
        ans += excel_num_conv((cnum - 1) % 26)
        cnum = (cnum - 1) // 26
    return ans[::-1]


print(no_excel(2147483647))
