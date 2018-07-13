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
        if self.touched_by_ball == True:
            print(1)

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
    def __init__(self, position, width, height, color):
        self.left = False
        self.right = False
        self.height = height
        self.width = width
        super().__init__(position, width, height, color)


    def update(self):
        if self.left == True:
            self.position.x = (self.position.x - 3) if self.position.x > 30 else 30 #TODO: dynamic min
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        if self.right == True:
            self.position.x = (self.position.x + 3) if self.position.x < 370 else 370 #TODO: dynamic max
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        self.left = False
        self.right = False
        super().update()
    
    def move_left(self):
        self.left = True

    def move_right(self):
        self.right = True

class Weak_Block(KineticBlock):
    def __init__(self, position, width, height, color):
        self.hp = 1
        super().__init__(position, width, height, color)

    def update(self):
        if self.touched_by_ball == True:
            print(self.hp)
        super().update()


class Strong_Block(KineticBlock):
    def __init__(self, position, width, height, color):
        self.hp = 3
        super().__init__(position, width, height, color)

    def update(self):
        if self.touched_by_ball == True:
            print(self.hp)
        super().update()
