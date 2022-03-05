import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (244, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 188, 212)
YELLOW = (255, 193, 7)
BLUE = (63, 81, 181)
GREEN = (76, 175, 80)

CROWN = pygame.transform.scale(pygame.image.load('img/crown.png'), (45, 45))