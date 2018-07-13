import pygame

from pygame.math import Vector2
from pygame import Rect


class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, position, width, height, color):
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
    """
    Block that is collidable
    """
    # KineticBall will handle the collison
    pass


class Paddle(KineticBlock):
    def __init__(self, bounds, speed, position, width, height, color):
        super().__init__(position, width, height, color)
        self.bounds = bounds
        self.speed = speed

    def update(self, **kwargs):
        if kwargs['left'] and self.rectangle.left - self.speed >= 0:
            self.rectangle.move_ip(-self.speed, 0)
            self.position.x = self.rectangle.centerx
            self.position.y = self.rectangle.centery
                
        if kwargs['right'] and self.rectangle.right + self.speed <= self.bounds[0]:
            self.rectangle.move_ip(self.speed, 0)
            self.position.x = self.rectangle.centerx
            self.position.y = self.rectangle.centery

        super().update()


class Brick(KineticBlock):
    def __init__(self, object_list, value, position, width, height, color):
        super().__init__(position, width, height, color)
        self.object_list = object_list
        self.value = value
    
    def update(self, **kwargs):
        if self.touched_by_ball:
            self.destroy()
        super().update()
    
    def destroy(self):
        self.object_list.remove(self)