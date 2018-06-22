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

        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rect.x = 0
        self.rect.y = self.screenheight-self.height

    def check_collision(self):
        pass

    def draw(self, screen, pygame):
        color = (0, 0, 0)
        pygame.draw.rect(screen, color, self.rect)

    def update(self, **kwargs):
        """ Update the player position. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
