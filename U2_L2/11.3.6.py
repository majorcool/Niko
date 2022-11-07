class Student:
    def __init__(self, name='', id=0):
        self.name = name
        self.id = id
        self.course = []

    def __str__(self):
        return self.name + str(self.id) + str(self.course)

    def add_course(self, new_course):
        self.course.append(new_course)

    def del_course(self, old_course):
        self.course.remove(old_course)

    def __len__(self):
        return len(self.course)

    def __del__(self):
        print("stu: name=", self.name, " id=", self.id, "deleted")

    def get_course(self):
        return self.course


class course:
    def __init__(self, id=None, name='', students=[]):
        self.id = id
        self.name = name
        self.students = students

    def add_student(self, stuid):
        self.students.append(stuid)

    def remove_student(self, stuid):
        self.students.remove(stuid)

    def __del__(self):
        print("course", self.name, "is deleted")


