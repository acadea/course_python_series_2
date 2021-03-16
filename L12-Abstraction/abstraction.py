import abc

# Abstraction - user only need to know how to use the method exposed by
# an object, without caring about the implementation details.

# Abstract class is the concept of a half completed base class
# all the subclasses will implement the methods defined in the abstract class
# So if we know a certain class is inheriting from the base class
# We would know exactly what methods are available

# an abstractmethod is a method that the abstract class expect all its subclasses to implement

# ABC is a module that brings in the feature of abstraction to Python
# by declaring a method using the @abstractmethod decorator
# we will force the child classes to implement all the abstract methods
# otherwise an error will be thrown


class PaymentGateway(abc.ABC):

    @abc.abstractmethod
    def pay(self, amount):
        pass

    @abc.abstractmethod
    def refund(self, amount):
        pass


class Paypal(PaymentGateway):
    def pay(self, amount):
        pass

    def refund(self, amount):
        pass


class Visa(PaymentGateway):

    def pay(self, amount):
        pass

    def refund(self, amount):
        pass


if __name__ == '__main__':
    PaymentGateway() # expect error
