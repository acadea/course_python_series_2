import time

# a function can return function
# closure -- function in a function


def add_celcius(function):
    def modified(self):
        return str(function(self)) + " deg C"
    return modified


def add_unit(unit: str):
    def decorator(function):
        # def modified(self):
        #     return str(function(self)) + " " + unit
        # return modified
        return lambda self: str(function(self)) + " " + unit
    return decorator

# def add_city(city: str):
#     def decorator(function):
#         print("City " + city + ": ")
#         return function
#     return decorator


class Temperature:
    def __init__(self, temperature: float):
        self._temp = temperature

    @add_unit("deg C")
    def get_temp(self):
        return self._temp


# practical example: helper decorators to perform different types of tasks
# Example1: logging time taken for a function to run
def log_time(func):
    def modified(*args):
        timenow = time.time()
        result = func(*args)
        print("Time taken: {time}".format(time=time.time() - timenow))
        return result
    return modified


# Example2: log function result in a log file
def log_result(func):
    # * operator
    def modified(*args):
        result = func(*args)
        with open("logs.txt", 'a') as file:
            file.write("{}".format(result))
        return result
    return modified


# chaining decorators
@log_result
@log_time
def loop():
    fruits = ['apple', 'orange', 'kiwi', 'durian']
    joined = ""
    for fruit in fruits:
        joined += fruit
    return joined


if __name__ == "__main__":
    temp = Temperature(12)
    print(temp.get_temp())

    loop()

