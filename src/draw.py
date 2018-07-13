import pygame
import random
import sys

from pygame.math import Vector2
from ball import GameBall
from block import KineticBlock, Paddle


class GameManager:
    def __init__(self):
        # Game settings
        self.SCREEN_SIZE = [800, 400]
        self.BACKGROUND_COLOR = [0, 0, 0]
        self.GAMEBALL_START_POS = Vector2(
            random.randint(20, self.SCREEN_SIZE[0] - 20),
            random.randint(40, self.SCREEN_SIZE[1] - 40)
        )
        self.GAMEBALL_VELOCITY = Vector2(5, 5)
        self.GAMEBALL_SIZE = 8
        self.GAMEBALL_COLOR = [255, 10, 0]
        self.PADDLE_START_POS = Vector2(459, 380)
        self.PADDLE_SPEED = 5
        self.PADDLE_SIZE = [34, 8]

        self.object_list = []

    def build_level(self):
        # TODO: Create game blocks: reg block, multi hit block
        gameball = GameBall(1, self.object_list, self.SCREEN_SIZE, self.GAMEBALL_START_POS,
                            self.GAMEBALL_VELOCITY, self.GAMEBALL_COLOR, self.GAMEBALL_SIZE)
        paddle = Paddle(self.SCREEN_SIZE, self.PADDLE_SPEED, self.PADDLE_START_POS,
                        self.PADDLE_SIZE[0], self.PADDLE_SIZE[1], [0, 0, 255])
        self.object_list.append(gameball)
        self.object_list.append(paddle)

    def start_game(self):
        screen = pygame.display.set_mode(self.SCREEN_SIZE)
        clock = pygame.time.Clock()

        while True:
            left = False
            right = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                left = True
            if keys[pygame.K_RIGHT]:
                right = True
            for object in self.object_list:
                object.update(left=left, right=right)
                object.check_collision()

            screen.fill(self.BACKGROUND_COLOR)
            for ball in self.object_list:
                ball.draw(screen, pygame)

            clock.tick(60)
            pygame.display.flip()

    def main(self):
        pygame.init()
        self.build_level()
        self.start_game()
        pygame.quit()


if __name__ == "__main__":
    breakout = GameManager()
    breakout.main()
