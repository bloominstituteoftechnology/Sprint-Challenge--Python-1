import pygame

from pygame.math import Vector2
from pygame import Rect


class Block:
    """
    Base class for square or rectangular object
    """

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


class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass


class VanishingBlock(KineticBlock):

    def __init__(self, position, width, height, color, hits):
        self.hits = hits
        super().__init__(position, width, height, color)

    def update(self):
        pass


class Paddle(KineticBlock):

    def update(self, **kwargs):
        for key in kwargs:
            # print(f"{key}  {kwargs[key]}")
            self.position.x = kwargs[key]
            # print(self.rectangle[1])
            width = self.rectangle[2] / 2
            self.rectangle[0] = self.position.x - width
            # self.rectangle = pygame.Rect(
            #     position.x - (width/2),
            #     position.y - (height/2),
            #     width,
            #     height)
        super().update()

    def check_collision(self):
        pass

    # def draw(self, screen, pygame):
    #     pygame.draw.rect(screen, self.color, self.rectangle)
