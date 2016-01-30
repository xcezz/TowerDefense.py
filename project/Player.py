class Player(object):

    def __init__(self, data):
        self.__score = 0
        self.__money = data["money"]
        self.__lifes = data["lifes"]

    def addScore(self, value):
        self.__score += value

    def getScore(self):
        return self.__score

    def removeLifes(self, value):
        self.__lifes -= value

    def addMoney(self, value):
        self.__money += value

    def getMoney(self):
        return self.__money

    def getLifes(self):
        return self.__lifes
