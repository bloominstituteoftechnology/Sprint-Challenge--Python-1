import pygame  # TODO:  Fix intellisense
import random
from pygame.math import Vector2
from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]


# def debug_create_objects(object_list):
#     kinetic = GameBall(1, object_list, SCREEN_SIZE,
#                        Vector2(random.randint(
#                            20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
#                        Vector2(4*random.random() - 2, 20),
#                        [0, 255, 0], 15)
#     object_list.append(kinetic)

#     block = KineticBlock(Vector2(200, 200), 50, 25, [0, 0, 0])
#     object_list.append(block)


def new_game(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, Vector2(random.randint(
        20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)), Vector2(4*random.random() - 2, 20), [0, 255, 0], 15)
    object_list.append(kinetic)

    paddle = Paddle(Vector2(200, 700), 25, 10, [0, 0, 0])
    object_list.append(paddle)

    for x in range(3):
        block = KineticBlock(
            Vector2((x * 133) + 62.5, 100), 25, 25, [0, 0, 255])
        object_list.append(block)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    new_game(object_list)

    while True:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Do something
            # obj list 1 which is a block located near the bottom of play area.. decrement pos x
            # print("Left key is pressed..")
            print("The paddle.. ", object_list[1].position)
            object_list[1].position[0] -= 10
            print("The paddle.. ", object_list[1].position)
            # object_list[1].update(move_left)
            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            # obj list 1 increment pos x
            # print("Right key is pressed..")
            print("The paddle.. ", object_list[1].position)
            object_list[1].position[0] += 10
            print("The paddle.. ", object_list[1].position)
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
