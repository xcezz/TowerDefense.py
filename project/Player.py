class Player(object):

    def __init__(self, data):
        self.__score = 0
        self.__money = data["money"]
        self.__lives = data["lives"]

    def addScore(self, value):
        self.__score += value

    def getScore(self):
        return self.__score

    def removeLives(self, value):
        self.__lives -= value

    def addMoney(self, value):
        self.__money += value

    def getMoney(self):
        return self.__money

    def getLives(self):
        return self.__lives
