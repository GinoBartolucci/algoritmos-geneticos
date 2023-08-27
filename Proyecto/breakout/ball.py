import pygame
from pygame.locals import *
import math
import random


class Ball:
    MAX_VEL = 5
    RADIUS = 10
    RED = (242, 85, 96)
    BLACK_RED = (220, 60, 70)

    def __init__(self, x, y):
        self.original_x = x - self.RADIUS
        self.original_y = y
        self.rect = Rect(x, y, self.RADIUS * 2, self.RADIUS * 2)

        velx = [1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3]
        dirx = [-1, 1]
        self.vel_x = ((random.choice(velx)**2) * random.choice(dirx))
        vely = math.sqrt(16 - abs(self.vel_x))
        self.vel_y = -1 * vely

    def _get_random_angle(self, min_angle, max_angle, excluded):
        angle = 0
        while angle in excluded:
            angle = math.radians(random.randrange(min_angle, max_angle))
            return angle

    def draw(self, window):
        pygame.draw.circle(window, self.RED, (self.rect.x + self.RADIUS,
                           self.rect.y + self.RADIUS), self.RADIUS)
        pygame.draw.circle(window, self.BLACK_RED, (self.rect.x + self.RADIUS,
                           self.rect.y + self.RADIUS), self.RADIUS, 3)

    def reset(self):
        self.rect.x = self.original_x
        self.rect.y = self.original_y

        velx = [1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3]
        dirx = [-1, 1]
        self.vel_x = ((random.choice(velx)**2) * random.choice(dirx))
        vely = math.sqrt(16 - abs(self.vel_x))
        self.vel_y = -1 * vely

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
