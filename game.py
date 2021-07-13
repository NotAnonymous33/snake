from constants import *
import pygame
from snake import Cell, Head
from food import Food


pygame.init()

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((HEIGHT, HEIGHT))
        self.window.fill(GREY)
        self.clock = pygame.time.Clock()
        self.cells = []
        self.head = Head(self.window)
        self.game_on = True
        self.food = Food(self.window)

    def play(self):
        while self.game_on:
            pygame.display.update()
            self.window.fill(GREY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.head.direction = 0
                    elif event.key == pygame.K_UP:
                        self.head.direction = 1
                    elif event.key == pygame.K_LEFT:
                        self.head.direction = 2
                    elif event.key == pygame.K_DOWN:
                        self.head.direction = 3


            #drawing all objects
            #print(self.food.distance(self.head))
            if self.food.distance(self.head) < 20:
                self.food.new_location()
                #increase length
                #increase points
                #show points
            self.food.draw()
            self.head.draw()
            for cell in self.cells:
                cell.draw()

            


            self.clock.tick(FPS)

