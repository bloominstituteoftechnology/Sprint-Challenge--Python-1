import pygame

from pygame.math import Vector2
from pygame import Rect

from block import KineticBlock
from ball import GameBall

# paddle global variables

SCREEN_HEIGHT = 800
class Paddle:
    def __init__(self, width, height, color, position):
        self.x = width
        self.y = height
        self.color = color
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.position = position                            

        self.is_moving = False
        self.direction = None


    def draw(self):
        pygame.draw.rect(self.color, self.rectangle)
    #TODO: Need to refactor the move code 
    # def move(self):
    #     if not self.is_moving:
    #         return

    #     if self.direction == self.y - self.height/2 > 0:
    #         self.y -= self.vel 
    #     elif self.direction == self.y + self.height/2 < SCREEN_HEIGHT:
    #         self.y += self.vel 