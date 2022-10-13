eng_str = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
num_str = "1234567890"

def passwd_check(passwd_str):
    eng_cnt = 0
    nums_cnt = 0
    for i in range(len(eng_str)):
        eng_cnt += passwd_str.count(eng_str[i])

    for i in range(len(num_str)):
        nums_cnt += passwd_str.count(num_str[i])
    return eng_cnt !=0 and nums_cnt != 0 and len(passwd_str) >= 8


def input_passwd():
    newpasswd = input("password?(must include (a-z,A-Z,0-9) ,8digits)")
    if newpasswd == 'q':
        return newpasswd
    while not passwd_check(newpasswd):
        print("密码不符合要求：must include (a-z,A-Z,0-9) ,8digits")
        newpasswd = newpasswd = input("password?(must include (a-z,A-Z,0-9) ,8digits)")
        if newpasswd == 'q':
            return newpasswd
    return newpasswd


def passwd_reset(login_info):
    while 1:
        username = input("username?")

        if username == 'q':
            return False

        usrname_flag = True
        while usrname_flag:
            for key in login_info:
                if key == username:
                    usrname_flag = False
                    break
            else:
                username = input("username?")

                if username == 'q':
                    return False

        new_password = input_passwd()

        if new_password == 'q':
            return False

        passwd_reuse_flag = True
        while passwd_reuse_flag:
            for oldpasswd in login_info[username]:
                if oldpasswd == new_password:
                    print("不要使用旧密码，重新输入")
                    new_password = input_passwd()

                    if new_password == 'q':
                        return False

                    break
            else:
                break

        login_info[username].insert(0,new_password)
        if len(login_info[username]) > 3:
            login_info[username].pop(len(login_info[username]) -1)

        return username,new_password

login_infoo = {'user1' : ["pw1"], 'user2' : ["pw312345678","pw2","pw1"]}

print(passwd_reset(login_infoo))

print(login_infoo)


