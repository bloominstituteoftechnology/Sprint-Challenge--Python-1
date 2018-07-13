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

class RegularBlock(KineticBlock):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.should_draw = True

    def collision(self):
        self.should_draw = False

class RainbowBlock(RegularBlock):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.collisioncount = 0

    def collision(self):
        self.collisioncount = 1
        if self.collisioncount >= 5:
            self.should_draw = False

# The above allows the Rainbow Block to take a certain number of hits before vanishing

        else:
            if self.collisioncount == 1 or self.collisioncount == 3:
                self.color = [0, 255, 0]
            if self.collisioncount == 2 or self.collisioncount == 4:
                self.color = [0, 0, 255]

# This makes the Rainbow Block change colors upon being hit

class Paddle(KineticBlock):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.left = False
        self.right = False
        self.height = height
        self.width = width

    def update(self):
        if self.left == True:
            self.position.x = (self.position.x - 2) if self.position.x > 30 else 30
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        if self.right == True:
            self.position.x = (self.position.x + 2) if self.position.x < 370 else 370
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        super().update()

    def moveleft(self):
        self.left = True

    def moveright(self):
        self.right = True
