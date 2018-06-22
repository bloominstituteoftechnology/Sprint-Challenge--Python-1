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
        self.width = width
        self.height = height
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

class Paddle(KineticBlock):
    def update(self):
        self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)

class SingleHitBlock(KineticBlock):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.hitpoints = 1

    def check_collision(self):
        if self.touched_by_ball == True:
            self.hitpoints -= 1
            print(self.hitpoints)
        if self.hitpoints <= 0:
            self.__del__(self)

class MultiHitBlock(SingleHitBlock):
    def __init__(self):
        self.hitpoints = 3
