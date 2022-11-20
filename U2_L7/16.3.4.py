def shuffle_array(nums: list[int]) -> list[int]:
    x = nums[:len(nums)//2]
    y = nums[len(nums)//2:]
    ans = []
    for i in range(len(nums)//2):
        ans.append(x[i])
        ans.append(y[i])
    return ans


nums = [2,5,1,3,4,7]
print(shuffle_array(nums))