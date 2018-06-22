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
        #screen.fill((255, 255, 255))
        #self.rect = self.rect.move(width=self.dist, height=self.dist)
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
    pass

class Paddle(KineticBlock):
    '''
    def player(self, direction, width):
        if direction == 'left':
            self.position.x - 1
        if direction == 'right':
            self.position.x + 1
'''
    SPEED = 3
    def update(self, **input):
        self.left = input['left']
        self.right = input['right']

        if self.left:
            self.position.x -= SPEED
            #TODO: add screen bounds
        if self.right:
            self.position.y += SPEED
            #TODO: add screen bounds
        self.rectangle = pygame.Rect(
                                    self.position.x - (self.rectangle.width/2),
                                    self.position.y - (self.rectangle.height/2),
                                    self.rectangle.width,
                                    self.rectangle.height)
        
        super().update()

class BreakableBlock(KineticBlock):
    # how is this different?
    # a block that the ball bounces off of, that vanishes after the ball touches it 
    # if touched_by_ball = true then remove from object_lists list
    # to do this here, we need two things 1, we need to be able to see object_list
    # two, we need a different update that will make this happen 

    def update(self, **kwargs):
        if(self.touched_by_ball):
            # remove from the list
            kwargs['object_list'].pop(kwargs['object_list'].index(self))

class StrongBlock(BreakableBlock):
    def __init__(self, strength, position, width, height, color):
        self.strength = strength
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        self.strength -= 1
        if self.touched_by_ball:
            self.strength -= 1
            self.color = [255, 0, 0] #TODO: fix lazy hack 
            if self.strength <= 0:
                super.update(object_list=kwargs['object_list'])
            else:
                self.touched_by_ball = False
