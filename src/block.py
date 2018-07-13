import pygame
import random

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
class PaddleBlock(KineticBlock):
    def __init__(self, object_list, position, width, height, color):
        self.object_list = object_list
        super().__init__(position, width, height, color)
    def update(self, **kwargs):
        self.touched_by_ball = False
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_LEFT]:
            self.rectangle.move_ip(-5, 0)
            self.position.x -= 5
        elif key[pygame.K_RIGHT]:
            self.rectangle.move_ip(5,0)
            self.position.x += 5

class GameBlock(PaddleBlock, KineticBlock):
    def __init__(self, margin, difficulty, object_list, position, width, height, color):
        self.margin = margin
        self.difficulty = difficulty
        super().__init__(object_list, position, width, height, color)

    def update(self, **kwargs):
        RANDOM_R = random.randint(125, 175)
        RANDOM_B = random.randint(175, 255)
        RANDOM_G = random.randint(25, 255)
        if self.touched_by_ball == True:
            if self.difficulty == 0:
                self.object_list.remove(self)
            else:
                self.difficulty -= 1
                self.color = [RANDOM_R, RANDOM_G, RANDOM_B]
                print(self.difficulty)
        self.touched_by_ball = False


        



