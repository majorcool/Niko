
magic = 55
while True:
    guess = int (input("guess"))
    if guess == magic:
        print("correct")
        break
    if abs(guess - magic) >50:
        print("lipu")
    elif abs(guess - magic) >30:
        print("nononoo")
    elif abs(guess - magic) <=10:
        print("close")
