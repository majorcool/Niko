
from User import User
from Course import Course
from Teacher import Teacher, Admin_teacher
from Student import Student


def login():
    username = ""
    password = ""
    while True:
        username = input("username:")
        password = input("password:")
        try:
            User.login(username, password)
        except UsernameNotFound:
            print("username does not exsist")
        except PasswordError:
            print("wrong password")
        else:
            break
    type = User.get_usertype(username)
    print(type)




randomstudent = Student("Niko")


