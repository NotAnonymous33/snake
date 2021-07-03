from constants import *
import pygame


pygame.init()

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((HEIGHT, HEIGHT))
        self.clock = pygame.time.Clock()

    def play(self):




        self.clock.tick(FPS)
