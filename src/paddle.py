import pygame

from pygame.math import Vector2
from pygame import Rect

from block import KineticBlock
from ball import GameBall
class Paddle:
    def __init__(self, x, y, clr, vel):
        self.x = x
        self.y = y
        self.height = PADDLE_HEIGHT
        self.width = PADDLE_WIDTH
        self.color = clr
        self.vel = vel

        self.is_moving = False
        self.direction = None


    def draw(self):
        leftx = self.x - self.width/2
        topy = self.y - self.height/2
        coords = pygame.Rect(leftx, topy, self.width, self.height)
        pygame.draw.rect(DISPLAYSURF, self.color, coords, 0)

    def move(self):
        if not self.is_moving:
            return

        if self.direction == UP and self.y - self.height/2 > 0:
            self.y -= self.vel 
        elif self.direction == DOWN and self.y + self.height/2 < SCREEN_HEIGHT:
            self.y += self.vel 