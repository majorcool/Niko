import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, point0: Point, point1: Point):
        self.__point0 = point0
        self.__point1 = point1

    def get_len(self):
        return math.sqrt(abs(self.__point0.x - self.__point1.x) ** 2 + abs(self.__point0.y - self.__point1.y) ** 2)
