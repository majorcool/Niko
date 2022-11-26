def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

print(div(1, 0))