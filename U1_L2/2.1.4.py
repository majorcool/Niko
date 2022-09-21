magic_num= 55
user_guess= int(input("your guess:"))
if user_guess == magic_num:
    print("corect!")
if user_guess < magic_num:
    print("too small")
if user_guess > magic_num:
    print("too big")
