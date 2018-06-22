import sys
import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]

BALL_VELOCITY = 8
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
PADDLE_VELOCITY = 10

BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(BALL_VELOCITY*random.random() - 2, BALL_VELOCITY*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    # block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255])
    # object_list.append(block)

    paddle = PaddleBlock(Vector2(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] - PADDLE_HEIGHT), PADDLE_WIDTH, PADDLE_HEIGHT, [255, 0, 255], PADDLE_VELOCITY)
    object_list.append(paddle)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            print('event: ', event)
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            object_list[1].paddle_to_left()

        if keys[pygame.K_RIGHT]:
            object_list[1].paddle_to_right(PADDLE_WIDTH, SCREEN_SIZE[0])

        for object in object_list:
            object.update()
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for obj in object_list:
            obj.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
