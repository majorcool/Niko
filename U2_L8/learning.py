class Animal:
    count = 0


class Dog(Animal):
    Animal.count += 1
    count = 0

    def __init__(self):
        pass
        #Dog.count += 1


class Cat(Animal):
    Animal.count += 1
    count = 0

    def __init__(self):
        pass
        #Cat.count += 1


dog1 = Dog()
cat1 = Cat()

cat2 = Cat()
dog2 = Dog()

cat3 = Cat()
cat4 = Cat()
dog3 = Dog()
dog4 = Dog()

print(Animal.count, Dog.count, Cat.count)