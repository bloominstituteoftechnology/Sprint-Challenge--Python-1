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
        self.width = width


    def update(self, **kwargs):
        self.touched_by_ball = False
        print('its happening')

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    def update(self, **kwargs):
        self.touched_by_ball = False
        mouse_pos = pygame.mouse.get_pos()
        self.position.x = mouse_pos[0]
        self.rectangle[0] = mouse_pos[0] - self.width/2


