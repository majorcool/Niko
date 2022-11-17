class Stack:
    def __init__(self):
        self.s = []

    def push(self, element):
        self.s.insert(0, element)

    def pop(self):
        return self.s.pop()

    def access(self):
        return self.s[len(self.s) - 1]

    def isempty(self):
        return not len(self.s)

    def size(self):
        return len(self)


ss = Stack()
ss.push("first")
ss.push("second")
print(ss.access())
print(ss.pop())
print(ss.access())
