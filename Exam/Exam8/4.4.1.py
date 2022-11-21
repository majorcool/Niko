import random


class Player:
    def __init__(self):
        self.points = 0

    def punch(self):
        punchlist = [10, 5, 2]
        return punchlist[random.randint(0, len(punchlist)) - 1]


class Computer(Player):
    pass


def judge(punch1, punch2):
    if punch1 == punch2:
        return -1
    if punch1 == 10:
        return int(punch2 != 5)  # returns 1 if punch1 wins, 0 if punch2 wins
    if punch1 == 5:
        return int(punch2 != 2)
    if punch1 == 2:
        return int(punch2 != 10)


def game(player, computer):
    player_punch = player.punch()
    print("player's punch = ", player_punch)
    computer_punch = computer.punch()
    print("computer's punch = ", computer_punch)
    if judge(player_punch, computer_punch) == -1:
        print("tie")
    else:
        if judge(player_punch, computer_punch):
            player.points += 1
        else:
            computer.points += 1

    print("player's points = ", player.points)
    print("compter's points = ", computer.points)


player = Player()
computer = Computer()
game(player, computer)
