import pygame
from constants import *


class Cell:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window

    def draw(self, color=(0, 0, 0)):
        pygame.draw.circle(self.window, color, [(self.x%NUM_ROWS)*(LENGTH+OFFSET), (self.y%NUM_ROWS)*(LENGTH+OFFSET)], 15)


class Head(Cell):
    def __init__(self, window):
        super().__init__(NUM_ROWS // 2, NUM_ROWS // 2, window)
        self.direction = 0

    def draw(self, color=(0, 120, 0)):
        if self.direction == 0:
            self.x += SPEED
        elif self.direction == 1:
            self.y -= SPEED
        elif self.direction == 2:
            self.x -= SPEED
        else:
            self.y += SPEED
        super().draw(color)
