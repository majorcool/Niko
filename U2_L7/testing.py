class A:
    def __init__(self):
        self.b = 1
        del self
    def __del__(self):
        print("del!")


a = A()
print(a.b)

def test(n):
    del n


n = 1
test(n)
print(n)