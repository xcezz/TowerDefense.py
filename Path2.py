class Pathfinder(object):
    def __init__(self, size):
        self.__size = size
        self.__available = []
        self.__pathDict = {}
        for i in range(0, size):
            for j in range(0, size):
                self.__available.append((i, j))
        self.__getpath()

    def __getpath(self):
        getpath(self.__pathDict, self.__available, self.__size)

    def deletefields(self, fields):
        for field in fields:
            self.__available.remove(field)

    def getpathdict(self):
        self.__getpath()
        return self.__pathDict


def getpath(pathDict, available, size):
    pathDict.clear()
    todo = []
    done = []
    for i in range(0, size):
        if (i, size - 1) in available:
            todo.append((i, size -1))
    while todo.__len__() != 0:
        (x, y) = todo.pop(0)
        done.append((x, y))
        if (x - 1, y) not in todo and (x - 1, y) not in done and available.__contains__((x - 1, y)):
            pathDict.update({(x - 1, y): (x, y)})
            todo.append((x - 1, y))

        if (x + 1, y) not in todo and (x + 1, y) not in done and available.__contains__((x + 1, y)):
            pathDict.update({(x + 1, y): (x, y)})
            todo.append((x + 1, y))

        if (x, y - 1) not in todo and (x, y - 1) not in done and available.__contains__((x, y - 1)):
            pathDict.update({(x, y - 1): (x, y)})
            todo.append((x, y - 1))

        if (x, y + 1) not in todo and (x, y + 1) not in done and available.__contains__((x, y + 1)):
            pathDict.update({(x, y + 1): (x, y)})
            todo.append((x, y + 1))
