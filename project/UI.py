class Handler(object):
    def __init__(self, field):
        self.__buttons = []
        self.__field = field

    def addButton(self, b):
        self.__buttons.append(b)

    def update(self, pos):
        for e in self.__buttons:
            if e.isInside(pos):
                e.active()
            else:
                e.passive()

    def click(self, pos):
        for e in self.__buttons:
            if e.isInside(pos):
                return e.click()
        if self.__field.isInside(pos):
            return self.__field.click(pos)

    def draw(self, screen):
        for e in self.__buttons:
            if e.getVisible():
                e.draw(screen)

    def activ(self):
        for e in self.__buttons:
            if not e.constant():
                e.visible()

    def deactiv(self):
        for e in self.__buttons:
            if not e.constant():
                e.invisible()


class Button(object):
    def __init__(self, data, imp, ima, constant):
        self.__x = data["x"]
        self.__y = data["y"]
        self.__w = data["w"]
        self.__h = data["h"]
        self.__statechange = data["statechange"]
        self.__image_passive = imp
        self.__image_active = ima
        self.__image = imp
        self.__constant = constant
        self.__visible = True
        pass

    def isInside(self, (x, y)):
        if (self.__x + self.__w) >= x >= self.__x and (self.__y + self.__h) >= y >= self.__y:
            return True
        return False

    def active(self):
        self.__image = self.__image_active

    def passive(self):
        self.__image = self.__image_passive

    def click(self):
        return self.__statechange

    def draw(self, screen):
        screen.blit(self.__image, (self.__x, self.__y))

    def constant(self):
        return self.__constant

    def visible(self):
        self.__visible = True

    def invisible(self):
        self.__visible = False

    def getVisible(self):
        return self.__visible


class Field(object):
    def __init__(self, data):
        self.__startx = data["offsetX"]
        self.__starty = data["offsetY"]
        self.__w = data["width"]
        self.__h = data["height"]
        self.__statechange = data["statechange"]
        pass

    def isInside(self, (x, y)):
        if (self.__startx + self.__w) >= x >= self.__startx and (self.__starty + self.__h) >= y >= self.__starty:
            return True
        return False

    def click(self, pos):
        return self.__statechange


class Text(object):
    def __init__(self, pos, font):
        self.__font = font
        self.__pos = pos
        self.__text = []

    def setText(self, text):
        self.__text = text
        return self

    def draw(self, screen):
        for t in self.__text:
            text = self.__font.render(t, 1, (255, 255, 255))
            screen.blit(text, (self.__pos[0], self.__pos[1] + self.__text.index(t) * self.__font.size(t)[1]))



