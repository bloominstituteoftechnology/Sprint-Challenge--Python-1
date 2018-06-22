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
        # self.draw_paddle = paddle
        self.touched_by_ball = False


    def update(self, **kwargs):
        self.touched_by_ball = False
        self.paddle = True
    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)
    # def drawPaddle(self, paddle, screen, pygame):
    #     pygame.draw.rect(screen, self.color, self.rectangle, self.paddle)
    def draw_paddle(self, paddle):
        x = 100
        y = 100
        width = 80
        height = 10
        
class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass


