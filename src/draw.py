import pygame #TODO:  Fix intellisense
import random
import sys #removes sys err msg

from pygame.math import Vector2

from ball import *
from block import *
from paddle import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255] #black

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(25*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 10)
    object_list.append(kinetic)

    block = KineticBlock(Vector2(280,500), 70, 100, [0, 250, 0])
    object_list.append(block)

    paddle = Paddle(Vector2(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - 20), SCREEN_SIZE[0] / 4, 10, [0, 0, 0])
    object_list.append(paddle)

# imports not working so had to create my paddle in this file (not working atm)
#creating paddle.py
 
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
            if isinstance(object,Block):
                object.update(right,left)
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
