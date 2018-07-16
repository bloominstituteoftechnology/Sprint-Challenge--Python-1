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
        self.width = width
        self.height = height
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

class RegularBlock(KineticBlock):
    def __init__(self, position, width, height, color, object_list):
        self.object_list = object_list
        super().__init__(position, width, height, color)
        self.hit = 0

    def check_collision(self):
        if self.touched_by_ball == True:
            self.object_list.remove(self)

#This went through a lot of variations before it became this final product. I decided to use object_list.remove(self) to remove the regular blocks.
#But then I got errors, because I wasn't passing the object_list attr in my def __init__. So I added that.
#When I included object_list in the super().__init__, it gave me errors. When I took it out, it worked fine.

class RainbowBlock(RegularBlock):
    def __init__(self, position, width, height, color, object_list):
        self.object_list = object_list
        super().__init__(position, width, height, color, object_list)

    def check_collision(self):
        if self.touched_by_ball == True:
            self.hit += 1
            if self.hit == 1:
                self.color = [100, 100, 100]
            if self.hit == 2:
                self.color = [0, 0, 0]
            if self.hit == 3:
                self.color = [255, 255, 0 ]
            if self.hit == 4:
                self.color = [255, 0, 255]
            if self.hit >= 5:
                self.object_list.remove(self)

# The RainbowBlock requires object_list in both the def __init__ and super().init__, unlike the RegularBlock. 
# Maybe someday I'll figure out why they're different in this way, but for now I just do what the compiler tells me.
# The above allows the Rainbow Block to take a certain number of hits before vanishing, and changes the color each time it is hit.

class Paddle(KineticBlock):
    def __init__(self, position, width, height, color):
        super().__init__(position, width, height, color)

    def update(self, **kwargs):
# I got the kwargs from line 25. I'm still not 100% clear on this but it works so I left it in.
        self.rectangle = pygame.Rect(
                                self.position.x - (self.width/2),
                                self.position.y - (self.height/2),
                                self.width,
                                self.height)
        super().update()
# I copied this from the top - lines 16-20. The paddle is basically just like all the other blocks, except it moves.
# And has different dimensions. 
# Resource for pygame.Rect: https://stackoverflow.com/questions/30939830/argument-must-be-rect-style-object
# This advice was invaluable and helped me understand what is going on a little better.
