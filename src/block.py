import pygame

from pygame.math import Vector2
from pygame import Rect

white = (255, 255, 255)

class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, bounds, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.bounds = bounds
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

class PlayerBlock(KineticBlock):
    VEL = 7

    def update(self, left, right):
        self.left = left
        self.right = right

        if self.left:
            self.position.x -= self.VEL
        if self.right:
            self.position.x += self.VEL
        self.rectangle = pygame.Rect(
            self.position.x - (self.rectangle.width/2),
            self.position.y - (self.rectangle.height/2),
            self.rectangle.width,
            self.rectangle.height)
        super().update()   

class SingleHit(KineticBlock):
    pass
    def __init__(self, object_list, bounds, position, width, height, color):
        self.object_list = object_list
        super().__init__(bounds, position, width, height, color)

    def update(self, **kwargs):
        if self.touched_by_ball:
            self.object_list.remove(self)

class MultiHit(KineticBlock):
    def __init__(self, object_list, bounds, position, width, height, color):
        self.object_list = object_list
        super().__init__(bounds, position, width, height, color)
        self.hits = 2
    def update(self, **kwargs):
        
        if self.touched_by_ball and self.hits == 0:
            self.object_list.remove(self)
        elif self.touched_by_ball and self.hits > 0:
            self.hits -= 1
            self.touched_by_ball = False
            self.color[1] -= 50     
                