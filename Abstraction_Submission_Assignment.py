from abc import ABC, abstractmethod #abc module === Abstract Base Class


class book(ABC):
    def receipt(self,amount):
        print("Your purchase amount: ",amount)
# Define the function that requires an argument to be pass in
    @abstractmethod
    def payment(self,amount):
        pass

class CashPayment(book):
#Defined how to implement the payment function from its parent receipt class.
    def payment(self, amount):
        print("Your cash payment amount of {}, has been accepted.".format(amount))

obj = CashPayment()
obj.receipt("$18.99")
obj.payment("$18.99")
