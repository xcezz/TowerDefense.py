class Button(object):
    def __init__(self, x, y, w, h, imp, ima):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__imp = imp
        self.__ima = ima
        self.__im = imp
        pass

    def isInside(self, (x, y)):
        if x >= self.__x and x <= (self.__x + self.__w) and y >= self.__y and y <= (self.__y + self.__h):
            return True
        return False

    def active(self):
        self.__im = self.__ima

    def passive(self):
        self.__im = self.__imp

    def getImage(self):
        return self.__im

    def getPosdata(self):
        return (self.__x, self.__y,  self.__x + self.__w, self.__y + self.__h)