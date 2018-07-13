import pygame

from pygame.math import Vector2
from pygame import Rect

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
        if self.rectangle.x < 0:
          self.rectangle.x = 0
        if self.rectangle.x > self.bounds[0] - self.rectangle.width:
          print(self.rectangle.x)
          self.rectangle.x = self.bounds[0] - self.rectangle.width

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class Paddle(KineticBlock):

    def update(self, **kwargs):
      for direction, value in kwargs.items():
        if value == True:
          print(self.rectangle)
          if direction == 'left':
            self.rectangle.x -=10
          else:
            self.rectangle.x +=10
      super().update()


