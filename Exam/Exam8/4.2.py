def array_sign(nums: list[int]) -> int:
    is_zero = False
    negative_count = 0
    for i in nums:
        if i == 0:
            return 0
        if i < 0:
            negative_count += 1
    if negative_count % 2 == 0:
        return 1
    else:
        return -1


print(array_sign([-1, 1, -1, 1, -1]))
