import pygame
from CHECKERS.constant import WIDTH, HEIGHT, SQUARE_SIZE, BLUE, GREEN
from CHECKERS.game import Game

FPS = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_tile(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner():
            game.win_screen()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_tile(pos)
                    game.select(row, col)

            game.update()

    pygame.quit()


main()
