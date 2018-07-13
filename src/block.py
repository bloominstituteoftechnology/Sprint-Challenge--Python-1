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
        # print(kwargs['left'])

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class Paddle(KineticBlock):
    pass
    def update(self, **kwargs):
        # print(kwargs['right'])
        left = kwargs['left']
        right = kwargs['right']
        if left:
            # print(self.rectangle.x)
            self.rectangle.x -= 10 
            self.position.x -= 10 
        elif right:
            self.rectangle.x += 10
            self.position.x += 10 
        super().update()
        
class Breakable(KineticBlock):
    def update(self, **kwargs):
        # print(kwargs['list'].index(self))
        if self.touched_by_ball:
            kwargs['list'].pop(kwargs['list'].index(self))

class HarderToBreak(KineticBlock):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.hits = 2
        print(self.hits)
    def update(self, **kwargs):
        
        if self.touched_by_ball and self.hits == 0:
            kwargs['list'].pop(kwargs['list'].index(self))
        elif self.touched_by_ball and self.hits > 0:
            self.hits -= 1
            self.touched_by_ball = False
            self.color[1] += 50 