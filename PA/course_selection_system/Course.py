from Mediator import Mediator

class Course():
    def __init__(self):
        self.type = None
        self.score = None
        self.teacher = None
        self.capacity = None
        self.stu_list = None

    def add_student(self, stus):
        return Mediator.add_student(stus, self)

    def delete_student(self, stus):
        return Mediator.delete_student(stus, self)
