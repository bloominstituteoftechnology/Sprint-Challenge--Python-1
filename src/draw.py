import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800, 400]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(3, 3),
                                    [255, 10, 0], 7)
    object_list.append(kinetic)

    #PADDLE
    block = KineticBlock(Vector2(400,380), 100, 20, [0, 0, 255])
    object_list.append(block)

    #GREEN ROW
    block = BreakingBlock(object_list, Vector2(40, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = BreakingBlock(object_list, Vector2(130, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = BreakingBlock(object_list, Vector2(220, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = BreakingBlock(object_list, Vector2(310, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = BreakingBlock(object_list, Vector2(400, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = BreakingBlock(object_list, Vector2(490, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = BreakingBlock(object_list, Vector2(580, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = BreakingBlock(object_list, Vector2(670, 100), 80, 30, [0, 255, 0])
    object_list.append(block)
    
    block = BreakingBlock(object_list, Vector2(760, 100), 80, 30, [0, 255, 0])
    object_list.append(block)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)

    run_game = True
 
    while run_game == True: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run_game = False
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # object_list[1].position.x = object_list[1].position.x - 0.5
            left = True
        if keys[pygame.K_RIGHT]:
            # object_list[1].position.x = object_list[1].position.x + 0.5
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
