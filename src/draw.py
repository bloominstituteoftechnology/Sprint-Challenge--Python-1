import sys
import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import GameBall
from block import KineticBlock, Paddle, Vanish, SlowVanish

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

STANDARD_BLOCK_SIZE = 40


def debug_create_objects(object_list):
    kinetic = GameBall(
        1,  # mass
        object_list,  # object_list
        SCREEN_SIZE,  # bounds
        Vector2(SCREEN_SIZE[0] / 2, 700),  # position
        Vector2(2, 6),  # velocity
        [255, 10, 0],  # color
        20,  # radius
    )
    object_list.append(kinetic)
    for j in range(8):
        for i in range(10):
            die_roll = random.random()
            if die_roll < .475:
                block = SlowVanish(
                    object_list,
                    SCREEN_SIZE,
                    Vector2(
                        i * (STANDARD_BLOCK_SIZE + 5) + STANDARD_BLOCK_SIZE / 2,
                        j * (STANDARD_BLOCK_SIZE + 5) + STANDARD_BLOCK_SIZE / 2,
                    ),
                    STANDARD_BLOCK_SIZE,
                    STANDARD_BLOCK_SIZE,
                    [0, 0, 255],
                )
                object_list.append(block)
            elif die_roll < .95:
                block = Vanish(
                    object_list,
                    SCREEN_SIZE,
                    Vector2(
                        i * (STANDARD_BLOCK_SIZE + 5) + STANDARD_BLOCK_SIZE / 2,
                        j * (STANDARD_BLOCK_SIZE + 5) + STANDARD_BLOCK_SIZE / 2,
                    ),
                    STANDARD_BLOCK_SIZE,
                    STANDARD_BLOCK_SIZE,
                    [0, 0, 255],
                )
                object_list.append(block)
            else:
                block = KineticBlock(
                    object_list,  # object_list
                    SCREEN_SIZE,  # bounds
                    Vector2(
                        i * (STANDARD_BLOCK_SIZE + 5) + STANDARD_BLOCK_SIZE / 2,
                        j * (STANDARD_BLOCK_SIZE + 5) + STANDARD_BLOCK_SIZE / 2,
                    ),  # position
                    STANDARD_BLOCK_SIZE,
                    STANDARD_BLOCK_SIZE,
                    [0, 0, 10],  # color
                )
                object_list.append(block)

    paddle = Paddle(
        object_list, SCREEN_SIZE, Vector2(SCREEN_SIZE[0] / 2, 770), 100, 20, [0, 0, 0]
    )
    object_list.append(paddle)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    while True:  # TODO:  Create more elegant condition for loop
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
        for item in object_list:
            if isinstance(item, Paddle):
                item.update(left, right)
            else:
                item.update()
            item.check_collision()

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
