import pygame
from pygame.locals import *


class Paddle:
    HEIGHT = 20
    WIDTH = 70
    SPEED = 8
    RED = (242, 85, 96)
    BLACK_RED = (220, 60, 70)

    def __init__(self, x, y):
        self.original_x = x
        self.original_y = y
        self.rect = Rect(x, y, self.WIDTH, self.HEIGHT)

    def move(self, left):
        if left:
            self.rect.x -= self.SPEED
        elif not left:
            self.rect.x += self.SPEED

    def draw(self, window):
        pygame.draw.rect(window, self.RED, self.rect)
        pygame.draw.rect(window, self.BLACK_RED, self.rect, 3)

    def reset(self):
        self.rect.x = self.original_x
        self.rect.y = self.original_y
