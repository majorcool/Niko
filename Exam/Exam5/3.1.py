nums = "1234567890"
low = "qwertyuiopasdfghjklzxcvbnm"
high = "QWERTYUIOPASDFGHJKLZXCVBNM"


def passwd_check(passwd):
    num_flag = False
    lowcase_flag = False
    capital_flag = False
    for i in passwd:
        weird_flag = True
        for num in nums:
            if i.find(num) != -1:
                num_flag = True
                weird_flag = False
        for _ in low:
            if i.find(_) != -1:
                lowcase_flag = True
                weird_flag = False
        for _ in high:
            if i.find(_) != -1:
                capital_flag = True
                weird_flag = False
        if weird_flag:
            print("别给我整奇怪的")
            return False
    if not num_flag:
        print("没数字")
    if not lowcase_flag:
        print("没小写")
    if not capital_flag:
        print("没大写")
    if len(passwd) < 8:
        print("不够8位")
    return int(num_flag + lowcase_flag + capital_flag) >= 2 and len(passwd) >= 8


def change_password(user_info: dict) -> bool:
    original_passwd = input("original passwd?")
    new_passwd_1 = input("new password?")
    new_passwd_2 = input("repeat new password?")
    if original_passwd != user_info["password"]:
        print("密码不正确")
        return change_password(user_info)
    if new_passwd_1 != new_passwd_2:
        print("密码不一致")
        return change_password(user_info)
    if not passwd_check(new_passwd_1):
        print("密码不符合如上要求")
        return change_password(user_info)
    user_info["password"] = new_passwd_1
    print("修改成功")
    return True


usr_inf = {
    "user_name": "user_1",
    "password": "password"
}

change_password(usr_inf)

print(usr_inf)
