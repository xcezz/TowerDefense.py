import pygame


def main():

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Towerdefense')

    rect = pygame.Rect(0, 0, 15, 15)
    image = pygame.Surface(rect.size).convert()
    image.blit(pygame.image.load("Images/background.png").convert(), (0, 0), rect)
    screen.blit(image, pygame.Rect(0, 0, 15, 15))

    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == '__main__': main()
