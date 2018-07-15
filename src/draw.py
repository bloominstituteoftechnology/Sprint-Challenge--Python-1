import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

# SCREEN_SIZE = [640, 480]

SCREEN_SIZE = [400, 600]
BACKGROUND_COLOR = [255, 255, 255]
PADDLE_WIDTH = 150
PADDLE_HEIGHT = 60

def load_level(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    block = KineticBlock(Vector2(200,200), 100, 100, [0, 0, 255], 50)
    object_list.append(block)

    paddle = Paddle(SCREEN_SIZE, Vector2(200, 600), 100,  [50, 50, 199])
    object_list.append(paddle)

    breakable = Breakable(Vector2(400,400), 100, 50, [255, 0, 0])
    object_list.append(breakable)

    block_3 = KineticBlock(Vector2(50, 100), 30, 70, [255, 255, 0])
    object_list.append(block_3)

    block_4 = KineticBlock(Vector2(100, 500), 150, 50, [0, 255, 0])
    object_list.append(block_4)

  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    load_level(object_list)


    while True: # TODO:  Create more elegant condition for loop
        left = False
        right = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        # TODO:  Feed input variables into update for objects that need it.

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