def prnt(height=6):
    ans=""
    for i in range((height // 2) + 1):
        for j in range((height // 2) - i):
            ans+=' '
        for j in range((i + 1) * 2 - 1):
            ans+='*'
        ans+='\n'

    starnum = height - 2
    if height % 2 == 0:
        starnum += 1
    for i in range(1, (height // 2) + 1):
        for j in range(i):
            ans+=' '
        for j in range(starnum):
            ans+='*'
        starnum -= 2
        ans+='\n'
    return ans

print(prnt(5))
print(prnt())