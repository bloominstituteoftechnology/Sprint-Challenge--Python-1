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
    """
    Base class for paddle object
    """

    def update(self, **input):
        SPEED = 3
        self.left = input['left']
        self.right = input['right']
        self.width = input['width']
        self.game_width = input['game_width']

        if self.left:
            if (self.position.x - (self.width // 2)) >= 0:
                self.position.x -= SPEED

        if self.right:
            if (self.position.x + (self.width // 2)) <= self.game_width:
                self.position.x += SPEED

        self.rectangle = pygame.Rect(
                                    self.position.x - (self.rectangle.width/2),
                                    self.position.y - (self.rectangle.height/2),
                                    self.rectangle.width,
                                    self.rectangle.height)
        super().update()

class BreakableBlock(KineticBlock):
    def update(self, **kwargs):
        if(self.touched_by_ball):
            #remove from the list
            kwargs['object_list'].pop(kwargs['object_list'].index(self))

class StrongBlock(BreakableBlock):
    def __init__(self, strength, position, width, height, color):
        self.strength = strength
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        if self.touched_by_ball:
            self.strength -= 1
            self.color = [0, 160, 0]
            if self.strength <= 0:
                super().update(object_list=kwargs['object_list'])
            else:
                self.touched_by_ball = False



    # def move_left(self):
    #     if self.position.x > (self.width / 2) + (PADDLE_MOVE_INCREMENT // 2):
    #         self.position.x -= PADDLE_MOVE_INCREMENT
    #         self.rectangle = pygame.Rect(
    #                         self.position.x - (self.width/2),
    #                         self.position.y - (self.height/2),
    #                         self.width,
    #                         self.height)

    # def move_right(self):
    #     if self.position.x < SCREEN_SIZE[0] - (self.width / 2) - (PADDLE_MOVE_INCREMENT // 2):
    #         self.position.x += PADDLE_MOVE_INCREMENT
    #         self.rectangle = pygame.Rect(
    #                         self.position.x - (self.width/2),
    #                         self.position.y - (self.height/2),
    #                         self.width,
    #                         self.height)

# class KineticPaddle(Paddle):
#     # No custom code needed here, just want to be able to differentiate
#     # KineticBall will handle the collison
#     pass
