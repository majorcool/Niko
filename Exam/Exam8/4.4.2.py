import random


class Player:
    def __init__(self):
        self.points = 0

    def punch(self):
        punchlist = [10, 5, 2]
        return punchlist[random.randint(0, len(punchlist)) - 1]

    def challenge(self):
        c_list = ["yes", "no"]
        return c_list[random.randint(0, len(c_list) - 1)]


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

class Fraud:
    def lie(self):
        lie_list = ["lose", "tie"]
        return lie_list[random.randint(0, len(lie_list) - 1)]

def game(player, computer, fraud):
    player_punch = player.punch()
    print("player's punch = ", player_punch)
    computer_punch = computer.punch()
    print("computer's punch = ", computer_punch)
    fraud_check = fraud.lie()
    print("fraud says", fraud_check)
    player_challenge = player.challenge() == "yes"
    print("player want t challenge?", player_challenge)
    player_true_pts = 0
    computer_true_pts = 0
    if judge(player_punch, computer_punch) == -1:
        print("tie")
    else:
        if judge(player_punch, computer_punch):
            player_true_pts += 1
        else:
            computer_true_pts += 1
    if player_challenge:
        player.points += player_true_pts *2
        computer.points += computer_true_pts *2
    else:
        if fraud_check == 'tie':
            pass
        else:
            computer.points += 1
    print("player's points = ", player.points)
    print("compter's points = ", computer.points)


player = Player()
computer = Computer()
fraud = Fraud()
game(player, computer, fraud)
