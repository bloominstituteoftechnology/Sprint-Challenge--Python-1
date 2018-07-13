import pygame #TODO:  Fix intellisense
import random

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

    # first roll of blocks
    # hard coded just for testing purposes
    block = KineticBlock( Vector2(0,0),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(85,0),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(170,0),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(255,0),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(340,0),75, 20, [0, 0, 255])
    object_list.append(block)

    #second roll of blocks
    #hard coded just for testing purposes
    block = KineticBlock( Vector2(0,30),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(85,30),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(170,30),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(255,30),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(340,30),75, 20, [0, 0, 255])
    object_list.append(block)

    block = KineticBlock( Vector2(0,60),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(85,60),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(170,60),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(255,60),75, 20, [0, 0, 255])
    object_list.append(block)
    block = KineticBlock( Vector2(340,60),75, 20, [0, 0, 255])
    object_list.append(block)


    # bar = KineticBlock(Vector2(200,700), 130, 30, [0, 0, 255])
    # object_list.append(bar)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    # keys = pygame.key.get_pressed()
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
 
    object_list = [] # list of objects of all types in the toy
    bar = KineticBlock(Vector2(200,700), 130, 30, [0, 0, 255])
    object_list.append(bar)
    
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
            print("pressed left")
            bar.position[0] = bar.position[0] - 1
            
            print(bar.position[0])
        if keys[pygame.K_RIGHT]:
            right = True
            print("press right")
            bar.position[0] = bar.position[0] + 1
            print(bar.position[0])
        object_list.append(bar)
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
