
class Character:

    def __init__(self, position: float = 0, health: float = 100):
        self._position = position
        self.health = health

    def fight(self):
        print("fighting")

    def move(self, distance: float):
        self._position += distance

    def print_position(self):
        print(str(self._position) + "m away.") 


# inheritance is the idea of extending a base class
# Our base class (aka parent class) is Character
# Our subclass (aka child class) is Mage
class Mage(Character):

    def __init__(self, position=0, health=100):
        # the super function let us access the base class constructor
        super().__init__(position=position, health=health)
        self._magic_point = 100

    def cast(self):
        # cast a magic spell
        print("YOU SHALL NOT PASS")
        self._magic_point -= 10

    def print_magic_point(self):
        print("MP: " + str(self._magic_point))


# We can extend the mage class again
# there is no limit on the inheritance level
# However it could lead to the class explosion problem
# ie large class hierarchical structure
class Wizard(Mage):
    def fight(self):
        print("booommm!")


# We can reuse the same base class
class Warrior(Character):

    def fight(self):
        print('Yarrrr')


# Python supports multi class inheritance
# but it is a bad practice, it introduces more problems than what it solves
# just for demonstration -- dont do this
# Champion is now inheriting from wizard and warrior
# We can inherits from as many classes as we want, but that adds a lot of complexities
class Champion(Wizard, Warrior):
    pass


if __name__ == '__main__':
    champ = Champion()

    # the wizerd class has a fight method
    # the warrior class also has a fight method
    # Which one is champ calling? It is ambiguous!
    # behind the scene python uses something called MRO(method resolution order) to resolve the correct method call
    # https: // www.python.org / download / releases / 2.3 / mro /
    # left one wins out
    champ.fight()
