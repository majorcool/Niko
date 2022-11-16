import random

#idk how to define marcos or similar stuff in python, so here goes the dirty version
too_big = 1
exact = 0
too_small = -1

class Dealer:
    def __init__(self):
        self.__num = None

    def set_number(self):
        self.__num = random.randint(0, 100)
        return self.__num

    def hint(self, n):
        if self.__num == n:
            print("猜对了")
            return exact
        if self.__num > n:
            print("猜小了")
            return too_small
        if self.__num < n:
            print("猜大了")
            return too_big


    def check(self,n):
        return self.__num == n


    def award(self, rounds, player):
        player.point = 10 - rounds + 1
        return 10 - rounds + 1


class Player:
    def __init__(self):
        self.point = 0

    def guesss_number(self, n1=0, n2=100):
        return random.randint(n1,n2)


def game():
    dealer = Dealer()
    player = Player()
    dealer.set_number()
    res = -1
    rounds = 0
    n1 = 0
    n2 = 100
    while not dealer.check(res):
        res = player.guesss_number(n1,n2)
        rounds += 1
        hint = dealer.hint(res)
        if hint == too_big:
            n2 -= 1
        if hint == too_small:
            n1 += 1
        dealer.award(rounds, player)
        #if dealer.award(rounds) < -10:
           # return False
    print(rounds)
    return True

game()