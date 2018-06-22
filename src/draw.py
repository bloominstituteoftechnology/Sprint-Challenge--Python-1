import pygame  # TODO:  Fix intellisense
import random
import sys, os
from pygame.locals import *

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800, 400]
BACKGROUND_COLOR = [255, 255, 255]
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 25
TOTAL_BLOCKS = 8
BLOCK_STARTING_POS = [85, 25]
BLOCK_ROWS = 4
BLOCK_COLS = 7
BLOCK_SPACING = 5

PADDLE_WIDTH = 76
PADDLE_HEIGHT = 20
PADDLE_STARTING_POS = [((SCREEN_SIZE[0] - PADDLE_WIDTH / 2) / 2), (SCREEN_SIZE[1] - 25)]


def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE,
                       Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                       # Vector2(4*random.random() - 2, 4*random.random() - 2),
                       Vector2(10, 10),
                       [255, 10, 0], 15)
    object_list.append(kinetic)

    # Create blocks
    x = BLOCK_STARTING_POS[0]
    y = BLOCK_STARTING_POS[1]
    for i in range(BLOCK_ROWS):
        for j in range(BLOCK_COLS):
            rand_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            block = KineticBlock(Vector2(x, y), BLOCK_WIDTH, BLOCK_HEIGHT, rand_color)
            object_list.append(block)
            x += BLOCK_WIDTH + BLOCK_SPACING
        x = BLOCK_STARTING_POS[0]
        y += BLOCK_HEIGHT + BLOCK_SPACING


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    # Create paddle
    paddle = Paddle(Vector2(PADDLE_STARTING_POS), PADDLE_WIDTH, PADDLE_HEIGHT, [0, 0, 0])
    object_list.append(paddle)

    while True:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.position.x -= 5
            paddle.rectangle = pygame.Rect(
                paddle.position.x,
                paddle.position.y,
                PADDLE_WIDTH,
                PADDLE_HEIGHT)
            print(paddle.position)

        if keys[pygame.K_RIGHT]:
            # Do something
            paddle.position.x += 5
            paddle.rectangle = pygame.Rect(
                paddle.position.x,
                paddle.position.y,
                PADDLE_WIDTH,
                PADDLE_HEIGHT)
            print(paddle.position)

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