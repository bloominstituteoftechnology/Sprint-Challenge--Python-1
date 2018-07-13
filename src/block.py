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
    """
    Has a difficulty property that tells how many times 
    it needs to be hit before it disappears (from 1-5)
    """

    def __init__(self, position, width, height, color, difficulty):
        super().__init__(position, width, height, color)
        self.hits_left = difficulty
        self.defeated = False
        self.colors = [[255, 0, 0], [255,140,0], [255, 215, 0], [0, 255, 0]]
        self.color = self.colors[-difficulty]

    def check_collision(self):
        if self.touched_by_ball:
            self.hits_left -= 1
            self.color = self.colors[-self.hits_left]
        if self.hits_left == 0:
            self.defeated = True

class UnbreakableBlock(Block):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.color = [100, 100, 100]

class Paddle(Block):
    """ 
    Player controlled paddle at the bottom of the screen
    """

    def update(self, **kwargs):
        distance = 2
        for k, v in kwargs.items():
            if k == "left" and v == True:
                self.rectangle = self.rectangle.move(-distance, 0)
                self.position.x -= distance 
            if k == "right" and v == True:
                self.rectangle = self.rectangle.move(distance, 0)
                self.position.x += distance
