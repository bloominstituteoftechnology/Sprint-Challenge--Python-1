import pygame

from pygame.math import Vector2
from pygame import Rect


class Paddle:
    def __init__(self, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.rectangle = pygame.Rect(
            position.x - (width/2),
            position.y - (height/2),
            width,
            height)
        self.color = color

    def update(self, **kwargs):
        for key in kwargs:
            print(f"{key}  {kwargs[key]}")
            self.position.x = kwargs['x']
        # self.position[0] = kwargs['newX']

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)
