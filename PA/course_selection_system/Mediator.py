
class Mediator:
    @staticmethod
    def add_student(stus, course):
        course.stu_list += stus

    @staticmethod
    def delete_student(stus, course):
        for i in stus:
            course.stu_list.remove(i)


    @staticmethod
    def kick_student(stu, course, teachername):
        if course.teacher != teachername:
            raise Exception
        if not stu in course.stu_list:
            raise Exception
        course.stu_list.remove(stu)

    @staticmethod
    def choose_course(stu, course):
        stu.courses.append(course)
        course.stu_list.append(stu)

    @staticmethod
    def withdraw_course(stu, course):
        stu.courses.remove(course)
        course.stu_list.remove(stu)