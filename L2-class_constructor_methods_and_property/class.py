
# To create an object

# just like we need a recipe to make a meal
# we need a template / blueprint to create an object
# This template is called Class in python


# Class tells Python how to create an object
# we define properties and methods of objects in their class
# objects created from this class would possess the properties and methods defined


# Terminologies:
# instantiate -- creating an object out of a class
# instance -- refer to the object created

class Character:

    # the init function is special function known as the constructor of a class
    # the init function automatically runs when we instantiate a class
    def __init__(self, position: float = 0, health: float = 100):
        # the first argument is a special argument
        # by convention we call it 'self'
        # it represents the object instance to be created

        print('created')

        # there are 2 types of properties
        # public and protected

        # public property -- meant for external use
        self.health = health

        # protected property prefixed with "_"
        # -- meant for internal use only
        self._position = position

    def move(self, distance: float):
        self._position += distance

    def print_position(self):
        print(str(self._position) + "m away.") 


if __name__ == "__main__":
    
    shiny = Character(position=10)

    shiny.move(20)

    shiny.print_position()

    # the "_" prefix is merely a convention
    # python doesn't stop us from accessing the protected property
    print(shiny._position)

    crazy = Character()
    # shiny and crazy are 2 different entities, have their own property
    crazy.print_position()
    crazy.move(50)
    crazy.print_position()



