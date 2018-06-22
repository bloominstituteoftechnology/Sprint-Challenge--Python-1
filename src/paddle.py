from block import *
from pygame.math import Vector2

class Paddle(KineticBlock):
    """
    Defines the paddle at the bottom of the screen that is controlled by the player.
    """
    def __init__(self, screenwidth, screenheight):
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        width = 100
        height = 25
        y = self.screenheight - height - 2

        KineticBlock.__init__(self, Vector2(0, y), width, height, [0, 0, 255])

    def update(self, **kwargs):
        self.touched_by_ball = False  

        for key in kwargs:
            if key == 'move' and kwargs[key] == 'left':
                self.rectangle.x -= 5
                self.position.x -= 5
            if key == 'move' and kwargs[key] == 'right':
                self.rectangle.x += 5
                self.position.x += 5

        if self.rectangle.x <= 0:
            self.rectangle.x = 0

        if self.rectangle.x > self.screenwidth - self.rectangle.width:
            self.rectangle.x = self.screenwidth - self.rectangle.width

    def check_collision(self):
        pass