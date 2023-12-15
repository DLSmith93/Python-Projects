
###########################################
## this script is for practicing classes ##
###########################################

""""
class book:
    author = "null"
    title = "null"
    genre = "null"
    pages = 0

class manga(book):
    artist = "null"
    volume = 0

class fan_fiction(book):
    sourceMaterial = "null"
    website = "null"


class Game:
    variable1 = "Hello"
    variable2 = "World"

if __name__ == "__main__":
    x = Game()
    print("{} {}!".format(x.variable1, x.variable2))
"""

class User:
    name = "null"
    username = "null"
    age = None
    email = "null"

    def __init__(self, name, username, age, email):
        self.name = name
        self.username = username
        self.age = age
        self.email = email

    def add_user(self):
        self.name = input("Please enter your full name: ")
        self.username = input("Please enter a username: ")
        self.age = input("How old are you: ")
        self.email = input("What is your email: ")

    def show_user(self):
        print("\nUSER")
        print("--------------------")
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Username: {}".format(self.username))
        print("Email: {}".format(self.email))

class Moderator(User):
    mod_number = None
    mod_active = True

    def add_mod(self):
        self.name = input("Please enter your full name: ")
        self.username = input("Please enter a username: ")
        self.age = input("How old are you: ")
        self.email = input("What is your email: ")
        self.mod_number = input("What is your mod number: ")
        answer = input("Are you an active mod yes or no: ").lower()
        if answer == "yes":
            self.mod_active = True
        else:
            self.mod_active = False

if __name__ == "__main__":

    tempName = input("What is your name: ")
    tempUsername = input("Please enter a username: ")
    tempAge = input("How old are you: ")
    tempEmail = input("what is your email: ")

    add_user = User(tempName,tempUsername, tempAge, tempEmail)
    add_mod = Moderator

    add_mod.add_mod()
    add_user.show_user()