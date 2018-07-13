import pygame

# from pygame.math import Vector2
# from pygame import Rect


class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.rectangle = pygame.Rect(
            position.x - (width / 2), position.y - (height / 2), width, height
        )
        self.width = width
        self.height = height
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
    """
    Class for the player paddle
    """

    def move_paddle(self, direction):

        if direction == "l" and self.position.x > self.width / 2:
            self.position.x -= 3
        elif direction == "r" and self.position.x < 400 - self.width / 2:
            self.position.x += 3
        self.rectangle = pygame.Rect(
            self.position.x - (self.width / 2),
            self.position.y - (self.height / 2),
            self.width,
            self.height,
        )


class BreakableBlock(KineticBlock):
    def __init__(self, position, width, height, color, hp):
        self.hp = hp
        self.orig_color = color
        color = [i * hp for i in color]
        super().__init__(position, width, height, color)

    def got_hit(self):
        self.hp -= 1
        self.color = [i * self.hp for i in self.orig_color]
