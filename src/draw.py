import pygame #TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800, 400]
BACKGROUND_COLOR = [255, 250, 231]

def debug_create_objects(object_list):
    #main ball in game
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [240, 197, 202], 20)
    object_list.append(kinetic)
    print(object_list)

    #blocks at top of screen
    block = TopBlock(Vector2(200,20), 100, 30, [156, 214, 184])
    object_list.append(block)
    block = TopBlock(Vector2(400,20), 100, 30, [156, 214, 184])
    object_list.append(block)
    block = TopBlock(Vector2(600,20), 100, 30, [156, 214, 184])
    object_list.append(block)
    block = TopBlock(Vector2(200,60), 100, 30, [0, 214, 200])
    object_list.append(block)
    block = TopBlock(Vector2(400,60), 100, 30, [0, 214, 200])
    object_list.append(block)
    block = TopBlock(Vector2(600,60), 100, 30, [0, 214, 200])
    object_list.append(block)
 
    #paddle
    paddle = KineticBlock(Vector2(400,390), 80, 20, [234, 112, 90])
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
            for object in object_list:

                if isinstance(object, Block):
                    object.update(left, right)
                    object.check_collision()
                else:
                    object.update()
                    object.check_collision()

        if keys[pygame.K_RIGHT]:
            right = True
            for object in object_list:

                if isinstance(object, Block):
                    object.update(left, right)
                    object.check_collision()
                else:
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
