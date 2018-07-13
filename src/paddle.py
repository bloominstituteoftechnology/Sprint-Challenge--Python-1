import pygame
from pygame.math import Vector2
from pygame import Rect

class Paddle:
    def __init__(self, position, width, height, color):
         self.position = position
         self.rect = pygame.Rect(position.x - (width/2), position.y -(height/2), width, height)
         self.color = color

    def update(self, right, left):
        self.touched_by_ball = False
        if right:
            print("hold,fire")
            self.rect.x += 3
        if left:
            print("shoot")
            self.rect.x -= 3

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rect)
