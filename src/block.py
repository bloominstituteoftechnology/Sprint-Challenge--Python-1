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
                                    self.position.x - (width/2),
                                    self.position.y - (height/2),
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

class Paddle():
    def __init__(self, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.width = width
        self.height = height
        self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        self.color = color
        self.touched_by_ball = False

    def update(self):
        self.touched_by_ball = False
        if pygame.key.get_pressed()[pygame.K_LEFT] == True:
            print("left pressed")
            self.position.x += -3
            self.rectangle = pygame.Rect(
                                    self.position.x - 3 - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
            print("right pressed")
            self.position.x += 3
            self.rectangle = pygame.Rect(
                                    self.position.x + 3 - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)