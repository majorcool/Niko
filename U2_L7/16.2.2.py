import random


class Dealer:
    def __init__(self):
        self.__num = None

    def set_number(self):
        self.__num = random.randint(0, 100)
        return self.__num

    def hint(self, n):
        if self.__num == n:
            print("猜对了")
        if self.__num > n:
            print("猜小了")
        if self.__num < n:
            print("猜大了")

    def check(self, n):
        return self.__num == n

    def award(self, rounds):
        return 10 - rounds + 1


class Player:
    def __init__(self):
        self.point = 0

    def guesss_number(self):
        return random.randint(0, 100)


def game(dealer, player):
    dealer.set_number()
    res = -1
    rounds = 0
    while not dealer.check(res):
        res = player.guesss_number()
        rounds += 1
        dealer.hint(res)
        if dealer.award(rounds) < -10:
            return False
    print(rounds)
    return True


dealer = Dealer()
player = Player()
while (game(dealer.player)):
    pass
