import pygame #TODO:  Fix intellisense
import random
import math

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # for i in range(5):
    #     blocks = Block((50, 50, 50, [0,0,255] )
    #     return blocks
    #     print(blocks)

        # object_list.append(blocks)

        #TODO Make a block loop:
    block = breakBlock(Vector2(35,20), 60, 60, [0, 0, 255], 1)
    object_list.append(block)
    block2 = breakBlock(Vector2(100,20), 60, 60, [0, 0, 255], 1)
    object_list.append(block2)
    block3 = breakBlock(Vector2(165,20), 60, 60, [0, 0, 255], 1)
    object_list.append(block3)
    block4 = breakBlock(Vector2(230,20), 60, 60, [0, 0, 255], 1)
    object_list.append(block4)
    block5 = breakBlock(Vector2(295,20), 60, 60, [0, 0, 255], 1)
    object_list.append(block5)
    block5 = breakBlock(Vector2(360,20), 60, 60, [0, 0, 255], 1)
    object_list.append(block5)
    # block6 = KineticBlock(Vector2(235,20), 60, 60, [0, 0, 255])
    # object_list.append(block6)
    # block7 = KineticBlock(Vector2(335,20), 60, 60, [0, 0, 255])
    # object_list.append(block7)
    # block8 = KineticBlock(Vector2(235,20), 60, 60, [0, 0, 255])
    # object_list.append(block8)
    # block9 = KineticBlock(Vector2(235,20), 60, 60, [0, 0, 255])
    # object_list.append(block9)
    # block10 = KineticBlock(Vector2(235,20), 60, 60, [0, 0, 255])
    # object_list.append(block10)
    playBlock = PlayBlock(Vector2(random.randint(100, 300),700), 70, 20, [255, 0, 255])
    object_list.append(playBlock)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    carryOn = True
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
    pygame.mouse.set_visible(False)
    while carryOn: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            # elif event.type==pygame.KEYDOWN:
            #     if event.key==pygame.K_x:
            #         carryOn=False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            PlayBlock.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            PlayBlock.K_moveRight(5)

        keys = pygame.key.get_pressed()
        # keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            PlayBlock.moveLeft(1)
        if keys[pygame.K_RIGHT]:
            PlayBlock.moveRight(1)

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
