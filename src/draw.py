import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [0, 0, 0]
GAME_BLOCK_COLOR = [150,150,150]

# TODO: random RGB color generator for Blocks to be Destroyed
def rgb_color():
   return [random.randint(150, 255),random.randint(150, 255),random.randint(150, 255)]
    


def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, 
                                    SCREEN_SIZE, # bounds
                                    # randomized starting position 
                                    Vector2(random.randint(30, SCREEN_SIZE[0] - 10), random.randint(10, SCREEN_SIZE[1] - 10)),
                                    # velocity
                                    # Two random numbers between -2 and 2 -- Why would you randomize the velocity?
                                    Vector2(-2, 2), # was `4*random.random() - 2`
                                    rgb_color(), # color
                                    10) # radius
    object_list.append(kinetic)

    # User Block
    block = KineticBlock(Vector2(200,790), 100, 20, rgb_color())
    object_list.append(block)

    # Blocks to be Destroyed by User
    dblock_1 = KineticBlock(Vector2(25,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_1)
    dblock_2 = KineticBlock(Vector2(75,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_2)
    dblock_3 = KineticBlock(Vector2(125,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_3)
    dblock_4 = KineticBlock(Vector2(175,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_4)
    dblock_5 = KineticBlock(Vector2(225,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_5)
    dblock_6 = KineticBlock(Vector2(275,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_6)
    dblock_7 = KineticBlock(Vector2(325,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_7)
    dblock_8 = KineticBlock(Vector2(375,10), 40, 20, GAME_BLOCK_COLOR)
    object_list.append(dblock_8)


  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print(object_list[1].position[0])
            object_list[1].position[0] += 1
            print(object_list[1].position[0])
            
            
            
        if keys[pygame.K_RIGHT]:
            # Do something
            # print(object_list[0]) # ball.GameBall object x 8
            # print(object_list[1]) # block.KineticBlock object x 1
            # print(object_list[2]) # block.KineticBlock object x 1
            # print(len(object_list)) # 10... 1 ball, 1 user block, 8 blocks to destroy
            print(object_list[1].position[0])
            object_list[1].position[0] -= 1
            print(object_list[1].position[0])
            # TODO: Figure out how to implement super().update() .. like in OOP-Toy            
            

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
