import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

PADDLE_SIZE = [75, 15]  # 75
PADDLE_COLOR = [100, 100, 100]

GAME_BALL_MASS = 100
GAME_BALL_SIZE = 10
GAME_BALL_COLOR = [255, 10, 0]
GAME_BALL_VELOCITY = [0, 0]

BRICK_COUNT = 5
KINETIC_BLOCK_COLOR = [0, 0, 255]
BREAKABLE_BLOCK_COLOR = [0, 255, 0]

STRONG_BLOCK_COLOR = [255, 0, 0]
BLOCK_STRENGTH = 3


def debug_create_objects(object_list):

    kinetic = GameBall(
        GAME_BALL_MASS,
        object_list,
        SCREEN_SIZE,
        Vector2(random.randint(
            0, SCREEN_SIZE[0]/2), random.randint(200, SCREEN_SIZE[1]/2)),
        Vector2(GAME_BALL_VELOCITY[0], GAME_BALL_VELOCITY[1]),
        GAME_BALL_COLOR,
        GAME_BALL_SIZE
    )

    paddle = Paddle(
        Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1] - 10), PADDLE_SIZE[0], PADDLE_SIZE[1], PADDLE_COLOR)

    object_list.append(kinetic)
    object_list.append(paddle)

    for x in range(6):
        for y in range(1):

            block = BreakableBlock(Vector2(x * 65 + SCREEN_SIZE[0]/10, y * 20 + 10),
                                   55, 15, BREAKABLE_BLOCK_COLOR)

            block_2 = StrongBlock(Vector2(x * 65 + SCREEN_SIZE[
                0]/10, y * 20 + 100),
                55, 15, STRONG_BLOCK_COLOR, BLOCK_STRENGTH)

            object_list.append(block)
            object_list.append(block_2)


# def add_new_ball(object_list):
#     kinetic_2 = Ball(
#         SCREEN_SIZE,
#         Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2),
#         Vector2(6, 6),
#         [255, 10, 0],
#         GAME_BALL_SIZE
#     )
#     object_list.append(kinetic_2)


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
        up = False
        down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            left = True

        if keys[pygame.K_RIGHT]:
            right = True

        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_DOWN]:
            down = True

        for object in object_list:
            # if len(object_list) == 73:
            #     add_new_ball(object_list)

            object.update(left=left, right=right, pygame=pygame,
                          object_list=object_list, up=up, down=down)
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
