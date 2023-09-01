import pygame
from pygame.locals import *
import math
import random


class Ball:
    INICIAL_VEL = 6
    MAX_VEL = 11
    RADIUS = 10
    RED = (242, 85, 96)
    BLACK_RED = (220, 60, 70)

    def __init__(self, x, y):
        self.original_x = x - self.RADIUS
        self.original_y = y
        self.rect = Rect(self.original_x, self.original_y,
                         self.RADIUS * 2, self.RADIUS * 2)
        self._inicial_vel()

    def _inicial_vel(self):
        angle = self._get_random_angle(30, 75, [0, 44, 45, 46])
        pos = 1 if random.random() < 0.5 else -1

        self.vel_y = - abs(math.sin(angle) * self.INICIAL_VEL)
        self.vel_x = pos * math.cos(angle) * self.INICIAL_VEL

    def _get_random_angle(self, min_angle, max_angle, excluded):
        angle = 0
        while angle in excluded:
            angle = math.radians(random.randrange(min_angle, max_angle, 1))
        return angle

    def increase_vel(self, increment):
        if self.MAX_VEL >= math.sqrt(self.vel_x**2 + self.vel_y**2):
            self.vel_x *= increment
            self.vel_y *= increment

    def draw(self, window):
        pygame.draw.circle(window, self.RED, (self.rect.x + self.RADIUS,
                           self.rect.y + self.RADIUS), self.RADIUS)
        pygame.draw.circle(window, self.BLACK_RED, (self.rect.x + self.RADIUS,
                           self.rect.y + self.RADIUS), self.RADIUS, 3)

    def reset(self):
        self.rect.x = self.original_x
        self.rect.y = self.original_y
        self._inicial_vel()

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # print(self.vel_x, self.vel_y)
        # print(math.sqrt(self.vel_x**2 + self.vel_y**2))
