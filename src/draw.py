import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [55, 55, 55]
HB_COLOR = [255, 0, 255] # magenta
EZ_COLOR = [127,255,0] #chart reuse
STANDARD_BLOCK_SIZE = 40
START_SPEED = 20

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(START_SPEED*random.random() - START_SPEED/2, START_SPEED*random.random() - START_SPEED/2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)


    # Beej's code for looping blocks using variables at the top^
    for j in range(5):
        for i in range(10):
            block = BeejBlock(object_list, SCREEN_SIZE,
                        Vector2(i * STANDARD_BLOCK_SIZE + STANDARD_BLOCK_SIZE/2,
                        j * STANDARD_BLOCK_SIZE + STANDARD_BLOCK_SIZE/2),
                        STANDARD_BLOCK_SIZE, STANDARD_BLOCK_SIZE, [20*j, 0, 255-10*i])
            object_list.append(block)


    b1 = HardBlock(object_list, Vector2(50, 70), 100, 35, HB_COLOR)
    b2 = HardBlock(object_list, Vector2(200, 70), 100, 35, HB_COLOR)
    b3 = HardBlock(object_list, Vector2(350, 70), 100, 35, HB_COLOR)
    object_list.extend([b1, b2, b3])

    b4 = EzBlock(object_list, Vector2(50, 150), 100, 35, EZ_COLOR)
    b5 = EzBlock(object_list, Vector2(200, 150), 100, 35, EZ_COLOR)
    b6 = EzBlock(object_list, Vector2(350, 150), 100, 35, EZ_COLOR)
    object_list.extend([b4, b5, b6]) 

    paddle = Paddle(Vector2(200, 700), 200, 50, [0,206,209])
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
