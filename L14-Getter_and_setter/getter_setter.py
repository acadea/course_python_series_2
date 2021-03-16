

# concept of getter and setter
# reading and writing protected properties

# Best practice in python: to use the @property decorator

class Climate:

    def __init__(self, temp: float):
        self._temp = temp

    def report(self):
        print("The temperature is " + str(self.temp))

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if not type(value) in (float, int):
            raise ValueError()
        self._temp = value


if __name__ == '__main__':
    climate = Climate(35)
    climate.temp = 20
    print(climate.temp)

    # why?
    # to control how we set or read a protected property
    # we encapsulate properties within the object so there is no direct modification on object properties

