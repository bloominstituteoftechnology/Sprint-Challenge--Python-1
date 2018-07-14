import pygame  #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 700]
BACKGROUND_COLOR = [255, 255, 255]

STANDARD_BLOCK_SIZE = 40

def load_level(object_list):
    kinetic = GameBall(
        1, object_list, SCREEN_SIZE,
        Vector2(
            random.randint(20, SCREEN_SIZE[0] - 20),
            random.randint(20, SCREEN_SIZE[1] - 20)),
        Vector2(4 * random.random() - 2, 4 * random.random() - 2),
        [255, 10, 0], 20)
    object_list.append(kinetic)

    for j in range(5): 
        for i in range(10): 
            block = Breakable(object_list, SCREEN_SIZE, 
                Vector2(i * STANDARD_BLOCK_SIZE + STANDARD_BLOCK_SIZE/2, 
                j * STANDARD_BLOCK_SIZE + STANDARD_BLOCK_SIZE/2), 
                STANDARD_BLOCK_SIZE, STANDARD_BLOCK_SIZE, 
                [20*j, 0, 255-20*j])
            object_list.append(block)

    paddle = Paddle(SCREEN_SIZE, Vector2(200, 650), 100, 25, [128, 128, 128])
    object_list.append(paddle)

def main():

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    load_level(object_list)

    while True:  # TODO:  Create more elegant condition for loop
        left = False
        right = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            object.update(left=left, right=right)
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
