class User:
    auth_file_loc = ""

    def __init__(self):
        username = ""
        password = ""

    def login(self):
        pass


class Student(User):
    def view_scr_reqirements(self):
        pass

    def view_course(self):
        pass

    def choose_course(self):
        pass

    def withdraw_course(self):
        pass


class Teacher(User):
    pass


class Admin_teacher(Teacher):
    def create_student(self):
        pass

    def set_global_scr_req(self):
        pass

    def view_stu_choice(self):
        pass


class Course():
    def __init__(self):
        type = None
        score = None
        teacher = None
        capacity = None
        stu_list = None

    def add_student(self):
        pass

    def delete_student(self):
        pass
