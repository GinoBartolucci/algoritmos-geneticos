from breakout import Game
import pygame
from pygame.locals import *

pygame.init()


class BreakoutGame:
    def __init__(self, window, window_width, window_height):
        self.game = Game(window, window_width, window_height, cols=6, rows=6)
        self.ball = self.game.ball
        self.paddle = self.game.paddle
        self.wall = self.game.wall

    def run_game(self):
        fps = 60
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(fps)
            # draw all objects
            self.game.draw()
            game_info = self.game.loop()

            if not game_info.game_over:
                # Mover paddle
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    self.game.move_paddle(left=True)
                if key[pygame.K_RIGHT]:
                    self.game.move_paddle(left=False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # si perde espera el click para reiniciar
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.reset()
            pygame.display.update()
        pygame.quit()


window_height = 600
window_width = 600
window = pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption('Breakout')

game = BreakoutGame(window, window_width, window_height)
game.run_game()
