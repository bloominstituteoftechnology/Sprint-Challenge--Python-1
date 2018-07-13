import pygame

from pygame.math import Vector2
from pygame import Rect

class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, position, width, height, color, obj_list):
        self.obj_list = obj_list
        self.position = position
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.touched_by_ball = False
        self.touch_count = 0

    def update(self, **kwargs):
        if self.touch_count == 3:
           self.obj_list.remove(self)

        if self.touch_count == 2:
           self.color = [111,30,200]
           
        if self.touched_by_ball == True:
           self.color = [56,0,240]
           self.touch_count += 1

        if len(self.obj_list) == 2:
            pygame.quit()

        self.touched_by_ball = False

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticBlock(Block):
    pass

class Paddle(KineticBlock):
    def __init__(self, position, width, height, color, obj_list):
        self.left = False
        self.right = False
        self.height = height
        self.width = width
        super().__init__(position, width, height, color, obj_list)


    def update(self):
        if self.touched_by_ball == True:
            self.color = [0,0,0]

        self.touched_by_ball = False
        if self.left == True:
            self.position.x = (self.position.x - 3) if self.position.x > 80 else 80
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        if self.right == True:
            self.position.x = (self.position.x + 3) if self.position.x < 560 else 560
            self.rectangle = pygame.Rect(
                                    self.position.x - (self.width/2),
                                    self.position.y - (self.height/2),
                                    self.width,
                                    self.height)
        self.left = False
        self.right = False
        super().update()
    
    def move_left(self):
        self.left = True

    def move_right(self):
        self.right = True