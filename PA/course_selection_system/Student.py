from User import User
from Mediator import Mediator
class Student(User):
    def __init__(self, name):
        super().__init__(name, "Student")
        f = open(name, "r")
        print(f.readlines())
        self.courses = f.readlines()[1].strip().split(" ")
        f.close()
    def view_scr_reqirements(self):
        pass

    def view_course(self):
        print(self.courses)
        pass

    def choose_course(self, course):
        return Mediator.choose_course(self,course)

    def withdraw_course(self, course):
        return Mediator.choose_course(self,course)

