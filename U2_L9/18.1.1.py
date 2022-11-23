class A:
    nums = 0

    def __init__(self):
        self.nums = 0

    @staticmethod
    def test1():
        for i in dir(A):
            if i.find("__") == 0 and i.rfind("__") == len(i)-2:
                continue
            print(i, end = ' ')
        print()

    @classmethod
    def test2(cls):
        for i in dir(cls):
            if i.find("__") == 0 and i.rfind("__") == len(i)-2:
                continue
            print(i, end = ' ')
        print()

    def test3(self):
        for i in dir(self):
            if i.find("__") == 0 and i.rfind("__") == len(i)-2:
                continue
            print(i, end = ' ')
        print()


A.test1()
A.test2()

a = A()
a.test3()