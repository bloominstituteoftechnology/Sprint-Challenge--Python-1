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
                                    Vector2(2, 2),
                                    [240, 197, 202], 20)
    object_list.append(kinetic)
    print(object_list)

    #blocks at top of screen

    #top row of blocks
    block1 = TopBlock(Vector2(50,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block1)
    block2 = TopBlock(Vector2(150,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block2)
    block3 = TopBlock(Vector2(250,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block3)
    block4 = TopBlock(Vector2(350,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block4)
    block5 = TopBlock(Vector2(450,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block5)
    block6 = TopBlock(Vector2(550,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block6)
    block7 = TopBlock(Vector2(650,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block7)
    block8 = TopBlock(Vector2(750,20), 90, 30, [156, 214, 184], object_list)
    object_list.append(block8)

    #bottom row of blocks
    block9 = TopBlock(Vector2(200,60), 100, 30, [0, 214, 200], object_list)
    object_list.append(block9)
    block10 = TopBlock(Vector2(400,60), 100, 30, [0, 214, 200], object_list)
    object_list.append(block10)
    block11 = TopBlock(Vector2(600,60), 100, 30, [0, 214, 200], object_list)
    object_list.append(block11)
 
    #paddle
    paddle = KineticBlock(Vector2(400,390), 80, 20, [234, 112, 90])
    object_list.append(paddle)
    print(object_list)

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
