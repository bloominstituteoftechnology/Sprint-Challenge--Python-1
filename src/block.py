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
            height
        )
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
    # KineticBall will handle the collision
    pass


class Paddle(KineticBlock):
    def paddle_left(self):
        pace = 10

        # Update x position
        # Check for bounds conflict
        if self.position.x - pace < pace:
            return

        self.position.x -= pace

        # Update rectangle
        self.rectangle[0] = self.position.x

    def paddle_right(self):
        pace = 10

        # Update x position
        # Check for bounds conflict
        if self.position.x + pace > 450:
            return

        self.position.x += pace

        # Update rectangle
        self.rectangle[0] = self.position.x


class Single_Hit_Block(KineticBlock):

    def __init__(self, position, width, height, color):
        self.hits = 1
        super().__init__(position, width, height, color)

    def check_collision(self):
        if self.touched_by_ball == True:
            self.hits -= 1
