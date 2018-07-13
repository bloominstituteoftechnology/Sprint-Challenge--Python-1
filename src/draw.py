import pygame #TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(6*random.random() , 6*random.random() ),
                                    [255, 10, 0], 10)
    object_list.append(kinetic)

    # block = Breakable(Vector2(200,200), 100, 10, [0, 50, 255])
    # object_list.append(block)
    # block = Breakable(Vector2(200,220), 100, 10, [0, 100, 255])
    # object_list.append(block)
    # block = Breakable(Vector2(200,240), 100, 10, [0, 150, 255])
    # object_list.append(block)
    # block = Breakable(Vector2(200,260), 100, 10, [0, 200, 255])
    # object_list.append(block)
    x = 25
    for i in range(0,7):
        block = Breakable(Vector2(x,200), 50, 10, [0, 50, 255])
        object_list.append(block)
        x += 60

    x = 25
    for i in range(0,7):
        block = HarderToBreak(Vector2(x,220), 50, 10, [0, 50, 0])
        object_list.append(block)
        x += 60

    paddle = Paddle(Vector2(200,700), 100, 10, [0, 0, 0])
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
            # print("left")
            left = True
            
        if keys[pygame.K_RIGHT]:
            right = True
        for object in object_list:
            # object.update()
            object.update(left=left, right=right, list=object_list)
            object.check_collision()
        # print(object_list[2])  
        # object_list[2].move(left, right)  
 
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
