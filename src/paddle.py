import pygame

from pygame.math import Vector2
from pygame import Rect

class Paddle:
    """
    Base class for paddle object
    """

    def __init__(self, position, dx, width, height, color):
        # Create a rectangle centered around the x and y
        self.position = position
        self.dx = dx
        self.rectangle = pygame.Rect(
                                    position.x - (width/2),
                                    position.y - (height/2),
                                    width,
                                    height)
        self.color = color
        self.touched_by_ball = False


    def update(self, **kwargs):
        self.touched_by_ball = False

        self.position.x += self.dx
        # if self.position.x < 0 or self.position.x > 640: # screen width
        #     self.position.x *= -1
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     # Do something
        #     # object_list[5].update()
        #     self.position.x = self.position.x -5
        #     print(self.position.x)
        #     #pass
        # if keys[pygame.K_RIGHT]:
        #     # Do something
        #     self.position.x = self.position.x + 5
        #     print(self.position.x)

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class KineticPaddle(Paddle):
    # No custom code needed here, just want to be able to differentiate
    # KineticBall will handle the collison

    pass


