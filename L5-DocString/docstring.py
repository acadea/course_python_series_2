class Character:
    def __init__(self, position: float = 0, health: float = 100):
        self._position = position

        self.health = health

    def move(self, distance: float):
        self._position += distance

    def print_position(self):
        print(str(self._position) + 'm away.')


class Mage(Character):
    def __init__(self, position: float = 0, health: float = 100):
        super().__init__(position, health)
        self._magic_point = 100

    def cast(self, spell: str):
        """ This method will make the character cast a spell.

        Consumes character's MP according to the spell's mp cost property.

        :param spell: Character will cast this spell.
        :type spell: str
        :return This function will not return anything.
        :rtype: None
        :except Exception description
        """
        print("YOU SHALL NOT PASS!!!")
        self._magic_point -= 10
        print(spell)

    def print_magic_point(self):
        print("MP: " + str(self._magic_point))


