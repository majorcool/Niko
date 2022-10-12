def za_conversion(x):
    result = ""
    for i in range(len(x)):
        ordx = ord(x[i])
        if ord('a') <= ordx <= ord('z'):
            result += chr(ord('a') + 26 - (ordx - ord('a')) - 1)
        if ord('A') <= ordx <= ord('Z'):
            result += chr(ord('A') + 26 - (ordx - ord('A')) - 1)
    return result


print(za_conversion(input()))
