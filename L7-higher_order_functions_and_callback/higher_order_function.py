

# a function can accepts other function as argument


# Higher order function
# function that either takes in another function as argument or return a function

# why callback?
# allow user to define their own logic and customise the function call
def shopping(budget, after_shopping):
    balance = budget - 50
    balance = budget - after_shopping(balance)
    print("Going home with ${balance}".format(balance=balance))
    return balance


def watch_movie(balance):
    print("Watching movie!")
    return balance - 10

# closure is a function created inside a function
# benefits: enclosing data within functions


# factory function
# functions that manufacture/create function
# aka higher order function that returns a function


# traditional way
# not descriptive
def calc_rate(amount, rate):
    return round(amount * rate, 2)


def make_rate_function(rate: float):
    def closure(amount: float):
        return round(amount * rate, 2)
    return closure


# using factory function to calculate amount
calc_gst = make_rate_function(0.1)
calc_tax = make_rate_function(0.2)

# why?
# we get descriptive functions and self commenting code




if __name__ == '__main__':
    shopping(100, watch_movie)
    print(calc_gst(1000))
    print(calc_tax(2000))


    pass



