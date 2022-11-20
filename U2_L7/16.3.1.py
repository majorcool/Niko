import random


class Player:
    def __init__(self):
        pass

    def select_num(self, playernum):
        return random.randint(0, playernum - 1)


class Mafia(Player):
    def select_num(self, playernum):
        return random.randint(0, playernum - 1)

    pass


class Judge:
    def __init__(self):
        pass

    def open_eye(self, players, mafiaonly=False):
        player_num = len(players)
        num_list = []
        for i in range(player_num):
            num_list.append(0)
        for i in players:
            if not mafiaonly:
                num_list[i.select_num(player_num)] += 1
            else:
                if i is Mafia:
                    num_list[i.select_num(player_num)] += 1
        maxcnt = 0
        maxloc = 0
        for i in range(player_num):
            if num_list[i] > maxcnt:
                maxloc = i
                maxcnt = num_list[i]
        return maxloc


def is_there_goodpeople(players):
    flag = False
    for i in players:
        if not i is Mafia:
            flag = True
    return flag


def is_there_mafia(players):
    flag = False
    for i in players:
        if i is Mafia:
            flag = True
    return flag


judge = Judge()
players = []
for i in range(3):
    players.append(Mafia())
for i in range(6):
    players.append(Player())
while True:
    mafia_kill = judge.open_eye(players, True)
    players.pop(mafia_kill)
    normal_kill = judge.open_eye(players)
    players.pop(normal_kill)
    if not is_there_goodpeople(players):
        print("好人")
        break
    if not is_there_mafia(players):
        print("Mafia")
        break
