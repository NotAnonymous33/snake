import pygame
from constants import *
import random


class Food:
    def __init__(self, window):
        self.window = window
        self.x: int
        self.y: int
        self.new_location()
        self.draw()




    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0),
                         [self.x * (LENGTH + OFFSET), self.y * (LENGTH + OFFSET), LENGTH, LENGTH])

    def new_location(self):
        self.x = random.randint(0, NUM_ROWS)
        self.y = random.randint(0, NUM_ROWS)

