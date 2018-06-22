import pygame  # TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]
DIFFICULTY = 5
PADDLE_WIDTH = 150
PADDLE_HEIGHT = 25


def debug_create_objects(object_list):
    ball = GameBall(1, object_list, SCREEN_SIZE,
                    Vector2(random.randint(
                        20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                    Vector2(DIFFICULTY, DIFFICULTY),
                    [255, 10, 0], 20)
    invincible_block = KineticBlock(Vector2(200, 200), 50, 50, [0, 255, 120])
    vanishing_block = DisappearingBlock(
        Vector2(100, 100), 50, 50 [125, 0, 125])
    paddle = Paddle(Vector2(
        SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-20), PADDLE_WIDTH, PADDLE_HEIGHT, [0, 0, 0])
    object_list += [ball, invincible_block,
                    vanishing_block, resilient_block, paddle]


def main():
    timer = 0
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    while True:  # TODO:  Create more elegant condition for loop
        ball = object_list[0]
            paddle = object_list[-1]

            if ball.dropped_count > 2:
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Do something
            paddle.position.x = max(PADDLE_WIDTH//2, paddle.position.x - 5)
            paddle.update()

            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            paddle.position.x = min(
                SCREEN_SIZE[0]-PADDLE_WIDTH//2, paddle.position.x + 5)
            paddle.update()
            pass

        for object in object_list:
            object.check_collision()
            object.update()

        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)

        clock.tick(60)
        timer += 1
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
