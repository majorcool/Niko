class Student:
    def __init__(self,name = '',id = 0):
        self.name = name
        self.id = id
        self.course = []



    def __str__(self):
        return self.name + str(self.id) + str(self.course)

    def __len__(self):
        return len(self.course)

    def __del__(self):
        print("stu: name=",self.name," id=",self.id,"deleted")

    def get_course(self):
        return self.course


stu0 = Student()
print(stu0)
stu1 = Student("aa",123)
print(stu1)