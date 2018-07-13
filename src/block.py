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
    def __init__(self, object_list, position, width, height, color):
        self.object_list = object_list
        super().__init__(position, width, height, color)

    def update(self):
        if self.touched_by_ball == True:
            self.object_list.remove(self)

class Paddle(KineticBlock):
    def __init__(self, object_list, position, width, height, color):
        super().__init__(object_list, position, width, height, color)

    def update(self):
        self.touched_by_ball = False