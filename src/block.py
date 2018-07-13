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

class PlayerPaddle(Block):
    def __init__(self, bounds, position, width, height, color):
        super().__init__(position, width, height, color)
        self.bounds = bounds
        
    def update(self, **kwargs):
        super().update()
        left = kwargs['left'] if 'left' in kwargs else None
        right = kwargs['right'] if 'right' in kwargs else None
        speed = 10
        
        if left:
            print('left' if left else 'nah')
            self.rectangle.move_ip(speed * -1, 0)
            if self.rectangle.centerx < 0 + self.rectangle.width / 2:
                self.rectangle.centerx = 0 + self.rectangle.width / 2
        elif right:
            print('right' if right else 'nah')
            self.rectangle.move_ip(speed, 0)
            if self.rectangle.centerx > self.bounds[0] - self.rectangle.width / 2:
                self.rectangle.centerx = self.bounds[0] - self.rectangle.width / 2