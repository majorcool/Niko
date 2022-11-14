import random


class Animal:
    def __init__(self):
        self.health = 100


class Manager:
    def __init__(self):
        self.performance = 100

    def feed(self, animals):
        for i in animals:
            i.health += 20

    def perform(self, animals):
        for i in animals:
            i.health -= 20

    def __inspect(self, staff, animals):
        for i in animals:
            if i.health < 80:
                staff.performance -= 20
                break

    def performance_report(self, staff, animals):
        self.__inspect(staff, animals)
        return staff.performance


class Keeper(Manager):
    def perform(self):
        return None


class Trainer(Manager):
    def feed(self):
        return None


def everyday():
    manager = Manager()
    keeper = Keeper()
    trainer = Trainer()
    a = Animal()
    animals = []
    animals.append(a)
    trainer.perform(animals)

    trainer.perform(animals)
    trainer.perform(animals)
    print("trainer:", manager.performance_report(trainer, animals))

    keeper.feed(animals)
    keeper.feed(animals)
    keeper.feed(animals)
    keeper.feed(animals)

    print("trainer:", manager.performance_report(trainer, animals))
    print("keeper:", manager.performance_report(keeper, animals))


everyday()
