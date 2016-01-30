class Wave(object):
    def __init__(self, data, image, pathdict, start):
        self.__start = start
        self.__count = data["count"]
        self.__minions = []
        self.__pathdict = pathdict
        self.__spawnrate = data["spawnrate"]
        self.__spawnticker = 1
        hp = data["hp"]
        speed = data["speed"]
        score = data["score"]
        goal = data["goal"]
        self.__miniondata = {"hp": hp,
                             "speed": speed,
                             "score": score,
                             "goal": goal,
                             "image": image,
                             "start": self.__start}

    def draw(self, screen, fielddata):
        for m in self.__minions:
            m.draw(screen, fielddata)

    def update(self, pathdict):
        self.__pathdict = pathdict
        if self.__count > 0:
            self.__spawnticker -= 1
            if self.__spawnticker is 0:
                self.__minions.append(Minion(self.__miniondata))
                self.__count -= 1
                self.__spawnticker = self.__spawnrate

        finished = 0
        for m in self.__minions:
            if m.update(self.__pathdict.get(m.pos())):
                finished += 1
                self.__minions.remove(m)
        return finished

    def minionpositions(self):
        poss = []
        for m in self.__minions:
            poss.append(m.pos())
        return poss

    def hit(self, index, damage, freeze, freezeduration):
        if self.__minions.__len__() > index and self.__minions[index].hit(damage, freeze, freezeduration) <= 0:
            score = self.__minions[index].getScore()
            self.__minions.remove(self.__minions[index])
            return score
        else:
            return 0

    def done(self):
        return self.__minions.__len__() is 0


class Minion(object):
    def __init__(self, data):
        self.__im = data["image"]
        self.__start = data["start"]
        self.__x = self.__start[0]
        self.__y = self.__start[1]
        self.__speed = data["speed"]
        self.__dir = (0, 0)
        self.__pos = (self.__start[0], self.__start[1])
        self.__hp = data["hp"]
        self.__score = data["score"]
        self.__goal = data["goal"]
        self.__freeze = 1
        self.__freezeduration = 0

    def move(self):
        self.__x += self.__dir[0] / float(self.__speed * self.__freeze)
        self.__y += self.__dir[1] / float(self.__speed * self.__freeze)

    def draw(self, screen, fielddata):
        screen.blit(self.__im, (int(fielddata["offsetX"] + fielddata["cellW"] * self.__x),
                                int(fielddata["offsetY"] + fielddata["cellH"] * self.__y)))

    def pos(self):
        return self.__pos

    def update(self, dir):
        self.move()
        if dir == (0, 0):
            self.__dir = (0, 1)
        else:
            self.__dir = dir
        if self.__freezeduration is 0:
            self.__freeze = 1
        else:
            self.__freezeduration -= 1
        if (self.__dir[0] is 1 and self.__x >= self.__pos[0] + 1) \
                or (self.__dir[1] is 1 and self.__y >= self.__pos[1] + 1) \
                or (self.__dir[0] is -1 and self.__x <= self.__pos[0] - 1) \
                or (self.__dir[1] is -1 and self.__y <= self.__pos[1] - 1):
            self.__pos = (self.__pos[0] + self.__dir[0], self.__pos[1] + self.__dir[1])
            self.__x = self.__pos[0]
            self.__y = self.__pos[1]
        if self.__y is self.__goal:
            return True

    def getScore(self):
        return self.__score

    def hit(self, damage, freeze, freezeduration):
        self.__hp -= damage
        self.__freeze = freeze
        self.__freezeduration = freezeduration
        return self.__hp


class Tower(object):
    def __init__(self, im, pos, data):
        self.__im = im
        self.__x = pos[0]
        self.__y = pos[1]
        self.__cost = data["cost"]
        self.__cooldown = data["cooldown"]
        self.__cooldowntick = 0
        self.__damage = data["damage"]
        self.__range = data["range"]
        self.__level = 1
        self.__size = data["size"]
        self.__freeze = data["freeze"]
        self.__freezeduration = data["freezeduration"]

    def size(self):
        return self.__size

    def draw(self, screen, fielddata):
        return screen.blit(self.__im, (fielddata["offsetX"] + fielddata["cellW"] * self.__x,
                                       fielddata["offsetY"] + fielddata["cellH"] * self.__y))

    def pos(self):
        return self.__x, self.__y

    def shoot(self):
        if self.__cooldowntick is 0:
            self.__cooldowntick = self.__cooldown
            return True, self.__damage, self.__freeze, self.__freezeduration
        return False, 0, 1, 0

    def update(self):
        if self.__cooldowntick > 0:
            self.__cooldowntick -= 1

    def getRange(self):
        return self.__range

    def getCost(self):
        return self.__cost

    def upgrade(self):
        self.__level += 1
        self.__damage += 10
        self.__range += 1
        self.__cost = int(self.__cost * 1.5)


class projectile(object):
    def __init__(self, pos1, pos2, fielddata, duration):
        self.__start = (fielddata["offsetX"] + fielddata["cellW"] * (pos1[0] + 1),
                        fielddata["offsetY"] + fielddata["cellH"] * (pos1[1] + 1))
        self.__end = (fielddata["offsetX"] + fielddata["cellW"] / 2 + fielddata["cellW"] * pos2[0],
                      fielddata["offsetY"] + fielddata["cellH"] / 2 + fielddata["cellH"] * pos2[1])
        self.__tick = duration

    def data(self):
        if self.__tick > 0:
            self.__tick -= 1
            return self.__start, self.__end
        else:
            return False
