import random


class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        deltax = random.randint(-1, 1)
        deltay = random.randint(-1, 1)
        self.x += deltax
        self.y += deltay

    def anti_collision(self, deltax, deltay):
        if self.x < 0 or self.x > 10:
            self.x -= 2 * deltax
        if self.y < 0 or self.y > 10:
            self.y -= 2 * deltay


class BigFish(FIsh):
    def __init__(self):
        super().__init__()
        self.hp = 100

    def move(self):
        deltax = random.randint(-1, 1)
        deltay = random.randint(-1, 1)
        self.hp -= abs(deltax) + abs(deltay)
        self.x += deltax
        self.y += deltay
        self.anti_collision(deltax, deltay)

    def check_hp(self):
        return self.hp

    def eat(self):
        self.hp += 1


class SmallFish(Fish):
    def __init__(self):
        super().__init__()

    def move(self):
        direction = random.randint(0, 1)
        deltax = 0
        deltay = 0
        if direction:
            deltax = random.randint(-1, 1)
        else:
            deltay = random.randint(-1, 1)
        self.x += deltax
        self.y += deltay
        self.anti_collision(deltax, deltay)
