import pygame #TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [0, 0, 0]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    object_list.append(block)

    paddle = PaddleBlock(object_list, Vector2(150, 749), 120, 15, [104, 104, 104])
    object_list.append(paddle)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Breakout-Clone")
    pygame.mouse.set_pos(0, 0)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    done = False

    while not done: # TODO:  Create more elegant condition for loop xx
        left = False
        right = False
        motion = False        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True
                print("Thank you for playing!")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                    print("left arrow was pressed!")
                elif event.key == pygame.K_RIGHT:
                    right = True
                    print("right arrow was pressed!")
                elif event.key == pygame.K_ESCAPE:
                    done = True
                    print("You've escaped the game!")
            elif event.type == pygame.MOUSEMOTION:
                #get mouse position
                x, y = pygame.mouse.get_pos()
                print(x, y)
                continue
        
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
