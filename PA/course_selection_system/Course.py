from Mediator import Mediator

class Course():
    def __init__(self, teachername, capacity, coursename):
        self.type = None
        self.score = None
        self.teacher = teachername
        self.capacity = capacity
        self.stu_list = None
        self.name = coursename
    def add_student(self, stus):
        return Mediator.add_student(stus, self)

    def delete_student(self, stus):
        return Mediator.delete_student(stus, self)
