import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [0, 0, 0]
# BALL_SPEED = 50

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, 
                                    SCREEN_SIZE, # bounds
                                    # randomized starting position 
                                    Vector2(random.randint(30, SCREEN_SIZE[0] - 10), random.randint(10, SCREEN_SIZE[1] - 10)),
                                    # velocity
                                    # Two random numbers between -2 and 2 -- Why would you randomize the velocity?
                                    Vector2(-2, 2), # was `4*random.random() - 2`
                                    [255, 255, 255], # color
                                    10) # radius
    object_list.append(kinetic)

    block = KineticBlock(Vector2(200,790), 100, 20, [255, 0, 0])
    object_list.append(block)
  
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
            
            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            
            pass

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
