import pygame

from pygame.math import Vector2
from pygame import Rect

SCREEN_SIZE = [400, 800]
PADDLE_MOVE_INCREMENT = 3

class Paddle:
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
        self.width = width
        self.height = height


    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

    def move_left(self):
        if self.position.x > (self.width / 2) + (PADDLE_MOVE_INCREMENT // 2):
            self.position.x -= PADDLE_MOVE_INCREMENT
            self.rectangle = pygame.Rect(
                            self.position.x - (self.width/2),
                            self.position.y - (self.height/2),
                            self.width,
                            self.height)


    def move_right(self):
        if self.position.x < SCREEN_SIZE[0] - (self.width / 2) - (PADDLE_MOVE_INCREMENT // 2):
            self.position.x += PADDLE_MOVE_INCREMENT
            self.rectangle = pygame.Rect(
                            self.position.x - (self.width/2),
                            self.position.y - (self.height/2),
                            self.width,
                            self.height)

class KineticPaddle(Paddle):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass


