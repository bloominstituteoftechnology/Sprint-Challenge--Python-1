import pygame
import random


from pygame.math import Vector2
from pygame import Rect


def rgb_color():
       return [random.randint(50, 255),random.randint(50, 255),random.randint(50, 255)]


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
        # if self.touched_by_ball: # Sanity Check to check that this is working
        #     print("CONTACT MADE!")
        self.touched_by_ball = False
        self.moving = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison
   
    pass

class Paddle(KineticBlock):
    # What do we need to do to our paddle to make it work?
    # Move left and right - change x axis
    # Stay in the screen
    # Based off of input that we gather in draw.py
    # We need to be able to see keypresses here

    # Override update and make use of keyword arguements aspect:
    SPEED = 10 # 
    def update(self, **input): # Look into this - **kwargs and **input options???
        self.left = input['left']
        self.right = input['right']
        self.up = input['up']
        self.down = input['down']
        if self.left:
            self.position.x -= self.SPEED # Since this is a `class level variable`, you need `self`
            # TODO: Add screen bounds
        if self.right: 
            self.position.x += self.SPEED
            # TODO: Add screen bounds
        if self.up:
                self.position.y -= self.SPEED # Since this is a `class level variable`, you need `self`
            # TODO: Add screen bounds
        if self.down: 
            self.position.y += self.SPEED
            # TODO: Add screen bounds 
        self.rectangle = pygame.Rect( # move the actual rectangle.
                                    self.position.x - (self.rectangle.width/2),
                                    self.position.y - (self.rectangle.height/2),
                                    self.rectangle.width,
                                    self.rectangle.height)
        super().update()
    
    pass

class BreakableBlock(KineticBlock):
    # How is this different? - It needs to know whether it has been touched or not?
    # e.g. self.touched_by_ball
    # A block that the ball bounces off of, that vanishes after the ball touches it
    # if touched_by_ball = true then remove the object_lists list
    # To do this here, we need to things: 1. we need to be able to see object_list
    # and 2. We need a different update that will make this happen.

    def update(self, **kwargs):
        if(self.touched_by_ball):
            # remove from the list
            kwargs['object_list'].pop(kwargs['object_list'].index(self))
    pass

class StrongBlock(BreakableBlock):
    def __init__(self, strength, position, width, height, color):
        self.strength = strength
        super().__init__(position, width, height, color)

    # Overrides update
    def update(self, **kwargs):
        if self.touched_by_ball:
            self.strength -= 1
            self.color = rgb_color() #TODO: Fix lazy hack
            if self.strength <= 0:
                kwargs['object_list'].pop(kwargs['object_list'].index(self)) # Avoids rewriting remove code from earlier
            else:
                self.touched_by_ball = False

    pass


