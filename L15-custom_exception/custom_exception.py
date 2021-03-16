
class MyError(Exception):
    pass




# Creating our custom error is more descriptive
# Python's exception system is based on OOP
# We simply need to extend the Exception base class
class PleaseReadTheInstructionError(Exception):
    pass


def main():
    number = input("Please enter a number above 10")
    if not number.isnumeric() and int(number) <= 10:
        raise PleaseReadTheInstructionError()


if __name__ == '__main__':
    main()
    raise MyError("Hey")


