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
    def __init__(self, position, width, height, color, hits):
        super().__init__(position, width, height, color)
        self.hits_to_break = hits
        self.broken = False
        self.colors = [[255, 0, 0], [255,140,0], [0, 255, 0]]
        self.color = self.colors[-hits]
    
    def check_collision(self):
        if self.touched_by_ball:
            self.hits_to_break -= 1
            self.color = self.colors[-self.hits_to_break]
        if self.hits_to_break == 0:
            self.broken = True

class UnbreakableBlock(Block):
    #This a block that is bounceable but not breakable
    
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.color = [75, 75, 75]

class GhostBlock(Block):
    #The block is destroyed when hit but the ball can't bounce off of it
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)
        self.color = [200, 200, 200]
        self.broken = False
    
    def check_collision(self):
        if self.touched_by_ball:
            self.broken = True
        
class Paddle(KineticBlock):
    #this is the paddle that the player controls at the bottom of the screen

    def update(self, **kwargs):
        distance = 2
        for k, v in kwargs.items():
            if k == "left" and v == True:
                self.rectangle = self.rectangle.move(-distance, 0)
                self.position.x -= distance
            if k == "right" and v == True:
                self.rectangle = self.rectangle.move(distance, 0)
                self.position.x += distance
        

        if self.left:
            self.position.x -= self.SPEED
        
        if self.right:
            self.position.x += self.SPEED

        self.rectangle = pygame.Rect(
            self.position.x - (self.rectangle.width/2),
            self.position.y - (self.rectangle.height/2),
            self.rectangle.width,
            self.rectangle.height
        )
        super().update()

class EasyBlock(KineticBlock):
    def update(self, **kwargs):
        if self.touched_by_ball:
            kwargs['object_list'].pop(kwargs['object_list'].index(self))


class HardBlock(EasyBlock):
    def __init__(self, life, position, width, height, color):
        self.life = life
        super().__init__(position, width, height, color)

    rand_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]

    def update(self, **kwargs):
        if self.touched_by_ball:
            self.life -= 1
            self.color = self.random_color
            if self.life <= 0:
                super().update(object_list = kwargs['object_list'])
            else:
                self.touched_by_ball = False