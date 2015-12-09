import pygame
import UI
from pygame.locals import *


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    # background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Pimmelberga", 1, (10, 10, 10))
    textpos = pygame.Rect(100, 100, 0, 0)
    # textpos.centerx = background.get_rect().centerx

    # background.blit(text, textpos)
    myimage = pygame.image.load("background.bmp")
    screen.blit(myimage, pygame.Rect(0, 0, 600, 800))

    # Blit everything to the screen
    screen.blit(myimage, (0, 0))
    pygame.display.flip()

    but = UI.Button(530, 30, 100, 100, pygame.image.load("button1.bmp"), pygame.image.load("button2.bmp"))
    minion = pygame.image.load("minion.bmp")

    a = 1

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                if but.isInside(event.pos):
                    print event.pos
            if event.type == MOUSEMOTION:
                if but.isInside(event.pos):
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    but.active()
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    but.passive()

        screen.blit(myimage, (0, 0))
        screen.blit(but.getImage(), but.getPosdata())

        screen.blit(minion, pygame.Rect(a, 20, 8, 8))
        a+=1
        pygame.display.flip()


if __name__ == '__main__': main()