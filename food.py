import pygame
from constants import *
import random


class Food:
    def __init__(self, window):
        self.window = window
        self.x: 15
        self.y: 10
        self.new_location()
        self.draw()

    def distance(self, head):
        xcor = self.x * (LENGTH + OFFSET) + LENGTH // 2
        ycor = self.y * (LENGTH + OFFSET) + LENGTH // 2
        xcor_head = head.x * (LENGTH + OFFSET) + LENGTH // 2
        ycor_head = head.y * (LENGTH + OFFSET) + LENGTH // 2
        return ((ycor_head - ycor)**2+(xcor_head - xcor)**2) ** 0.5


    def draw(self):
        pygame.draw.circle(self.window, (255, 0, 0),
                           (self.x * (LENGTH + OFFSET), self.y * (LENGTH + OFFSET)), 10)

    def new_location(self):
        self.x = random.randint(1, NUM_ROWS - 1)
        self.y = random.randint(1, NUM_ROWS - 1)
        print(self.x, self.y)

