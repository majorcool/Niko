def count_ope_to_zero(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count

print(count_ope_to_zero(10, 10))