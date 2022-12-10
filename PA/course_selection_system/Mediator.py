from Course import Course
from User import *
from Teacher import *
from Student import Student

class Mediator:
    @staticmethod
    def add_student(stus, course):
        course.stu_list += stus

    @staticmethod
    def delete_student(stus, course):
        for i in stus:
            course.stu_list.remove(i)

    @staticmethod
    def new_student(name):
        return Student(name)

    @staticmethod
    def kick_student(stu, course, teachername):
        if course.teacher != teachername:
            raise Exception
        

    @staticmethod
    def choose_course(stu, course):
        stu.courses.append(course)
        course.stu_list.append(stu)

    @staticmethod
    def withdraw_course(stu, course):
        stu.courses.remove(course)
        course.stu_list.remove(stu)