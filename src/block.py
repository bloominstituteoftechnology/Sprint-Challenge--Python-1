import pygame
import random

from pygame.math import Vector2
from pygame import Rect

def random_color():
    return [random.randint(0, 255) for j in range(3)]

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
        self.width = width
        self.height = height

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
    def check_collision(self):
        if self.touched_by_ball == True:
            self.rectangle = pygame.Rect(0,0,0,0)

class MultipleHitsBlock(KineticBlock):
    counter = 0

    def check_collision(self):
        if self.touched_by_ball == True:
            self.counter += 1
            self.color = random_color()
        if self.counter >= 1:
            self.rectangle = pygame.Rect(0,0,0,0)

class Paddle(KineticBlock):
    def update(self, **kwargs):
        self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)







