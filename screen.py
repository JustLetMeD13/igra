# screen.py

import pygame

class Screen:
    def __init__(self, width, height, title="Game Window"):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def fill(self, color):
        self.screen.fill(color)

    def update(self):
        pygame.display.flip()

    def draw_rect(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)