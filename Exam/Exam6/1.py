def is_power_of_3_v1(n: int) -> bool:
    if n <= 0:
        return False
    if n // 3 > 1 and n % 3 == 0:
        return is_power_of_3_v1(n // 3)
    if n // 3 <= 1:
        return n == 3
    return False


def is_power_of_3_v2(n: int) -> bool:
    for i in range(1, 1291):  # (2^31)以3为底开根结果向上取整
        if 3 ** i == n:
            return True
    return False


print(is_power_of_3_v2(int(input())))
