class Monster(object):
    def __init__(self, im):
        self.__im = im
        self.__x = 0
        self.__y = 0
        pass

    def move(self, (x, y)):
        self.__x += x
        self.__y += y

    def blit(self):
        return self.__im, (6 + 10 * self.__x, 6 + 10 * self.__y)

    def pos(self):
        return self.__x, self.__y


class Tower(object):
    def __init__(self, im, pos):
        self.__im = im
        self.__x = pos[0]
        self.__y = pos[1]
        pass

    def blit(self):
        return self.__im, (6 + 10 * self.__x, 6 + 10 * self.__y)

    def pos(self):
        return self.__x, self.__y
