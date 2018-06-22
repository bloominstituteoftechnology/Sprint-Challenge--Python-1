import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    block = KineticBlock(Vector2(200,470), 100, 20, [0, 0, 255])
    object_list.append(block)
  
    breakable_block = BreakableBlock(Vector2(50,30), 100, 20, [0, 255, 0])
    object_list.append(breakable_block)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
    pygame.mouse.set_visible(False)
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            # Do something
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
            if not (issubclass(type(ball), BreakableBlock) and ball.should_draw == False):
                ball.draw(screen, pygame)
            # if issubclass(type(ball), BreakableBlock):
            #     if ball.should_draw == False:
            #         print("dont draw")
            #     else:
            #         ball.draw(screen, pygame)    
            # else:
            #     ball.draw(screen, pygame)
                
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
