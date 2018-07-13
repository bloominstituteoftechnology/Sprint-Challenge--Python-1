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
    pass

class Paddle(KineticBlock):
    def __init__(self, position, width, height, color):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.direction = 0
        self.speed = 5
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)

    def update(self):
        """
        Move paddle if the left or right key is held down. Do not allow
        paddle to move out of bounds.
        """
        # Handling movement of paddle
        self.position.x += self.direction
        
        # Making sure paddle does not go out of bounds
        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > 300:
            self.position.x = 300

        super().update()