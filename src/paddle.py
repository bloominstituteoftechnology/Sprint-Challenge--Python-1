import pygame

from pygame.math import Vector2
from pygame import Rect

class Paddle:
    """
    Base class for Paddle
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
        
    def moveLeft(self, position):
        # THIS IS NOT WORKING - MORE PSUEDOISH STUFF
        self.position.x -= 5
        if (self.position.x < 0): 
            self.position.x = 0
        
    def moveRight(self, position, width):
        # THIS IS ALSO NOT WORKING - le sigh
        self.position.x += 5
        if self.position.x > screen.x - self.width: # out-of-bounds
            self.position.x = screen.x

class KineticPaddle(Paddle):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass


