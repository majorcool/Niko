class RadiusError(Exception):
    pass


def circle_s(r):
    if r < 0:
        raise RadiusError
    return 3.14 * r * r


print(circle_s(-1))
