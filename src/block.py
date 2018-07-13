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
        self.steps = 20

    def update(self, **kwargs):
        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)


class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    def movePaddle(self, direction, SCREEN_WIDTH):
        print('movePaddle METHOD', direction)
        print(self.rectangle[0], SCREEN_WIDTH)
        if direction == 'RIGHT':
            print(self.rectangle[0] + self.steps)
            if self.rectangle[0] + self.steps > SCREEN_WIDTH:
                print(True)
                self.rectangle[0] = 0
            else:
                print(False)
                self.rectangle[0] += self.steps
        if direction == 'LEFT':
            if self.rectangle[0] - self.steps < 0:
                self.rectangle[0] = SCREEN_WIDTH
            else:
                self.rectangle[0] -= self.steps
