def fill_cups(amount: list[int]) -> int:
    secs = 0
    while max(amount) > 0:
        max1 = -1
        max1_val = -1
        for i in range(3):
            if amount[i] > max1_val:
                max1_val = amount[i]
                max1 = i
        max2 = -1
        max2_val = -1
        for i in range(3):
            if amount[i] > max2_val and i != max1:
                max2_val = amount[i]
                max2 = i
        if max2_val > 0:
            amount[max2] -= 1
            amount[max1] -= 1
            secs += 1
        else:
            amount[max1] -= 1
            secs += 1
    return secs


print(fill_cups([5,0,0]))