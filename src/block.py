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

class PlayerBlock(Block):
    def __init__(self, position, width, height, color):
        self.position = position
        self.rectangle = pygame.Rect(
                            position.x - (width/2),
                            position.y - (height/3),
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

    def moveRight(self, position):
        self.position.x += position
        self.rectangle[0] += position
        return self.position.x

    def moveLeft(self, position):
        self.position.x -= position
        self.rectangle[0] -= position
        print(self.rectangle[0])
    
        return self.position.x

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass


