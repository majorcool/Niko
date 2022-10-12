def ishuiwen (hw_str):
    left = hw_str[:len(hw_str) // 2]
    right = hw_str[-(len(hw_str) // 2):]
    return left == right[::-1]

print(ishuiwen(input()))

