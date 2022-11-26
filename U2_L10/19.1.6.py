class IllegalArgumentException(Exception):
    pass


def triangle(a,b,c):
    edge_list = sorted((a,b,c))

    if edge_list[0] + edge_list[1] <= edge_list[2]:
        raise IllegalArgumentException("a, b, c 不能构成三角形")
    print(a, b, c)

try:
    triangle(int(input()), int(input()), int(input()))
except Exception as exc:
    print("exception:", exc)