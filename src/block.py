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


class BreakableBlock(KineticBlock):
    def __init__(self, object_list, bounds, position, width, height, color):
        self.object_list = object_list
        super().__init__(position, width, height, color)
        self.breakable = True

    def update(self, **kwargs):
         if self.touched_by_ball:
              self.object_list.remove(self)



# class LessBrittleBlock(BreakableBlock):
#     def __init__(self, position, width, height, color):
#         super().__init__(position, width, height, color)
#         self.hits = 0


#     def update(self, **kwargs):
#         # if self.touched_by_ball and self.hits < 1:
        #     self.hits += 1
        #     self.color = [5, 22, 20]
        #     self.touched_by_ball = False
        #   if self.touched_by_ball:
        #       self.rectangle.width = 0
        #       self.rectangle.height = 0



class Paddle(KineticBlock):
    def __init__(self, bounds, position, width, height, color):
        super().__init__(position, width, height, color)
        self.bounds = bounds

    def update(self, **kwargs):
        left = kwargs['left']
        right = kwargs['right']
        speed = 11

        if left:
            self.position.x -= speed
            if self.position.x < 0 + self.rectangle.width / 2:
                self.position.x = 0 + self.rectangle.width / 2
        elif right:
            self.position.x += speed
            if self.position.x > self.bounds[0] - self.rectangle.width / 2:
                self.position.x = self.bounds[0] - self.rectangle.width / 2
        self.rectangle = pygame.Rect(
            self.position.x - (self.rectangle.width/2),
            self.position.y - (self.rectangle.height/2),
            self.rectangle.width,
            self.rectangle.height,
        )
        super().update()