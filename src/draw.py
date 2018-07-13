import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [0, 0, 0]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(200 , 700),
                                    Vector2(2.5 , -2.5),
                                    [255, 0, 255], 5)
    object_list.append(kinetic)

    paddle = Paddle(SCREEN_SIZE, Vector2(200,720), 75, 10, [255, 0, 255])
    object_list.append(paddle)

    # block array
    block1 = KineticBlock(object_list, Vector2(35,200), 50, 20, [0, 0, 255])
    object_list.append(block1)

    block2 = StrongKineticBlock(object_list, Vector2(90,200), 50, 20, [0, 0, 255], 2)
    object_list.append(block2)

    block3 = KineticBlock(object_list, Vector2(145,200), 50, 20, [0, 0, 255])
    object_list.append(block3)

    block4 = KineticBlock(object_list, Vector2(200,200), 50, 20, [0, 0, 255])
    object_list.append(block4)

    block5 = KineticBlock(object_list, Vector2(255,200), 50, 20, [0, 0, 255])
    object_list.append(block5)

    block6 = KineticBlock(object_list, Vector2(310,200), 50, 20, [0, 0, 255])
    object_list.append(block6)
    
    block7 = KineticBlock(object_list, Vector2(365,200), 50, 20, [0, 0, 255])
    object_list.append(block7)

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
