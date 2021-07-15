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

        self.head = Head(self.window)
        self.cells = [Cell(NUM_ROWS // 2 - 1, NUM_ROWS // 2, self.window)]
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

            # drawing all objects
            # print(self.food.distance(self.head))
            if self.food.distance(self.head) < 20:
                self.food.new_location()
                for _ in range(1):
                    self.cells.append(Cell(self.cells[-1].x, self.cells[-1].y, self.window))
                # increase length
                # increase points
                # show points

            self.cells[0].x = self.head.x
            self.cells[0].y = self.head.y





            for i in range(len(self.cells)-1, 0, -1):
                self.cells[i].x = self.cells[i - 1].x
                self.cells[i].y = self.cells[i - 1].y

            for cell in self.cells:
                cell.draw()
            self.food.draw()
            self.head.draw()
            # print(len(self.cells))

            self.clock.tick(FPS)

