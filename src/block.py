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
        self.collision_count = 0


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

    SPEED = 3 #pixels per frame

    def update(self, **kwargs):
        left = kwargs['left']
        right = kwargs['right']

        if left:
            self.position.x -= self.SPEED
        if right:
            self.position.x += self.SPEED

        self.rectangle = pygame.Rect(
            self.position.x - (self.rectangle.width/2),
            self.position.y - (self.rectangle.height/2),
            self.rectangle.width,
            self.rectangle.height,
        )
    

class EzBlock(KineticBlock):
    def __init__(self, object_list, position, width, height, color):
        self.object_list = object_list
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        if self.collision_count == 2:
            self.color = [255,69,0]
            self.object_list.remove(self)

        # if self.collision_count == 2:
            
        if self.touched_by_ball == True:
            self.color = [255,255,0]
            self.collision_count += 1
        self.touched_by_ball = False
    
class HardBlock(KineticBlock):
    def __init__(self, object_list, position, width, height, color):
        self.object_list = object_list
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        if self.collision_count == 3:
            self.object_list.remove(self)

        if self.collision_count == 2:
            self.color = [255,69,0]
            
        if self.touched_by_ball == True:
            self.color = [255,255,0]
            self.collision_count += 1
        self.touched_by_ball = False

class BeejBlock(KineticBlock):
    def __init__(self, object_list, bounds, position, width, height, color):
        self.object_list = object_list
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
        if self.touched_by_ball:
            self.object_list.remove(self)