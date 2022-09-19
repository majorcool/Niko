chance = 5
magic = 55
while chance > 0:
    guess = int (input("guess"))
    if guess == magic:
        print("correct")
        break
    if guess > magic:
        print("too big")
    if guess < magic:
        print("too small")
    chance -= 1
