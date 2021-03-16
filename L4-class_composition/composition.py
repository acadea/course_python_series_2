
# Inheritance is sometimes considered as bad practice
# Problem with Inheritance
# Inheritance is not very flexible and messy


class Animal:
    def eat(self):
        pass

    def sleep(self):
        pass


class Bird(Animal):
    pass


class BirdCanFly(Bird):
    pass


class BirdCanFlyButCanSwim(BirdCanFly):
    pass


class BirdCanFlyButCantSwim(BirdCanFly):
    pass


class BirdCantFly(Bird):
    pass


class BirdCantFlyButCanSwim(BirdCantFly):
    pass


class BirdCantFlyAndCantSwim(BirdCantFly):
    pass


class Mammal(Animal):
    pass


class MammalCanFly(Mammal):
    pass


class MammalCantFly(Mammal):
    pass


class Flyable:
    def fly(self):
        pass


class Swimmable:
    def swim(self):
        pass


# composing rather than inheriting
# this is cleaner and easier to debug and maintain
class Swan(Animal):
    def __init__(self):
        self.flyable = Flyable()
        self.swimmable = Swimmable()


class Whale(Mammal):
    def __init__(self):
        self.swimmable = Swimmable()


class Bat(Mammal):
    def __init__(self):
        self.flyable = Flyable()


if __name__ == '__main__':
    swan = Swan()
    # we can call fly from flyable
    # all the methods/properties related to flyable can be called from the flyable property
    swan.flyable.fly()
    swan.swimmable.swim()
