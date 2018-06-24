import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

PADDLE_SIZE = [100, 15]
PADDLE_COLOR = [100, 100, 100]

GAME_BALL_SIZE = 15

BRICK_LIST = []
BRICK_COUNT = 5
KINETIC_BLOCK_COLOR = [0, 0, 255]
BREAKABLE_BLOCK_COLOR = [0, 255, 0]
STRONG_BLOCK_COLOR = [255, 0, 0]


def debug_create_objects(object_list):

    kinetic = GameBall(
        1,
        object_list,
        SCREEN_SIZE,
        Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2),
        Vector2(0, 0),
        [255, 10, 0],
        GAME_BALL_SIZE
    )

    paddle = Paddle(
        Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1] - 10), PADDLE_SIZE[0], PADDLE_SIZE[1], PADDLE_COLOR)

    object_list.append(kinetic)
    object_list.append(paddle)

    for x in range(6):
        for y in range(6):
            block = BreakableBlock(Vector2(x * 65 + SCREEN_SIZE[0]/10, y * 20 + 20),
                                   55, 15, BREAKABLE_BLOCK_COLOR)

            block_2 = StrongBlock(Vector2(x * 65 + SCREEN_SIZE[
                0]/10, y * 20 + 140),
                55, 15, STRONG_BLOCK_COLOR, 2)

            object_list.append(block)
            object_list.append(block_2)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    while len(object_list) > 2:  # TODO:  Create more elegant condition for loop
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

        for object in object_list:
            object.update(left=left, right=right, pygame=pygame,
                          object_list=object_list)
            object.check_collision()

        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
