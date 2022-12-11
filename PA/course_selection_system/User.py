

class UsernameNotFound(Exception):
    pass


class PasswordError(Exception):
    pass


class User:
    auth_file_loc = "auth_file.txt"

    def __init__(self, username, usertype = "User"):
        if not User.check_user_exsist(username):
            f = open(User.auth_file_loc, "a+")
            self.username = username
            self.password = "password"
            f.write(username + ' ' + self.password + '\n')
            f.close()

        userfile = open(username, "rw")
        print(userfile.readline().find("usertype"))
        if userfile.readline().find("usertype") == -1:
            print("usertype not found, writing")
            userfile.write("usertype: " + usertype + "\n")

        userfile.close()
        # 创建文件

    @staticmethod
    def check_user_exsist(username):
        f = open(User.auth_file_loc, "r")
        usernames = []
        while (True):
            line = f.readline()
            if line == "":
                break
            line = line.strip()
            usernames.append(line.split(" ")[0])
        if not username in usernames:
            return False
        return True
    @staticmethod
    def get_usertype(username):
        f = open(username, "r")
        raw_line = f.readline()
        type = raw_line.strip().lstrip("usertype: ")
        return type

    @staticmethod
    def login(username, password):
        if not User.check_user_exsist(username):
            raise UsernameNotFound
        f = open(User.auth_file_loc, "r")
        usernames = []
        passwords = []
        while(True):
            line = f.readline()
            if line == "":
                break
            line = line.strip()
            usernames.append(line.split(" ")[0])
            passwords.append(line.split(" ")[1])
        if not password == passwords[usernames.index(username)]:
            raise PasswordError
        return True


