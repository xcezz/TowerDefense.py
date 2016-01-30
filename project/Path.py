class Node(object):
    BOTTOM, TOP, RIGHT, LEFT = 0, 1, 2, 3

    def __init__(self):
        self.__available = True
        self.__value = -1
        self.__neighbours = [None, None, None, None]
        self.__direction = (0, 0)
        self.__tower = None

    def add(self, field, position):
        self.__neighbours[position] = field

    def available(self):
        return self.__available

    def setAvailable(self, value, tower):
        self.__available = value
        self.__tower = tower

    def getvalue(self):
        return self.__value

    def setvalue(self, value):
        self.__value = value

    def getdirection(self):
        if self.__value == 0 or self.__value == -1:
            return 0, 0
        val = None
        index = None
        for i in self.__neighbours:
            if i is not None:
                if (val is None or index is None) and i.getvalue() > -1:
                    val = i.getvalue()
                    index = self.__neighbours.index(i)
                else:
                    if -1 < i.getvalue() < val:
                        val = i.getvalue()
                        index = self.__neighbours.index(i)
        if index is not None:
            if index == Node.RIGHT:
                return 1, 0
            if index == Node.LEFT:
                return -1, 0
            if index == Node.BOTTOM:
                return 0, 1
            if index == Node.TOP:
                return 0, -1
        return 0, 0

    def getTower(self):
        return self.__tower

    def getNeighbours(self):
        return self.__neighbours


class Field(object):
    def __init__(self, size, start, end):
        self.__size = size
        self.__start = start
        self.__end = end
        fields = []
        for i in range(0, self.__size):
            fields.append([])
            for j in range(0, self.__size):
                fields[i].append(Node())

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if i > 0:
                    fields[i][j].add(fields[i - 1][j], Node.TOP)
                if i < size - 1:
                    fields[i][j].add(fields[i + 1][j], Node.BOTTOM)
                if j > 0:
                    fields[i][j].add(fields[i][j - 1], Node.LEFT)
                if j < size - 1:
                    fields[i][j].add(fields[i][j + 1], Node.RIGHT)
        fields[0][self.__size / 2].setAvailable(False, None)
        self.__fields = fields

    def getpath(self):
        todo = []
        self.__fields[0][self.__size / 2].setAvailable(True, None)
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__fields[i][j].setvalue(-1)

        for i in range(0, self.__size):
            self.__fields[self.__size - 1][i].setvalue(0)
            todo.append(self.__fields[self.__size - 1][i])

        i = 0
        while todo.__len__() > 0:
            for x in range(0, todo.__len__()):
                f = todo.pop(0)
                for n in f.getNeighbours():
                    if isinstance(n, Node) and n.available() and n.getvalue() == -1:
                        n.setvalue(i + 1)
                        todo.append(n)
            i += 1

        pathdict = {}
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                pathdict.update({(j, i): self.__fields[i][j].getdirection()})

        for i in range(1, self.__start + 1):
            pathdict.update({(self.__size / 2, -i): (0, 1)})

        for i in range(0, self.__end):
            pathdict.update({(self.__size / 2, self.__size - 1 + i): (0, 1)})

        for i in range(0, self.__size):
            pathdict.update({(i, self.__size - 1): (0, 1)})

        for i in range(0, self.__size / 2):
            pathdict.update({(i, self.__size): (1, 0)})

        for i in range(self.__size / 2 + 1, self.__size):
            pathdict.update({(i, self.__size): (-1, 0)})

        pathdict.update({(self.__size / 2, self.__size): (0, 1)})

        self.__fields[0][self.__size / 2].setAvailable(False, None)

        return pathdict

    def deactivate(self, position, tower):
        self.__fields[position[1]][position[0]].setAvailable(False, tower)

    def activate(self, position):
        self.__fields[position[1]][position[0]].setAvailable(True, None)

    def available(self, position, size):
        i, j = position[1], position[0]
        try:
            for k in range(0, size):
                for l in range(0, size):
                    if not self.__fields[i + k][j + l].available():
                        return False
        except IndexError:
            return False
        return True

    def getTower(self, pos):
        i, j = pos[1], pos[0]
        return self.__fields[i][j].getTower()


