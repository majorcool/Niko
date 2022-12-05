def can_place_flowers(pots, n):
    zero_sections = []
    temp_start = 0
    temp_len = 0
    for i in range(1,len(pots)):
        if pots[i] == 1:
            temp_start = i
            zero_sections.append(temp_len)
            temp_len = 0
        if pots[i] == 0:
            temp_len += 1
    zero_sections.append(temp_len)
    max_flower = 0
    for i in zero_sections:
        max_flower += (i - 1) // 2
    print(max_flower)
    return n <= max_flower
print(can_place_flowers([1,0,0,0,1],1))