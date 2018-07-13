import pygame
import random
import sys

from pygame.math import Vector2
from ball import GameBall
from block import KineticBlock, Paddle, Brick

# TODO: Break levels out to own class
level_1 = [
    {"row": 1, "color": [255, 0, 0]},
    {"row": 2, "color": [255, 0, 0]},
    {"row": 3, "color": [255, 153, 51]},
    {"row": 4, "color": [255, 153, 51]},
    {"row": 5, "color": [0, 204, 0]},
    {"row": 6, "color": [0, 204, 0]},
    {"row": 7, "color": [255, 255, 0]},
    {"row": 8, "color": [255, 255, 0]}
]

levels = [level_1]

class GameManager:
    def __init__(self, levels):
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
        self.PADDLE_SPEED = 6
        self.PADDLE_SIZE = [34, 8]
        self.BRICK_SIZE = [50, 20]
        self.BRICKS_PER_ROW = int(self.SCREEN_SIZE[0]/self.BRICK_SIZE[0])

        self.levels = levels
        self.object_list = []

    def build_level(self):
        # TODO: Create game blocks: multi hit block
        gameball = GameBall(1, self.object_list, self.SCREEN_SIZE, self.GAMEBALL_START_POS,
                            self.GAMEBALL_VELOCITY, self.GAMEBALL_COLOR, self.GAMEBALL_SIZE)
        paddle = Paddle(self.SCREEN_SIZE, self.PADDLE_SPEED, self.PADDLE_START_POS,
                        self.PADDLE_SIZE[0], self.PADDLE_SIZE[1], [0, 0, 255])
        
        self.object_list.append(gameball)
        self.object_list.append(paddle)

        for level in self.levels:
            for row in level:
                self.build_row(self.BRICKS_PER_ROW, Brick, row["row"], row["color"])
    
    def build_row(self, num_bricks, brick_type, row, color):
        pos_x = self.BRICK_SIZE[0]/2
        pos_y = self.BRICK_SIZE[1] * row

        for i in range(num_bricks):
            game_brick = brick_type(self.object_list, 1, Vector2(
                pos_x, pos_y), self.BRICK_SIZE[0], self.BRICK_SIZE[1], color)
            self.object_list.append(game_brick)
            pos_x += 50

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
            for object in self.object_list:
                object.draw(screen, pygame)

            clock.tick(60)
            pygame.display.flip()

    def main(self):
        pygame.init()
        self.build_level()
        self.start_game()
        pygame.quit()


if __name__ == "__main__":
    breakout = GameManager(levels)
    breakout.main()
