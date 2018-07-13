import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [55, 55, 55]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)
    b1 = HardBlock(Vector2(50, 100), 100, 75, [255, 0, 255])
    b2 = HardBlock(Vector2(200, 100), 100, 75, [255, 0, 255])
    b3 = HardBlock(Vector2(350, 100), 100, 75, [255, 0, 255])
    object_list.extend([b1, b2, b3])

    b4 = EzBlock(Vector2(50, 200), 100, 75, [127,255,0])
    b5 = EzBlock(Vector2(200, 200), 100, 75, [127,255,0])
    b6 = EzBlock(Vector2(350, 200), 100, 75, [127,255,0])
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
