import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE,
                       Vector2(random.randint(
                           20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                       Vector2(4*random.random() - 2, 4*random.random() - 2),
                       [255, 10, 0], 20)
    object_list.append(kinetic)

    block_array = []
    vx = 43
    vy = 25

    for i in range(30):
        block = KineticBlock(Vector2(vx, vy), 70, 30, [0, 0, 255])
        object_list.append(block)
        vx += 78
        if vx > 360:
            vx = 43
            vy += 35

    # block = KineticBlock(Vector2(40, 25), 70, 30, [0, 0, 255])
    # object_list.append(block)
    # block = KineticBlock(Vector2(118, 25), 70, 30, [0, 0, 255])
    # object_list.append(block)
    # block = KineticBlock(Vector2(196, 25), 70, 30, [0, 0, 255])
    # object_list.append(block)
    # block = KineticBlock(Vector2(274, 25), 70, 30, [0, 0, 255])
    # object_list.append(block)
    # block = KineticBlock(Vector2(360, 25), 70, 30, [0, 0, 255])
    # object_list.append(block)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    while True:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Do something
            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            pass

        for object in object_list:
            object.update()
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
