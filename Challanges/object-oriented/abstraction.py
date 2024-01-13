
from abc import ABC, abstractmethod

class libarary(ABC):
    
    def inquiry(self, book):
        print("You have requested to check out {}".format(book))

    @abstractmethod
    def checkout(self, book):
        pass

class bookCheckout(libarary):
    
    def checkout(self, book):
        available = True

        if available:
            print("{} is a available you can check the book out for 2 weeks".format(book))

        else:
            print("Sorry, {} is not available.".format(book))


member = bookCheckout()

book = input("What book do you want to check out: ")
member.inquiry(book)
member.checkout(book)
        