import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *
# from paddle import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE,
                       Vector2(random.randint(
                           20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                       Vector2(4*random.random() - 2, 4*random.random() - 2),
                       [255, 10, 0], 20)
    object_list.append(kinetic)
    paddle = Paddle(
        Vector2(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - 20), SCREEN_SIZE[0] / 3, 10, [0, 0, 0])
    object_list.append(paddle)

    block = VanishingBlock(Vector2(200, 200), 100, 100, [0, 0, 255], 2)
    object_list.append(block)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    while len(object_list) > 2:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            object_list[0].velocity[1] += 1

        if keys[pygame.K_LEFT]:
            # Do something
            # print(object_list[1].position)
            if not object_list[1].position[0] <= 0:
                newX = object_list[1].position[0] - 5
                # print(newX)
                object_list[1].update(x=newX)

        if keys[pygame.K_RIGHT]:
            # Do something
            # print(object_list[1].position)

            if not object_list[1].position[0] >= SCREEN_SIZE[0]:
                newX = object_list[1].position[0] + 5
                object_list[1].update(x=newX)

        for object in object_list:
            object.update()
            object.check_collision()

        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for object in object_list:
            if isinstance(object, KineticBlock):
                if object.touched_by_ball == True:
                    object_list.remove(object)
                else:
                    object.draw(screen, pygame)
            object.draw(screen, pygame)

        # if len(object_list) == 2:
        #     print("Game Over! YOU WIN!")
        #     pygame.quit()

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
