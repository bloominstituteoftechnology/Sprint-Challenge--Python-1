import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]
BRICK_LIST = []
BRICK_COUNT = 5

for i in range(BRICK_COUNT):
    BRICK_LIST.append(i)

print(BRICK_LIST)


def debug_create_objects(object_list):

    kinetic = GameBall(
        1,
        object_list,
        SCREEN_SIZE,
        Vector2(random.randint(20, SCREEN_SIZE[0] - 20),
                random.randint(20, SCREEN_SIZE[1] - 20)),
        Vector2(16*random.random() - 2, 16*random.random() - 2),
        [255, 10, 0],
        20
    )

    paddle = Paddle(Vector2(300, 460), 175, 25, [0, 0, 255])

    object_list.append(kinetic)
    object_list.append(paddle)

    # for y in range(5):
    #     for x in range(5):
    #         block = KineticBlock(Vector2(x * 25, y * 25),
    #                              20, 20, [0, 0, 255])
    #         object_list.append(block)

    block = Single_Hit_Block(Vector2(300, 100), 100, 100, [0, 0, 255])
    object_list.append(block)


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
            # object_list[0].position[0] -= 1
            object_list[1].paddle_left()

        if keys[pygame.K_RIGHT]:
            # Do something
            # object_list[0].position[0] += 1
            object_list[1].paddle_right()

        for object in object_list:
            object.update()
            object.check_collision()
            if hasattr(object, 'hits'):
                if getattr(object, 'hits') <= 0:
                    object_list.remove(object)

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
