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
    def update(self, **kwargs):
        self.touched_by_ball = False
        
        
        if kwargs is not None:
            print(kwargs)
            print(self.position.x)
            if kwargs["left"] == True:
                self.position.x = self.position.x - 5    
            elif kwargs["right"] == True:
                self.position.x = self.position.x + 5
            else:
                pass
            
            if self.position.x < 600 and self.position.x > 40:
                self.rectangle = pygame.Rect(
                                        self.position.x - (50/2),
                                        self.position.y - (25/2),
                                        50,
                                        25)

class BreakBlock(Block):
    def update(self, **kwargs):
        self.touched_by_ball = True