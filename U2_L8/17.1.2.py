class Fruit:
    variety = 0


class FruitA(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        FruitA.nums += 1

    def __del__(self):
        FruitA.nums -= 1


class FruitB(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        FruitB.nums += 1

    def __del__(self):
        FruitB.nums -= 1


class FruitC(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        FruitC.nums += 1

    def __del__(self):
        FruitC.nums -= 1


class FruitD(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        FruitD.nums += 1

    def __del__(self):
        FruitD.nums -= 1


class FruitE(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        FruitE.nums += 1

    def __del__(self):
        FruitE.nums -= 1


a = FruitA()
aa = FruitA()
del aa
b = FruitB
c = FruitC
d = FruitD
e = FruitE

print(Fruit.variety)
print(FruitA.nums)
