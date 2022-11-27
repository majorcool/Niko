class GetFloatError(Exception):
    pass


def float_input():
    try:
        result = float(input())
    except ValueError:
        raise GetFloatError
    else:
        return result


try:
    print(float_input())
except GetFloatError:
    print("not float")

