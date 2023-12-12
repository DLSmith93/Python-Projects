#
#   Python: 3.11.
#
#   Author:  Devin Smith
#
#   Purpose: Creating a text based game to practice aspects of python
#


def start(nice=0, mean=0, name=""):
    #get user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice, mean, name)

def describe_game(name):

    if name != "":
        print("/nThank you for playing the game {}!\n".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("Please enter your name here -> ").capitalize()
                if name != "":
                    print("Welcome {}!".format(name))
                    print("In this game you will interact with several people and you")
                    print("decide wether they were nice or mean!")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("A stranger approaches you, will you be nice(n) or mean(m)").lower()
        if pick == "n":
            print("The stranger walks away smiling and pleased!")
            nice = nice + 1
            stop = False
        if pick == "m":
            print("The stranger walks away frustrated and scowling")
            mean = mean + 1
            stop = False
    score(nice, mean, name)

def show_score(nice, mean, name):
    print("The current score of tha game is \n {}: Nice \n{}: Mean".format(nice, mean))

def score(nice, mean, name):
    if nice >  2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    print("Congratz {}, you have won the game. You're a nice person".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    print("Sorry {}, you've lost. You're not a very nice person".format(name))
    again(nice, mean, name)

def again(nice, mean, name):
    if nice > 2:
        choice = input("You've won would you like to play again! yes(y) or no(n)").lower()
        if choice == "y":
            print("Thanks for playing again")
            reset(nice, mean, name)
        else:
            print("Thanks for playing, hope you comeback soon!")
            quit()
    if mean > 2:
        choice = input("You've lost {}, would you like to play again? yes(y) or no(n)".format(name)).lower()
        if choice == "y":
            print("Thanks for playing again")
            reset(nice, mean, name)
        else:
            print("Thanks for playing, hope you come back soon!")
            quit()

def reset(nice, neam, name):
    nice = 0
    mean = 0
    start(nice, mean, name) 
        
if __name__ == "__main__":
    start()
