import math
import pygame


class Paddle():
    """ The paddle at the bottom that the
    player controls. """

    def __init__(self):
        super().__init__()

        self.width = 100
        self.height = 20
        self.image = pygame.Surface([self.width, self.height])

        self.rectangle = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rectangle.x = 0
        self.rectangle.y = self.screenheight-self.height

        self.touched_by_ball = True

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        color = (0, 0, 0)
        pygame.draw.rect(screen, color, self.rectangle)

    def update(self, **kwargs):
        """ Update the player position. """
        pos = pygame.mouse.get_pos()
        self.rectangle.x = pos[0]
        if self.rectangle.x > self.screenwidth - self.width:
            self.rectangle.x = self.screenwidth - self.width

        self.touched_by_ball = True


class KineticPaddle(Paddle):
    pass
