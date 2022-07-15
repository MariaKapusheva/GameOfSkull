import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH//(2*COLS)

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (233, 234, 236)
DARK = (96, 96, 96)
ORANGE = (255, 153, 51)
FONT = pygame.font.SysFont('Corbel',35)

ROSE = pygame.transform.scale(pygame.image.load('assets/rose.png'), (45, 45))
SKULL = pygame.transform.scale(pygame.image.load('assets/skull.png'), (45, 45))