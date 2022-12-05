def can_place_flowers(pots, n):
    if pots[0] == 0:
        pots = [0] + pots
    if pots[len(pots) - 1] == 0:
        pots = pots + [0]
    zero_sections = []
    temp_len = 0
    for i in range(0,len(pots)):
        if pots[i] == 1:
            if temp_len != 0:
                zero_sections.append(temp_len)
            temp_len = 0
        if pots[i] == 0:
            temp_len += 1
    if temp_len != 0:
        zero_sections.append(temp_len)
    max_flower = 0
    for i in zero_sections:
        if i == 0:
            continue
        print((i - 1) // 2)
        max_flower += (i - 1) // 2
    print(max_flower)
    print(zero_sections)
    return n <= max_flower
print(can_place_flowers([0,0,1,0,0],2))
