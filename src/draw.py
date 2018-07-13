import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
S_WIDTH = 400
S_HEIGHT = 800
BACKGROUND_COLOR = [255, 255, 255]
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 30

NUMBER_OF_BLOCKS = 6
BLOCK_WIDTH = S_WIDTH / NUMBER_OF_BLOCKS
BLOCK_HEIGHT = BLOCK_WIDTH / 2


def debug_create_objects(object_list):
    kinetic = GameBall(
        1,
        object_list,
        SCREEN_SIZE,
        Vector2(
            random.randint(20, SCREEN_SIZE[0] - 20),
            random.randint(20, SCREEN_SIZE[1] - 20),
        ),
        Vector2(4 * random.random() - 2, 4 * random.random() - 2),
        [255, 10, 0],
        20,
    )
    object_list.append(kinetic)

    block = KineticBlock(
        Vector2(S_WIDTH / 2, S_HEIGHT - 20), PADDLE_WIDTH, PADDLE_HEIGHT, [0, 0, 255]
    )
    object_list.append(block)
    # CREATE BLOCKS

    for i in range(3):
        blocks = []  # WIP
        color = [104, 237, 126]
        for x in range(3):
            block = KineticBlock(
                Vector2(72 + (i * 124), 100 + (x * 40)), 120, 30, color
            )
            object_list.append(block)


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

        # TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            if isinstance(object, Block):
                object.update(right, left)
                object.check_collision()
            else:
                object.update()
                object.check_collision()

        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
        # for i in range(len(blocks)):
        #     blocks[i].draw(display)
        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
