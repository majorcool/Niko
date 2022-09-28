users = ('root', 'user1', 'user2')
passwords = ('123', 'abc', '@*#')

for _ in range (3):
    usrname=input("username:")
    for i in range(len(users)):
        if users[i] == usrname:
            break
    else:
        print("User does not exsist")
        continue
    passwd=input("password:")
    if passwords[i] == passwd:
        print("Welcome")
        break
    else:
        print("Password does not match")
else:
    print("Too many retries, login failed")