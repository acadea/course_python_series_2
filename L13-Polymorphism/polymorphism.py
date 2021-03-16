import abc

# Polymorphism - Classes have the same methods but different implementations

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


class Customer:

    def make_payment(self, gateway: PaymentGateway, amount: float):
        return gateway.pay(amount)

    def get_refund(self, gateway: PaymentGateway, amount: float):
        return gateway.refund(amount)

    def complain(self):
        print("Can I talk to your manager?")


if __name__ == '__main__':
    paypal = Paypal()

    karen = Customer()

    # Dependency Injection:
    # we are passing (injecting) an external object to a class, so the Customer is
    # dependent on the PaymentGateway provided. Hence "dependency injection"
    # 25 dollar terms for a 25 cent concept.
    karen.make_payment(paypal, 100)

    karen.complain()
