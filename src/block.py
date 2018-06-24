import pygame
import random

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
            height
        )
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
    # KineticBall will handle the collision
    pass


class Paddle(KineticBlock):

    SPEED = 5

    def update(self, **kwargs):
        self.left = kwargs["left"]
        self.right = kwargs["right"]

        # keeps paddle in bounds on left
        if self.left and self.position.x - self.rectangle.width/2 - 10 >= 0:  # -10 gives left gutter
            self.position.x -= self.SPEED

        # keeps paddle in bounds on right
        if self.right and self.position.x + self.rectangle.width/2 + 10 <= 400:  # +10 gives right gutter
            self.position.x += self.SPEED

        self.rectangle = pygame.Rect(
            self.position.x - (self.rectangle.width/2),
            self.position.y - (self.rectangle.height/2),
            self.rectangle.width,
            self.rectangle.height
        )
        super().update()


class BreakableBlock(KineticBlock):

    def update(self, **kwargs):

        if self.touched_by_ball:
            kwargs['object_list'].pop(kwargs['object_list'].index(self))


class StrongBlock(BreakableBlock):

    random_color = [random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)]

    def __init__(self, position, width, height, color, strength):
        self.strength = strength
        self.block_deduction = 1/strength
        super().__init__(position, width, height, color,)

    def update(self, **kwargs):
        if self.touched_by_ball:
            self.strength -= 1
            self.color = self.random_color
            # decrease block's height by amount of strength everytime the block is hit
            self.rectangle.height = self.rectangle.height - \
                self.rectangle.height * self.block_deduction

            if self.strength <= 0:
                super().update(object_list=kwargs['object_list'])

            else:
                self.touched_by_ball = False
