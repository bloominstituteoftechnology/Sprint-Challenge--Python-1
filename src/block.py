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
    
class Paddle(KineticBlock)
    SPEED = 4

    def update(self, **input):
        self.left = input['left']
        self.right = inmput['right']

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

    random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]

    def update(self, **kwargs):
        if self.touched_by_ball:
            self.life -= 1
            self.color = self.random_color
            if self.life <= 0:
                super().update(object_list = kwargs['object_list'])
            else:
                self.touched_by_ball = False