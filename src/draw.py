import pygame  # TODO:  Fix intellisense

import pygame  # TODO:  Fix intellisense
from ball import *
from block import *
from pygame.math import Vector2

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):

    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
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

    block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    block = KineticBlock(Vector2(200, 200), 100, 100, [0, 0, 255])


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = [] # list of objects of all types in the toy
    object_list = []  # list of objects of all types in the toy


    while True: # TODO:  Create more elegant condition for loop
    while True:  # TODO:  Create more elegant condition for loop
        right = False
        

            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

        # TODO:  Feed input variables into update for objects that need it.
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
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
