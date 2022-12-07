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
    def new_student(num):
        stulist = []
        for i in range(num):
            stulist.append(Student())
        return stulist

    @staticmethod
    def choose_course(stu, course):
        stu.courses.append(course)
        course.stu_list.append(stu)

    @staticmethod
    def withdraw_course(stu, course):
        stu.courses.remove(course)
        course.stu_list.remove(stu)