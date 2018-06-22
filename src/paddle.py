import pygame
from pygame.math import Vector2
from pygame import Rect

Screen_SIZE = [400, 800]
PADDLE_MOVE_INCREMENT = 3

class Paddle:
  def __init__(self, position, width, height, color):
    self.position = positionself.rectangle = pygame.Rect(
      position.x - (width/2),
      position.y - (height/2),
      width,
      height
    )
    self.color = color
    self.touched_by_ball = False
    self.height = height

  def update(self, **kwargs):
    self.touched_by_ball = False

  def check_collision(self):
    pass

  def draw(self, screen, pygame):
    pygame.draw.rect(screen, self.color, self.rectangle)

  def move_left(self):
    if self.position.x > (self.width / 2 ) + (PADDLE_MOE_INCREMENT // 2):
      self.position.x -= PADDLE_MOVE_INCREMENTself.rectangle = pygame.Rect(
        self.position.x - (self.width/2),
        self.position.y - (self.height/2),
        self.width,
        self.height
      )

  def move_right(self):
    if self.position.x < Screen_SIZE[0] - (self.width / 2) - (PADDLE_MOVE_INCREMENT // 2):
      self.position.x += PADDLE_MOVE_INCREMENT
      self.rectangle = pygame.Rect(
        self.position.x - (self.width/2),
        self.potition.y - (self.height/2),
        self.width,
        self.height
      )



