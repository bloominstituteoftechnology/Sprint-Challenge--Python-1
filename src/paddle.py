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
        self.touched_by_ball = False

    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)
        # self.rectangle.center = pygame.mouse.get_pos()
        # pygame.mouse.set_visible(False)


class KineticBlock(Paddle):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass
