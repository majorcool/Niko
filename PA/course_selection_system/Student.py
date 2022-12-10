from User import User
from Mediator import Mediator
class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []
    def view_scr_reqirements(self):
        pass

    def view_course(self):
        pass

    def choose_course(self, course):
        return Mediator.choose_course(self,course)

    def withdraw_course(self, course):
        return Mediator.choose_course(self,course)

