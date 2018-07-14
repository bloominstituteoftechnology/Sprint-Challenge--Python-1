import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 700]
BACKGROUND_COLOR = [255, 255, 255]
STANDARD_BLOCK = 40

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE,
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(20*random.random() - 2, 20*random.random() - 2),
                                    [255, 10, 0], 15)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)


    breakable = lambda i, J, k: BreakableBlock(object_list, SCREEN_SIZE, Vector2(20+(i*60), j * 50),60,30,[125,0,10])
    breakableblocks = []

    for i in range(0, 10):
        for j in range(1, 10):
            for k in range(2, 10):
                if i % 2 == 0:
                    breakableblocks.append(breakable(i, j, k))

    object_list.extend(breakableblocks)

    paddle = Paddle(SCREEN_SIZE, Vector2(200,600), 150, 20, [25, 55, 0])
    object_list.append(paddle)



def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = [] # list of objects of all types in the toy

    debug_create_objects(object_list)

    while True: # TODO:  Create more elegant condition for loop
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
