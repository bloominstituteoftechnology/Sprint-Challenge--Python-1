import pygame
import random

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



class Paddle(KineticBlock):
    def __init__(self, position, width, height, color):
        self.left = False
        self.right = False
        self.height = height
        self.width = width
        super().__init__(position, width, height, color)

    def update(self):
        if self.left == True:
            self.position.x = (self.position.x - 3) if self.position.x > self.width/2 else self.width/2
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
            self.left = False
            
        if self.right == True:
            self.position.x = (self.position.x + 3) if self.position.x < 400-self.width/2 else 400-self.width/2
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
            self.right = False

        super().update()

class RegularBlock(KineticBlock):
    def __init__(self, object_list, position, width, height, color):
        self.object_list = object_list
        super().__init__(position, width, height, color)

    def update(self):
        if self.touched_by_ball == True:
            self.object_list.remove(self)
        super().update()


class StrongBlock(KineticBlock):
    def __init__(self, object_list, position, width, height, color):
        self.object_list = object_list
        self.hp = 5
        super().__init__(position, width, height, color)

    def update(self):
        if self.touched_by_ball == True:
            self.hp -= 1
            # self.color = [random.randint(100, 250), random.randint(100, 250), random.randint(100, 250)]
            color2 = [i+50 for i in self.color]
            self.color = color2 
            if self.hp == 0:
                self.object_list.remove(self)
            self.touched_by_ball = False
        super().update()