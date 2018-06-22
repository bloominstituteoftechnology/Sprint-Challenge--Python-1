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
        print('rect: ', self.rectangle)
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class PaddleBlock(KineticBlock):

    def __init__(self, position, width, height, color, velocity):
        self.position = position
        self.rectangle = pygame.Rect(
                                    position.x - (width/2), # TODO: x-coord should move according to left/right keys
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.velocity = velocity
        self.touched_by_ball = False
        super().__init__(position, width, height, color)
    
    def paddle_to_left(self):

        # Update x position
        # Check for bounds conflict
        if self.position.x < self.velocity:
            return
        self.position.x -= self.velocity

        # Update rectangle's x-coordinate
        self.rectangle[0] = self.position.x
    
    def paddle_to_right(self, paddle_width, screen_width):

        # Update x position
        # Check for bounds conflict
        if (self.position.x + paddle_width)  + self.velocity > screen_width:
            return
        self.position.x += self.velocity

        # Update rectangle's x-coordinate
        self.rectangle[0] = self.position.x

