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
        self.width = width
        self.height = height

    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)


class Paddle(Block):
    def __init__(self, position, width, height, color, canvasWidth):
        self.moveLeft = False
        self.moveRight = False
        self.speed = 5
        self.canvasWidth = canvasWidth
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        if self.moveLeft and self.position.x > self.speed:
            self.color = [255, 0, 0]
            self.position.x = self.position.x - self.speed
            self.moveLeft = False
        if self.moveRight and (self.position.x + self.speed) < self.canvasWidth:
            self.color = [0, 0, 255]
            self.position.x = self.position.x + self.speed
            self.moveRight = False
        self.rectangle = pygame.Rect(
            self.position.x - (self.width/2),
            self.position.y - (self.height/2),
            self.width,
            self.height)
        super().update()


class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    # def __init__(self, position, width, height, color):
    #     super().__init__(position, width, height, color)
    pass
