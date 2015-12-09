import pygame
import GameObjects
import Path2
from pygame.locals import *


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Basic Pygame program')

    background = pygame.image.load("background.bmp").convert()
    screen.blit(background, pygame.Rect(0, 0, 600, 800))


    pygame.display.flip()

    clock = pygame.time.Clock()
    FPS = 10

    pathfinder = Path2.Pathfinder(50)
    pathdict = pathfinder.getpathdict()

    turrets = []
    minions = []

    # Event loop
    while 1:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = ((event.pos[0] - 6)/10, (event.pos[1] - 6)/10)
                    fields = [pos, (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), (pos[0], pos[1] + 1)]
                    check = True
                    for field in fields:
                        if field not in pathdict.keys():
                            check = False
                    if check:
                        turrets.append(GameObjects.Tower(pygame.image.load("tower.bmp"), pos))
                        pathfinder.deletefields(fields)
                if event.button == 2:
                    pathdict = pathfinder.getpathdict()
                if event.button == 3:
                    minions.append(GameObjects.Monster(pygame.image.load("minion.bmp")))

        screen.blit(background, (0, 0))
        for t in turrets:
            screen.blit(t.blit()[0], t.blit()[1])
        for m in minions:
            if pathdict.get(m.pos()):
                movement = (pathdict.get(m.pos())[0] - m.pos()[0], pathdict.get(m.pos())[1] - m.pos()[1])
                m.move(movement)
            screen.blit(m.blit()[0], m.blit()[1])

        pygame.display.flip()


if __name__ == '__main__': main()
