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
          self.rectangle.x = self.bounds[0] - self.rectangle.width
        self.position.x = self.rectangle.x + self.rectangle.width/2

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
          if direction == 'left':
            self.rectangle.x -=10
          else:
            self.rectangle.x +=10
      super().update()

class Brick(KineticBlock):

    def __init__(self, object_list,bounds, position, width, height, color, hp):
      super().__init__(bounds, position, width, height, color)
      self.object_list = object_list
      self.hp = hp
      self.colors = {
        1 : [255, 181, 0],
        2 : [255, 165, 255],
        3 : [99, 179, 7],
        4 : [15, 151, 230]
      }
      self.color = self.colors[self.hp]

    def update(self, **kwargs):
      # for key, value in kwargs.items():
      if self.touched_by_ball == True:
        print('Touched ', self.hp)
        self.hp-=1
        if self.hp == 0:
          self.object_list.remove(self)
        else:
          self.color = self.colors[self.hp]
      super().update()

class Floor(KineticBlock):

    def __init__(self, object_list,bounds, position, width, height, color, lives):
      super().__init__(bounds, position, width, height, color)
      self.object_list = object_list
      self.lives = lives
      self.colors = {
        1 : [255, 181, 0],
        2 : [255, 165, 255],
        3 : [99, 179, 7],
        4 : [15, 151, 230]
      }
      self.color = self.colors[self.lives]

    def update(self, **kwargs):
      # for key, value in kwargs.items():
      if self.touched_by_ball == True:
        print('Dead ', self.lives)
        self.lives-=1
        if self.lives == 0:
          self.lives = 4
        else:
          self.color = self.colors[self.lives]
      super().update()
