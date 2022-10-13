def move_sequence(x, direction = "right", list_input = []):
    result = []
    length = len(list_input)
    if direction == "left":
        for i in range(x, length):
            result.append(list_input[i])
        for i in range(x):
            result.append(list_input[i])
    if direction == "right":
        for i in range(x):
            result.append(list_input[-(x-i)])
        for i in range(length-x):
            result.append(list_input[i])
    return result

print(move_sequence(2,"left",[1,2,3]))
