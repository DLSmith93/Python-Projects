

class Protected:
    def __init__(self):
        self.__varPrivate = 666

    def getPrivate(self):
        print(self.__varPrivate)

    def setPrivate(self, private):
        self.__varPrivate = private


if __name__ == "__main__":

    object = Protected()
    object.getPrivate()
    object.setPrivate(777)
    object.getPrivate()