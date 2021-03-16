import datetime
import random

# Programming paradigm

# procedural (step by step instruction)
abc = 123

if abc > 100:
    print('Heyyaaa')


# object orientated (hiding logic within entities called objects -- encapsulation)
#
# functions inside object are known as methods
# variables inside object are known as properties

# in Python, everything is an object

# Eg. 'now' is a method of the datetime object in the datetime module
# We use the 'dot' operator to access method and properties inside an object
time_now = datetime.datetime.now()

# now() will return a datetime object for the current timestamp
print(type(time_now))

# getting the "day" attribute/property from the datetime object
day = time_now.day

print(time_now)
print(day)


# randrange is a function aka method from the random module
rand = random.randrange(1, 10)

# calling the 'join' method from a string object. Remember, everything in python is an object
joined = "-".join(['there', 'is', 'an', 'evil', 'panda'])

# calling the 'format' method from a string object.
formatted = '{colour} is a colour'.format(colour='blue')

# the idea of OOP is to encapsulate code (putting code inside a blackbox), so the end user only needs
# to work with exposed methods and properties without understanding the inner working.

# It is like withdrawing money from the ATM. You only need to interact with the buttons on
# the machine. You don't need to know the inner working how the ATM is connected to your account
# how the system prints out the transaction receipt, how the system calculates the money etc etc.

# Benefits? Cleaner and more reusable code
# we simply need the object to execute the logic

# functional
# describing the logic using meaningful functions
# reads a lot like English
# Python is not a functional language, but it supports features in functional programming
# eg map
fruits = ['apple', 'orange', 'kiwi', 'grape']


def to_upper(word: str):
    return word.upper()


# reads a lot like english!
# it looks like we are describing the process rather than writing the instructions
uppercase_fruits = map(to_upper, fruits)

print(tuple(uppercase_fruits))
