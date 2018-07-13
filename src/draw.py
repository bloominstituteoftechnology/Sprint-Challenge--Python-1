import sys
import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import GameBall
from block import Paddle, Vanish, SlowVanish

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    kinetic = GameBall(
        1,  # mass
        object_list,  # object_list
        SCREEN_SIZE,  # bounds
        Vector2(
            random.randint(20, SCREEN_SIZE[0] - 20),
            random.randint(20, SCREEN_SIZE[1] - 20),
        ),  # position
        Vector2(2, 12),  # velocity
        [255, 10, 0],  # color
        20,  # radius
    )
    object_list.append(kinetic)
    block = SlowVanish(
        Vector2(50, 20), 50, 10, [0, 0, 255]
    )  # position width height color
    object_list.extend((block,))
    block = SlowVanish(
        Vector2(151, 20), 50, 10, [0, 0, 255]
    )  # position width height color
    object_list.extend((block,))
    block = Vanish(Vector2(252, 20), 50, 10, [0, 0, 255])  # position width height color
    object_list.extend((block,))
    block = Vanish(Vector2(353, 20), 50, 10, [0, 0, 255])  # position width height color
    object_list.extend((block,))
    block = SlowVanish(
        Vector2(50, 80), 50, 10, [0, 0, 255]
    )  # position width height color
    object_list.extend((block,))
    block = Vanish(Vector2(151, 80), 50, 10, [0, 0, 255])  # position width height color
    object_list.extend((block,))
    block = Vanish(Vector2(252, 80), 50, 10, [0, 0, 255])  # position width height color
    object_list.extend((block,))
    block = SlowVanish(
        Vector2(353, 80), 50, 10, [0, 0, 255]
    )  # position width height color
    object_list.extend((block,))

    block = Paddle(Vector2(1, 799), 100, 100, [0, 0, 0])
    object_list.extend((block,))


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
                item.update(right, left)
            elif isinstance(item, Vanish) or isinstance(item, SlowVanish):
                item.update(object_list)
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
