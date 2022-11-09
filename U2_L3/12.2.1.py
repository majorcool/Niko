class A:
    def __init__(self):
        self.__a = 1

    def alter_a(self,new_a):
        self.__a = new_a


class B(A):
    def __init__(self):
        self.__b = 2

    def alter(self,new_a):
        super().alter_a(new_a)

a = B()
a.alter(100)
print(a._A__a)