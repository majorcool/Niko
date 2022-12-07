from User import User
from Mediator import Mediator
class Teacher(User):
    pass


class Admin_teacher(Teacher):
    def create_student(self, num):
        return Mediator.new_student(num)

    def set_global_scr_req(self, scr):
        return scr

    def view_stu_choice(self, stu):
        return stu

