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


    def update(self, *args):
        self.touched_by_ball = False
        if args[0]:
            self.rectangle.x -= 4
        if args[1]:
            self.rectangle.x += 4

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class DestructableBlock(KineticBlock):
    def __init__(self, object_list, position, width, height, color):
        self.object_list = object_list
        self.touched_by_ball = False
        self.color = color
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.position = position

    def update(self, *args):
        if self.touched_by_ball:
            for object in self.object_list:
                if object == self:
                    self.object_list.remove(object)
                else:
                    continue

class NotSoDestructableBlock(DestructableBlock):
    
    def __init__(self, object_list, position, width, height, color):
        self.counter = 3
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.touched_by_ball = False
        self.color = color
        self.object_list = object_list
        self.position = position

        super()
    
    def update(self, *args):
        if self.touched_by_ball and self.counter == 0:
            for object in self.object_list:
                if object == self:
                    self.object_list.remove(object)
                else:
                    continue
        elif self.touched_by_ball and self.counter != 0:
            self.counter -= 1
            self.touched_by_ball = False

class AbsolutelyPositivelIndustructibleBlock(KineticBlock):
    
    def __init__(self, position, width, height, color):
        KineticBlock.__init__(self, position, width, height, color)
    
        self.position = position
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.touched_by_ball = False
    
    def update(self, *args):
        "x"

#class paddle