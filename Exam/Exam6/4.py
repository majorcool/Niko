def max_sec_average(nums: list, k: int) -> float:
    avgmax = None
    for i in range(len(nums) - k + 1):
        avg_list = nums[i:i + k]
        total = 0.0
        for j in avg_list:
            total += j
        if avgmax == None:
            avgmax = total / k
        avgmax = max(avgmax, total / k)
    return avgmax


print(max_sec_average([1, 12, -5, -6, 50, 3], 4))
