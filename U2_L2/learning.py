class C:
    def __init__(self):
        print('init 被调用了...')

    def __del__(self):
        print('del 被调用了...')


c1 = C()
c2 = c1
c3 = c2

del c1
print('-----')
del c3
print('*****')
del c2
print('#####')