import pygame
from .constant import BLUE, GREEN, YELLOW, SQUARE_SIZE, BLACK, WHITE, WIDTH, HEIGHT
from .board import Board

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = GREEN
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw_board(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = GREEN
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]

            if skipped:
                self.board.remove(skipped)

            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLUE:
            self.turn = GREEN
        else:
            self.turn = BLUE

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def winner(self):
        return self.board.winner()

    def win_screen(self):
        pygame.init()
        winner = self.winner()
        FONT = pygame.font.Font('freesansbold.ttf', 40)
        text_surf = FONT.render(f'{winner} WINS!!!', True, WHITE)
        text_rect = text_surf.get_rect()
        text_rect.topleft = (WIDTH/2) - (text_surf.get_width()/2), HEIGHT/2

        self.win.fill(BLACK)
        self.win.blit(text_surf, text_rect)
        pygame.display.update()