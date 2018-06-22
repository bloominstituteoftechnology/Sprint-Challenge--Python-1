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
        if self.touched_by_ball:
            print('stop touching me!')
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

    SPEED = 3

    def update(self, **input):
        self.left = input['left']
        self.right = input['right']

        if self.left:
            self.position.x -= self.SPEED
            # TODO: Add screen bounds
        if self.right:
            self.position.x += self.SPEED
            # TODO: Add screen bounds
        self.rectangle = pygame.Rect(
            self.position.x - (self.rectangle.width/2),
            self.position.y - (self.rectangle.height/2),
            self.rectangle.width,
            self.rectangle.height)
        super().update()


class BreakableBlock(KineticBlock):
    # how is this different?
    # if touched_by_ball = true then remove from object_lists list
    # To do this here, we need two things 1, we need to able to see object_list
    # Two, we need a different update that will make this happen
    def update(self, **kwargs):
        if(self.touched_by_ball):
            # remove from the list
            kwargs['object_list'].pop(kwargs['object_list'].index(self))


class StrongBlock(BreakableBlock):
    def __init__(self, strength, position, width, height, color):
        self.strength = strength
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        if self.touched_by_ball:
            self.strength -= 1
            self.color = [255, 0, 0]  # TODO: Fix lazy hack
            if self.strength <= 0:
                super().update(object_list=kwargs['object_list'])
            else:
                self.touched_by_ball = False
