

class UsernameNotFound(Exception):
    pass


class PasswordError(Exception):
    pass


class User:
    auth_file_loc = ""

    def __init__(self, username):
        f = open(User.auth_file_loc, "a+")
        self.username = username
        self.password = "password"
        f.write(username + ' ' + self.password + '\n')
        f.close()
        self.file = open(username, "w")
        self.file.close()

    def login(self, username, password):
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
        if not username in usernames:
            raise UsernameNotFound
        if not password == passwords[usernames.index(username)]:
            raise PasswordError
        return True

